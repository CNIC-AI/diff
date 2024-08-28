import json


from abc import ABC, abstractmethod
from collections import defaultdict


FILE_PATH = "/public/home/wangjh/workspace/jax/diff/logs/20240827221826/functions.json"


class Policy(ABC):
    @abstractmethod
    def check(self, item):
        pass

    def post_processing(self):
        self._post_processing()
        print("---")

    @abstractmethod
    def _post_processing(self):
        pass


class Count(Policy):
    def __init__(self) -> None:
        super().__init__()

        self.num_files = 0
        self.num_new_functions = 0
        self.num_functions = 0

        self.data = []

    def check(self, item):
        self.num_new_functions += len(item["new_functions"])
        self.num_functions += len(item["functions"])

        if len(item["new_functions"]) + len(item["functions"]) > 0:
            self.num_files += 1  # 该文件涉及函数变化

            if len(item["new_functions"]) > 0:
                self.data.append(
                    {
                        "filename": item["filename"],
                        "new_functions": item["new_functions"],
                    }
                )

    def _post_processing(self):
        print(f"files: {self.num_files}")
        print(f"new functions: {self.num_new_functions}")
        print(f"functions: {self.num_functions}")

        # TODO: 写文件
        with open("./count.json", "w") as file:
            json.dump(self.data, file, indent=4)


class FindAMD(Policy):
    def __init__(self) -> None:
        super().__init__()

        self.num_functions = 0
        self.data = []

    def check(self, item):
        substr = [
            s.lower()
            for s in [
                "AMD",
                "CODEGEN",
            ]
        ]

        data = defaultdict(list)

        def exist_substr(sub, main):
            return any([s in main for s in sub])

        for s in item["new_functions"] + item["functions"]:
            if exist_substr(substr, s.lower()):
                data["functions"].append(s)

        if data or exist_substr(substr, item["filename"].lower()):
            self.num_functions += len(data["functions"])

            self.data.append({"filename": item["filename"], **data})

    def _post_processing(self):
        print(f"AMD-related functions: {self.num_functions}")

        with open("./find_AMD.json", "w") as file:
            json.dump(self.data, file, indent=4)


if __name__ == "__main__":
    with open(FILE_PATH, "r") as file:
        data = json.load(file)

    policy_lst = [Count(), FindAMD()]

    for item in data:
        for policy in policy_lst:
            policy.check(item)

    for policy in policy_lst:
        policy.post_processing()
