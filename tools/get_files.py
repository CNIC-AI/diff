import sys
import os


language_suffix = (
    # ".c",
    ".cc",
    ".cpp",
    ".h",
    # ".hh",
    ".hpp",
    # ".inl",
    # ".py",
)


def get_files(directory, suffix=language_suffix):
    """_summary_

    Args:
        directory (_type_): _description_
        suffix (_type_, optional): _description_. Defaults to language_suffix.

    Returns:
        _type_: _description_
    """

    files = []

    for root, _, raw_files in os.walk(directory):
        for file in raw_files:
            if file.endswith(suffix):
                files.append(os.path.join(root, file))

    # return files
    return [s[len(directory) :] for s in files]


if __name__ == "__main__":
    files = get_files("../")

    for file in files:
        print(file)
