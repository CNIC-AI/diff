import re
import json


from shared_vars import *


def get_headers(abspath):
    pattern = re.compile(r'#\s*include\s*[<"](.*?)[">]')

    headers = []
    with open(abspath, "r", encoding="utf-8") as file:
        for line in file:
            match = pattern.search(line)

            if match:
                headers.append(match.group(1))

    return headers


def get_include_directories(abspath):
    with open(PATH_TO_COMMON_FILES, "r") as file:
        data = json.load(file)

    path = set()
    for s1 in get_headers(abspath):
        for s2 in data:
            if s2.endswith(s1):
                path.add(s2[: -len(s1)])

    return sorted(path)
