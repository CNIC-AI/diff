import json


with open("diff.json", "r", encoding="utf-8") as file:
    data = json.load(file)


if __name__ == "__main__":
    data = data["data"]
    print("num files:", len(data))

    cnt = 0
    for item in data:
        cnt += len(item["functions"])
    print("num functions:", cnt)
