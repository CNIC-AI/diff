import re
import json
import time


from arguments import parse_args
from get_functions import *


def functions2dict(filename):
    functions = dict()

    for node in get_functions(filename):
        data = node2json(node)

        # 如何定义 key 决定了“新增函数”
        # key = str(
        #     f"{data['namespace']}/{data['class']}/{data['name']}/{data['params']}"
        # )
        key = str(
            f"{data['namespace']}/{data['class']}/{data['name']}"
        )  # without overload

        functions[key] = data["positions"]

    return functions


def main():
    """_summary_"""

    args = parse_args()

    with open("./logs/diff.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        print("processing:", line)

        file_1, file_2 = args.dir_1 + line, args.dir_2 + line
        dict_1, dict_2 = functions2dict(file_1), functions2dict(file_2)

        # 均对 keys 排序
        right_only = sorted(set(dict_2.keys()) - set(dict_1.keys()))
        # TODO:

        common = sorted(set(dict_1.keys()) & set(dict_2.keys()))

        def function2string(filename, start, end):

            # 去看原来的文件
            with open(filename, "r") as file:
                code = "".join(file.readlines()[start - 1 : end])

                def remove_comments():
                    code_no_single_line_comments = re.sub(r"//.*", "", code)
                    code_no_comments = re.sub(
                        r"/\*.*?\*/", "", code_no_single_line_comments, flags=re.DOTALL
                    )

                    # 削减多余空字符（只保留一个）
                    code_precise = re.sub(r"\s+", " ", code_no_comments).strip()
                    return code_precise

                return remove_comments()  # 预处理后的函数

        # TODO: 处理新增函数
        new_functions = []
        for key in right_only:
            new_functions.append(key)

        functions = []
        for key in common:
            if function2string(file_1, *dict_1[key]) != function2string(
                file_2, *dict_2[key]
            ):
                functions.append(key)

        yield {
            "filename": line,
            "new_functions": new_functions,
            "functions": functions,
        }


if __name__ == "__main__":
    start_time = time.time()

    with open("./logs/diff_without_overload.json", "w", encoding="utf-8") as json_file:
        json_file.write("{\n")
        json_file.write('"data": [\n')

        first = True

        try:
            for data in main():
                if not first:
                    json_file.write(",\n")  # 不是第一个对象则添加逗号换行

                json.dump(data, json_file, ensure_ascii=False, indent=4)
                first = False

        except StopIteration:
            pass

        json_file.write("\n")
        json_file.write("]\n")
        json_file.write("}\n")

    elapsed_time = time.time() - start_time

    print(f"Elapsed time: {elapsed_time} seconds")
