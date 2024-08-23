import json


if __name__ == "__main__":
    with open("./logs/diff.json", "r", encoding="utf-8") as file:
        data = json.load(file)["data"]

    # 统计新增函数个数、修改函数个数
    num_new_functions = num_functions = 0

    for item in data:
        num_new_functions += len(item["new_functions"])
        num_functions += len(item["functions"])

    print("num new functions:", num_new_functions)
    print("num functions:", num_functions)
