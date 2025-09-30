import os  # 导入os模块

# os.name 属性可以告诉我们当前操作系统的类型
if os.name == "nt":
    print("当前系统是 Windows")
elif os.name == "posix":
    print("当前系统是 Linux/Unix 或 macOS")
else:
    print("未知操作系统")


# os.uname() 只在 Linux/Unix/macOS 下可用，Windows 下会报错
if hasattr(os, "uname"):
    info = os.uname()  # 获取系统详细信息
    print("系统名称：", info.sysname)
    print("主机名：", info.nodename)
    print("系统版本：", info.version)
else:
    print("当前系统不支持 os.uname()")


# os.environ 是一个包含所有环境变量的字典
print("所有环境变量：", os.environ)

# 获取PATH环境变量的值
path_value = os.environ.get("PATH")
print("PATH环境变量：", path_value)

# 获取一个不存在的环境变量，如果没有则返回默认值
my_var = os.environ.get("MY_VAR", "未设置")
print("MY_VAR环境变量：", my_var)


# os.path.abspath('.') 获取当前目录的绝对路径
current_dir = os.path.abspath(".")
print("当前目录的绝对路径：", current_dir)


# os.path.join() 用于拼接路径，自动适配不同系统的分隔符
current_dir = os.path.abspath(".")
new_folder = os.path.join(current_dir, "my_folder")
print("新目录的完整路径：", new_folder)


# 创建新目录
new_folder = "my_folder"
if not os.path.exists(new_folder):  # 先判断目录是否已存在
    os.mkdir(new_folder)  # 创建目录
    print("目录已创建：", new_folder)

# 删除目录
os.rmdir(new_folder)  # 删除目录（目录必须为空）
print("目录已删除：", new_folder)

# 获取当前目录的绝对路径
current_dir = os.path.abspath(".")

# 使用 os.path.join() 拼接路径
file_path = os.path.join(current_dir, "example.txt")

# 使用 os.path.split() 拆分路径
dir_name, file_name = os.path.split(file_path)
print("目录部分：", dir_name)
print("文件名部分：", file_name)

# 获取当前目录的绝对路径
current_dir = os.path.abspath(".")

# 使用 os.path.join() 拼接路径
file_path = os.path.join(current_dir, "example.txt")

# os.path.splitext() 返回(主文件名, 扩展名)
main_name, ext = os.path.splitext(file_path)
print("主文件名：", main_name)
print("扩展名：", ext)


# 假设当前目录下有 test.txt 文件
old_name = "test.txt"
new_name = "test_renamed.txt"

# 重命名文件
if os.path.exists(old_name):
    os.rename(old_name, new_name)  # 重命名文件
    print(f"{old_name} 已重命名为 {new_name}")

# 删除文件
if os.path.exists(new_name):
    os.remove(new_name)  # 删除文件
    print(f"{new_name} 已被删除")

# os.listdir('.') 列出当前目录下的所有文件和文件夹
# os.path.isdir(name) 判断name是否是目录
# 1. os.listdir('.') 获取当前目录下的所有文件和文件夹名称，返回一个列表
# 2. 对列表中的每个name进行遍历
# 3. os.path.isdir(name) 检查name是否为目录（文件夹）
# 4. 只有当name是目录时，才将其包含在最终的列表中
# 5. 使用列表推导式简洁地完成筛选操作
dirs = [name for name in os.listdir(".") if os.path.isdir(name)]
print("所有子目录：", dirs)

# 列出所有以 .py 结尾的文件
# 1. os.listdir('.') 获取当前目录下的所有文件和文件夹名称，返回一个列表
# 2. 对列表中的每个name进行遍历
# 3. os.path.isfile(name) 检查name是否为文件
# 4. os.path.splitext(name)[1] == '.py' 检查文件扩展名是否为 .py
# 5. 只有当name是文件且扩展名是.py时，才将其包含在最终的列表中
# 6. 使用列表推导式简洁地完成筛选操作
py_files = [
    name
    for name in os.listdir(".")
    if os.path.isfile(name) and os.path.splitext(name)[1] == ".py"
]
print("所有 Python 文件：", py_files)
