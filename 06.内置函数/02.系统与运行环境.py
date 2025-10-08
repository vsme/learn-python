import sys  # 导入sys模块

# sys.argv是一个列表，包含了命令行参数
print("所有命令行参数：", sys.argv)  # 第一个参数是脚本名

# 获取第一个参数（脚本名）
print("脚本名：", sys.argv[0])

# 如果有额外参数，可以这样获取
if len(sys.argv) > 1:
    print("第一个用户输入的参数：", sys.argv[1])
else:
    print("没有输入额外参数")

# python 脚本名 参数1 参数2
# python 02.系统与运行环境.py hello
# 所有命令行参数： ['02.系统与运行环境.py', 'hello']
# 脚本名： 02.系统与运行环境.py
# 第一个用户输入的参数： hello

# sys模块可以获取和设置Python解释器的路径

# 获取Python解释器路径
print("Python解释器路径：", sys.executable)

# 设置Python解释器路径
sys.executable = "C:/Python311/python.exe"

import platform  # 导入platform模块

# 获取操作系统名称
print("操作系统名称：", platform.system())  # 如 Windows、Linux、Darwin（macOS）

# 获取操作系统详细版本
print("操作系统详细版本：", platform.version())

# 获取完整平台信息
print("完整平台信息：", platform.platform())
# 操作系统名称： Darwin
# 操作系统详细版本： Darwin Kernel Version 25.0.0: Wed Sep 17 21:41:45 PDT 2025; root:xnu-12377.1.9~141/RELEASE_ARM64_T6000
# 完整平台信息： macOS-26.0.1-arm64-arm-64bit

# 获取Python版本
print("Python版本：", platform.python_version())
# Python版本： 3.11.11


print("程序即将退出")
sys.exit(0)  # 0表示正常退出，非0表示异常退出
print("这行不会被执行")  # 这行不会输出，因为上面已经退出
