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
    for file in files1:
        print(file)
