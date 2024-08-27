import clang.cindex


from .get_include_directories import *


class Book:
    """ """

    def __init__(self, abspath):
        self.abspath = abspath
        self.functions = {}

    def get_string(self, key):
        with open(self.abspath, "r") as file:
            start, end = self.functions[key]

            def remove_comments():
                """规范化函数字节

                Returns:
                    _type_: _description_
                """

                code_no_single_line_comments = re.sub(
                    r"//.*", "", "".join(file.readlines()[start - 1 : end])
                )
                code_no_comments = re.sub(
                    r"/\*.*?\*/", "", code_no_single_line_comments, flags=re.DOTALL
                )

                # 削减多余空字符（只保留一个）
                code_precise = re.sub(r"\s+", " ", code_no_comments).strip()
                return code_precise

            return remove_comments()


def get_book(func):
    """请谨慎选择 key

    Args:
        func (_type_): _description_
    """

    def wrapper(*args, **kwargs):
        result = Book(args[0] + args[1])

        for node in func(*args, **kwargs):
            data = node2json(node)
            sep = "|"

            result.functions[
                str(f"{data['namespace']}{sep}{data['class']}{sep}{data['name']}")
            ] = data["positions"]

        return result

    return wrapper


@get_book
def get_functions(directory, relpath):
    """_summary_

    Args:
        directory (_type_): _description_
        relpath (_type_): _description_

    Returns:
        _type_: _description_

    Yields:
        _type_: clang (function) nodes
    """

    abspath = directory + relpath
    args = [
        "-x",
        "c++",
        "-std=c++17",
    ]

    # 完全考虑头文件（但更耗时）
    args = args + [f"-I{directory}" + x for x in get_include_directories(abspath)]

    index = clang.cindex.Index.create()
    translation_unit = index.parse(abspath, args=args)

    def get_clang_nodes(node):
        """_summary_

        Args:
            node (_type_): _description_

        Returns:
            _type_: _description_

        Yields:
            _type_: _description_
        """

        if node.location.file and node.location.file.name != abspath:
            return

        function_kinds = [
            clang.cindex.CursorKind.FUNCTION_DECL,
            clang.cindex.CursorKind.FUNCTION_TEMPLATE,
            clang.cindex.CursorKind.CONSTRUCTOR,  # 以下是类相关函数
            clang.cindex.CursorKind.DESTRUCTOR,
            clang.cindex.CursorKind.CXX_METHOD,
            clang.cindex.CursorKind.CONVERSION_FUNCTION,  # e.g. operator int() { return 0; }
        ]

        if node.kind in function_kinds and node.is_definition():
            yield node

        for child in node.get_children():
            yield from get_clang_nodes(child)

    return get_clang_nodes(translation_unit.cursor)


def node2json(node):

    def get_enclosing_namespace(node):
        namespaces = []

        while node:
            if node.kind == clang.cindex.CursorKind.NAMESPACE:
                namespaces.append(node.spelling)
            node = node.semantic_parent

        return "::".join(reversed(namespaces)) if namespaces else None

    def get_enclosing_class(node):
        while node:
            if (
                node.kind == clang.cindex.CursorKind.CLASS_DECL
                or node.kind == clang.cindex.CursorKind.STRUCT_DECL
            ):
                return node.spelling
            node = node.semantic_parent

        return None

    # 返回值类型
    if node.kind == clang.cindex.CursorKind.CONSTRUCTOR:
        return_type = "Constructor"
    elif node.kind == clang.cindex.CursorKind.DESTRUCTOR:
        return_type = "Destructor"
    else:
        return_type = node.result_type.spelling

    # 参数类型（列表）
    params = []
    for arg in node.get_arguments():
        param_type = arg.type.spelling
        params.append(param_type)

    # 创建 json
    data = {
        "namespace": get_enclosing_namespace(node),
        "class": get_enclosing_class(node),
        "name": node.spelling,
        "params": params,
        "return_type": return_type,
        "positions": (node.extent.start.line, node.extent.end.line),
    }

    return data
