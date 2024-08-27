import os
import time
import json
import subprocess


from concurrent.futures import ThreadPoolExecutor


from shared_vars import *
from tools import *


def get_common_files():
    """_summary_"""

    print("summarize common files ...")

    global dirs  # target forders
    results = []
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = {executor.submit(get_files, dirs[i]): i for i in range(2)}

    for future in futures:
        results.append(future.result())

    # common files
    with open(PATH_TO_COMMON_FILES, "w") as file:
        json.dump(sorted(set(results[0]) & set(results[1])), file, indent=4)

    # return    # 统计新文件
    with open(PATH_TO_RIGHT_ONLY_FILES, "w") as file:
        json.dump(sorted(set(results[1]) - set(results[0])), file, indent=4)


def get_diff_files():
    """_summary_"""

    print("diff ...")
    with open(PATH_TO_COMMON_FILES, "r") as file:
        data = json.load(file)

    try:
        diff = []
        cnt = 0

        for filename in data:
            cnt += 1
            if cnt % 1000 == 0:
                print("processed", cnt, "files ...")

            command = ["diff", args.dir_1 + filename, args.dir_2 + filename]
            result = subprocess.run(command, capture_output=True, text=True)

            if result.returncode != 0:
                diff.append(filename)

                # TODO: 记录详细差异

        with open(PATH_TO_DIFF_FILES, "w") as file:
            # 记录包含差异的文件名（后缀）
            json.dump(diff, file, indent=4)

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


def pre_processing():
    start = time.time()
    get_common_files()
    get_diff_files()

    print("Preprocessing time:", time.time() - start)


def main():
    """_summary_

    Yields:
        _type_: _description_
    """

    with open(PATH_TO_DIFF_FILES, "r") as file:
        data = json.load(file)

    for line in data:
        line = line.strip()

        # HACK:
        # line = "/clang/include/clang/Basic/FileEntry.h"
        books = [get_functions(dir, line) for dir in dirs]

        new_functions = sorted(
            set(books[1].functions.keys()) - set(books[0].functions.keys())
        )

        functions = []
        for key in sorted(
            set(books[0].functions.keys()) & set(books[1].functions.keys())
        ):
            if books[0].get_string(key) != books[1].get_string(key):
                functions.append(key)

        yield {
            "filename": line,
            "new_functions": new_functions,
            "functions": functions,
        }


if __name__ == "__main__":
    start = time.time()
    # pre_processing()

    with open(PATH_TO_JSON, "w") as file:
        first = True
        file.write("[\n")

        try:
            cnt = 0
            for data in main():
                cnt += 1
                if cnt % 100 == 0:
                    print("get functions from", cnt, "files ...")

                if not first:
                    file.write(",\n")  # 不是第一个对象则添加逗号换行

                json.dump(data, file, indent=4)
                first = False

        except StopIteration:
            pass

        file.write("\n]\n")

    print("Total time:", time.time() - start)
