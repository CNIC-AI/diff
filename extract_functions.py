import clang.cindex


def extract_functions(filename):
    """All functions (with body) in a file!

    Args:
        filename (_type_): _description_
    """

    index = clang.cindex.Index.create()
    translation_unit = index.parse(filename, args=["-x", "c++", "-std=c++17"])

    def get(node, class_name=None):
        """_summary_

        Args:
            node (_type_): _description_
            class_name (_type_, optional): _description_. Defaults to None.
        """

        file = node.location.file
        if file and file.name != filename:
            # print(file)

            return

        # if (
        #     node.kind == clang.cindex.CursorKind.CXX_METHOD
        #     or node.kind == clang.cindex.CursorKind.FUNCTION_DECL
        # ):
        #     if node.is_definition():
        #         yield node
        # elif node.kind == clang.cindex.CursorKind.FUNCTION_TEMPLATE:
        #     # 认为模板函数声明、定义不能分离
        #     assert node.is_definition()
        #     yield node

        function_kinds = [
            clang.cindex.CursorKind.CXX_METHOD,  # 类的成员函数
            clang.cindex.CursorKind.FUNCTION_DECL,  # 全局或非成员函数
            clang.cindex.CursorKind.CONSTRUCTOR,  # 构造函数
            clang.cindex.CursorKind.DESTRUCTOR,  # 析构函数
            clang.cindex.CursorKind.FUNCTION_TEMPLATE,  # 函数模板
            clang.cindex.CursorKind.CONVERSION_FUNCTION,  # 转换函数
        ]

        if node.kind in function_kinds and node.is_definition():
            yield node

        for child in node.get_children():
            yield from get(child, class_name)

    return get(translation_unit.cursor)
