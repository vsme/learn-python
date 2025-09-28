# utils包的初始化文件
# 现代 Python 中不要求必须有 __init__.py 才算包，但建议保留以便清晰与兼容。
# 这个文件使utils目录成为一个Python包
# 可以在其他模块中导入utils包，如：import utils.abc
print("初始化 my_package")
version = "1.0"

# 控制 from package import * 的行为
__all__ = ["module1"]  # 仅允许导入 module1
