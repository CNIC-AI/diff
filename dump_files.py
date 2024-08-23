import os


dir1 = "llvm-project"
dir2 = "llvm-project-cd9a641613eddf25d4b25eaa96b2c393d401d42c"


def dump_files(directory, suffix=(".h", ".hpp", ".cc", ".cpp")):
    """_summary_

    Args:
        directory (_type_): _description_

    Returns:
        _type_: _description_
    """

    files = []

    for root, _, raw_files in os.walk(directory):
        for file in raw_files:
            if file.endswith(suffix):
                files.append(os.path.join(root, file))

    return [s[len(directory) :] for s in files]


if __name__ == "__main__":
    files1 = dump_files(dir1)
    # for file in files1:
    #     print(file)
    files2 = dump_files(dir2)

    common_elements = sorted(list(set(files1) & set(files2)))
    # print(common_elements)
    unique_in_list1 = sorted(list(set(files1) - set(files2)))
    unique_in_list2 = sorted(list(set(files2) - set(files1)))

    # dump
    with open("common.txt", "a") as file:
        for line in common_elements:
            file.write(line + "\n")

    with open("left.txt", "a") as file:
        for line in unique_in_list1:
            file.write(line + "\n")

    with open("right.txt", "a") as file:
        for line in unique_in_list2:
            file.write(line + "\n")
