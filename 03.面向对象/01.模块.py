import mymath
import sys
import os

print(mymath.area(2))

# 须在根目录使用 `PYTHONPATH=$(pwd) python 03.面向对象/01.模块.py` 才能导入 utils 包
# from utils.xyz import world
# print(world())

# 或者 添加项目根目录到Python路径
# os.path.abspath(__file__) - 获取当前文件的绝对路径
# os.path.dirname() - 两次调用获取项目根目录路径
# sys.path.append() - 将根目录添加到Python模块搜索路径中
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.abc import hello

print(hello())

# 查看 chapter03 目录下的文件
