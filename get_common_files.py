import os


from arguments import parse_args

script_name = os.path.splitext(os.path.basename(__file__))[0]


def get_files(prefix, suffix=(".h", ".hpp", ".cc", ".cpp")):
    """_summary_

    Args:
        prefix (_type_): directory path
        suffix (tuple, optional): _description_. Defaults to (".h", ".hpp", ".cc", ".cpp").
    """

    def cond():
        return file.endswith(suffix)

    files = []

    for root, _, raw_files in os.walk(prefix):
        for file in raw_files:
            if cond():
                files.append(os.path.join(root, file))

    return [s[len(prefix) :] for s in files]


if __name__ == "__main__":
    args = parse_args()

    files_1, files_2 = get_files(args.dir_1), get_files(args.dir_2)

    # NOTE: 只关注新增的文件
    with open(f"logs/{script_name}_right_only.txt", "w") as file:
        for line in sorted(set(files_2) - set(files_1)):
            file.write(line + "\n")
    print("done!")

    # 获取公共文件
    with open(f"logs/{script_name}_common.txt", "w") as file:
        for line in sorted(set(files_1) & set(files_2)):
            file.write(line + "\n")
    print("done!")
