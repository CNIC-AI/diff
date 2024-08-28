import json


from abc import ABC, abstractmethod
from collections import defaultdict


FILE_PATH = "./functions.json"


class Policy(ABC):
    def __init__(self) -> None:
        super().__init__()

        self.data = []

    @abstractmethod
    def check(self, item):
        pass

    def post_processing(self):
        self._logger()

        self._print()
        print("---")

    def _logger(self):
        """格式化输出"""

        with open(f"{self.__class__.__name__}.json", "w") as file:
            json.dump(self.data, file, indent=4)

    @abstractmethod
    def _print(self):
        pass


class Count(Policy):
    def __init__(self) -> None:
        super().__init__()

        self.num_files = 0
        self.num_new_functions = 0
        self.num_functions = 0

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

    def _print(self):
        print(f"files: {self.num_files}")
        print(f"new functions: {self.num_new_functions}")
        print(f"functions: {self.num_functions}")


class Find(Policy):
    def __init__(self) -> None:
        super().__init__()

        self.num_functions = 0
        self.substr = []  # pattern

    def check(self, item):
        data = defaultdict(list)

        def match(main):
            return any([s in main for s in [s.lower() for s in self.substr]])

        for s in item["new_functions"] + item["functions"]:
            if match(s.lower()):
                data["functions"].append(s)

        if data or match(item["filename"].lower()):
            self.num_functions += len(data["functions"])

            self.data.append({"filename": item["filename"], **data})

    def _print(self):
        print(f"{self.__class__.__name__} functions: {self.num_functions}")


class FindAMD(Find):
    def __init__(self) -> None:
        super().__init__()

        self.substr.append("AMD")

    def _logger(self):
        """Find相关后处理使用MarkDown"""

        with open(f"{self.__class__.__name__}.md", "w") as file:
            cnt = 0
            file.write(f"# {self.__class__.__name__}\n\n")

            for item in self.data:
                file.write(f"## {item['filename']}\n\n")

                for s in item["functions"]:
                    cnt += 1

                    # FIXME: 制作函数相关标题
                    parts = s.split("|")
                    parts[1] = "" if parts[1] == "None" else parts[1] + "::"

                    file.write(f"### {cnt}: {parts[1]}{parts[2]}\n\n")
                    file.write(f"- 解释：\n\n")


class FindCodeGen(FindAMD):
    """_summary_

    Args:
        FindAMD (_type_): _description_
    """

    def __init__(self) -> None:
        super().__init__()

        del self.substr[:]  # 注释本行则选择 AMD + CODEGEN 相关全部函数
        self.substr.append("CODEGEN")


if __name__ == "__main__":
    with open(FILE_PATH, "r") as file:
        data = json.load(file)

    policy_lst = [Count(), FindAMD(), FindCodeGen()]

    # 针对每个json块，应用多种检查策略，每个策略将会不断记录信息
    for item in data:
        for policy in policy_lst:
            policy.check(item)

    # 统一调用“后处理行为”，将每个策略记录到的信息写入日志
    for policy in policy_lst:
        policy.post_processing()
