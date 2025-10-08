import os

# 获取当前工作目录（即当前Python脚本运行的文件夹）
print("当前工作目录：", os.getcwd())

# 切换到指定目录（如切换到C盘根目录，注意Windows下路径用\\或r'路径'）
os.chdir(r"/Users/yaavi/Documents/projects/learn-python/06.内置函数")
print("切换后的工作目录：", os.getcwd())

# 创建一个新文件夹
os.mkdir("test_folder")  # 在当前目录下创建名为test_folder的文件夹

# 删除文件夹（只能删除空文件夹）
os.rmdir("test_folder")

# 列出当前目录下的所有文件和文件夹
print("当前目录内容：", os.listdir("."))

# 获取操作系统的环境变量（如PATH）
print("系统PATH环境变量：", os.environ.get("PATH"))

# os.path

# 拼接路径（推荐用os.path.join，自动适配操作系统的分隔符）
full_path = os.path.join("folder", "file.txt")
print("拼接后的路径：", full_path)

# 拆分路径，分离文件夹和文件名
folder, filename = os.path.split("folder/file.txt")
print("文件夹部分：", folder)
print("文件名部分：", filename)

# 判断文件是否存在
print("file.txt是否存在：", os.path.exists("file.txt"))

# 判断路径是否为文件
print("file.txt是文件吗：", os.path.isfile("file.txt"))

# 判断路径是否为文件夹
print("folder是文件夹吗：", os.path.isdir("folder"))

# 获取绝对路径
print("file.txt的绝对路径：", os.path.abspath("file.txt"))

# 获取文件扩展名
name, ext = os.path.splitext("file.txt")
print("文件名：", name)
print("扩展名：", ext)

import shutil

# 复制文件（把a.txt复制为b.txt）
shutil.copy("a.txt", "b.txt")

# 复制整个文件夹（把src_folder复制为dst_folder）
# shutil.copytree("src_folder", "dst_folder")

# 移动文件或文件夹（也可以用来重命名）
shutil.move("b.txt", "new_b.txt")  # 把b.txt移动或重命名为new_b.txt

# 删除文件
os.remove("new_b.txt")

# 删除整个文件夹及其内容
# shutil.rmtree("dst_folder")

import glob

# 查找当前目录下所有txt文件
txt_files = glob.glob("*.txt")
print("所有txt文件：", txt_files)

# 查找所有子文件夹下的txt文件（递归查找）
all_txt_files = glob.glob("**/*.txt", recursive=True)
print("所有子文件夹下的txt文件：", all_txt_files)

import tempfile

# 创建一个临时文件，返回文件对象
with tempfile.TemporaryFile(mode="w+t") as f:
    f.write("这是临时文件内容")
    f.seek(0)  # 回到文件开头
    print("临时文件内容：", f.read())
# 文件会在with语句结束后自动删除

# 创建一个临时目录
with tempfile.TemporaryDirectory() as tmpdirname:
    print("临时目录路径：", tmpdirname)
    # 可以在临时目录下创建文件
    filepath = os.path.join(tmpdirname, "temp.txt")
    with open(filepath, "w") as f:
        f.write("写入临时文件")
    # 读取刚才写入的内容
    with open(filepath, "r") as f:
        print("读取临时文件内容：", f.read())
# 临时目录和里面的内容会自动删除

import fnmatch

# 判断文件名是否以.txt结尾
print(fnmatch.fnmatch("report.txt", "*.txt"))  # 输出True

# 判断文件名是否以data_加两位数字结尾
print(fnmatch.fnmatch("data_01.csv", "data_??.csv"))  # 输出True
print(fnmatch.fnmatch("data_1.csv", "data_??.csv"))  # 输出False
