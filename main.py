import re
import json


from extract_functions import *


if __name__ == "__main__":

    def extract_functions_as_dict(filename):
        ret = dict()

        nodes = extract_functions(filename)  # 调用 clang

        # yielding
        for node in nodes:
            # 函数名
            name = node.spelling
            start, end = node.extent.start, node.extent.end

            # 返回值类型
            if node.kind == clang.cindex.CursorKind.CONSTRUCTOR:
                return_type = (
                    "Constructor"  # 构造函数没有返回值类型，标记为"Constructor"
                )
            elif node.kind == clang.cindex.CursorKind.DESTRUCTOR:
                return_type = "Destructor"  # 析构函数没有返回值类型，标记为"Destructor"
            else:
                return_type = node.result_type.spelling

            # 参数类型
            params = []
            for arg in node.get_arguments():
                param_type = arg.type.spelling
                params.append(param_type)
            params_str = ", ".join(params)

            # TODO: make a list of unique signiture
            key = str(f"{return_type}:{name}:{params_str}")
            # print(f"{key} at {start.line}~{end.line}")

            # NOTE: 按格式制作字典
            ret[key] = (start.line, end.line)

        return ret

    # TODO: go though all files
    with open("./diff.txt", "r") as file:
        lines = file.readlines()  # 全部含有差异的文件

    # 每行对应一个文件
    def func():
        for line in lines:
            line = line.strip()
            # line = "/llvm/lib/Target/AMDGPU/AMDGPULegalizerInfo.cpp"  # test-only
            print("processing:", line)

            file1, file2 = (
                "llvm-project" + line,
                "llvm-project-cd9a641613eddf25d4b25eaa96b2c393d401d42c" + line,
            )

            # 全函数，对应行号
            dict1 = extract_functions_as_dict(file1)
            # print(dict1)
            dict2 = extract_functions_as_dict(file2)

            common = sorted(set(dict1.keys()) & set(dict2.keys()))
            # print(type(common))
            # left = set(dict1.keys()) - set(dict2.keys())
            # print(left)
            # 而是只关注新增的函数，被修改的函数
            right = set(dict2.keys()) - set(dict1.keys())

            # TODO: 记录新增的函数的 id
            for key in right:
                # print(key)

                pass

            functions = []  # 全部差异函数的签名
            for key in common:
                # 每个 key 代表该文件中的一个函数名，标签对应行号，取函数体，转换为去除注释后的单行字符串

                def get_function_as_string(file_, dict_):
                    with open(file_, "r") as file_content:  # 去看原来的文件
                        lines = file_content.readlines()
                        start, end = dict_[key]
                        code = "".join(lines[start - 1 : end])

                        def remove_comments():
                            code_no_single_line_comments = re.sub(r"//.*", "", code)
                            code_no_comments = re.sub(
                                r"/\*.*?\*/",
                                "",
                                code_no_single_line_comments,
                                flags=re.DOTALL,
                            )
                            code_minimal_block = re.sub(
                                r"\s+", " ", code_no_comments
                            ).strip()  # 多个空字符只保留一个

                            return code_minimal_block

                        return remove_comments()
                        return code

                s1 = get_function_as_string(file1, dict1)
                # print(s1)
                s2 = get_function_as_string(file2, dict2)
                if s1 != s2:
                    # 发现差异函数，追加至 json
                    functions.append(key)

            # TODO: json 写入文件
            data = {"filename": line, "functions": functions}
            # print(data)
            if functions:
                yield data

    with open("diff.json", "w", encoding="utf-8") as json_file:
        json_file.write("{\n")
        json_file.write('"data": [\n')

        first = True  # 用于判断是否是第一个对象

        try:
            for obj in func():
                if not first:
                    json_file.write(",\n")  # 不是第一个对象则添加逗号换行

                json.dump(obj, json_file, ensure_ascii=False, indent=4)
                first = False
        except StopIteration:
            pass

        json_file.write("\n")
        json_file.write("]\n")
        json_file.write("}\n")
