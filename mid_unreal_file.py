import ast
import os
import  re


def remove_docstrings(file_path, output_path=None):
    """
    读取 Python 文件，去掉类和函数的 r""" """ 文档字符串，兼容语法错误的代码。

    :param file_path: 输入的 .py 文件路径
    :param output_path: 输出文件路径（可选），如果为空则覆盖原文件
    """
    # 检查文件是否存在
    if not os.path.exists(file_path):
        print(f"错误：文件 {file_path} 不存在")
        return

    # 读取文件内容
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as file:
            source = file.read()
    except Exception as e:
        print(f"读取文件 {file_path} 时出错: {e}")
        return

    if not source.strip():
        print(f"错误：文件 {file_path} 为空")
        return

    # 定义正则表达式，匹配函数和类的 r""" """ 文档字符串
    # 函数模式
    func_pattern = r'(def\s+[a-zA-Z_]\w*\s*\([^)]*\)\s*:\s*\n\s*)r"""[\s\S]*?"""(\s*\n)'
    # 类模式（支持继承语法，例如 class XXX(YYY):）
    class_pattern = r'(class\s+[a-zA-Z_]\w*\s*(?:\([^)]*\))?\s*:\s*\n\s*)r"""[\s\S]*?"""(\s*\n)'

    # 先移除函数的 docstring
    modified_source = re.sub(func_pattern, r'\1\2', source, flags=re.MULTILINE)
    # 再移除类的 docstring
    modified_source = re.sub(class_pattern, r'\1\2', modified_source, flags=re.MULTILINE)

    # 写入文件
    output_file = output_path if output_path else file_path
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(modified_source)
        print(f"已处理文件: {file_path} -> {output_file}")
    except Exception as e:
        print(f"写入文件 {output_file} 时出错: {e}")

# 示例使用
if __name__ == "__main__":
    # 输入文件路径
    input_file = r"V:\A\Work\sp\LetGoArtCheckMid\LetsGo\Intermediate\PythonStub\unreal.py"
    output_file = r"V:\A\Work\sp\LetGoArtCheckMid\LetsGo\Intermediate\PythonStubFile\unreal.py"
    remove_docstrings(input_file ,output_file)
    input_file = r"F:\LetsGoDevelop_ft_tools\LetsGo\Intermediate\PythonStub\unreal.py"
    output_file = r"F:\LetsGoDevelop_ft_tools\LetsGo\Intermediate\PythonStubFile\unreal.py"
    remove_docstrings(input_file ,output_file)
