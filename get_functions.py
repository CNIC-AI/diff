import clang.cindex


def get_functions(filename):
    """Get all C/C++ functions within a file.

    “试图将每一个函数的信息组合成一个 json 串！”

    Args:
        filename (_type_): _description_
    """

    index = clang.cindex.Index.create()
    translation_unit = index.parse(filename, args=["-x", "c++", "-std=c++17"])

    def get_clang_nodes(node):

        if node.location.file and node.location.file.name != filename:
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
        "return_type": return_type,
        "params": params,
        "positions": (node.extent.start.line, node.extent.end.line),
    }

    return data


if __name__ == "__main__":
    for node in get_functions("data/example.h"):
        print(node2json(node))
