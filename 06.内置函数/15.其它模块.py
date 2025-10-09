import copy

# 定义一个嵌套列表
lst1 = [1, 2, [3, 4]]

# 浅拷贝：只复制最外层，内部嵌套对象还是同一个
lst2 = copy.copy(lst1)
lst2[2][0] = 99
print("浅拷贝后lst1：", lst1)  # [1, 2, [99, 4]]

# 深拷贝：递归复制所有层级，完全独立
lst3 = copy.deepcopy(lst1)
lst3[2][0] = 100
print("深拷贝后lst1：", lst1)  # [1, 2, [99, 4]]
print("深拷贝后lst3：", lst3)  # [1, 2, [100, 4]]


from enum import Enum


# 定义一个星期的枚举类型
class Weekday(Enum):
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7


# 使用枚举
today = Weekday.MON
print("今天是：", today)
print("今天的值：", today.value)
print("今天的名字：", today.name)

import uuid

# 生成一个随机的UUID（版本4）
unique_id = uuid.uuid4()
print("随机UUID：", unique_id)

# 生成基于名字的UUID（版本5）
name_id = uuid.uuid5(uuid.NAMESPACE_DNS, "python.org")
print("基于名字的UUID：", name_id)

import base64

# 原始字符串
text = "hello world"
# 编码为字节
text_bytes = text.encode("utf-8")
# Base64编码
encoded = base64.b64encode(text_bytes)
print("Base64编码：", encoded)

# Base64解码
decoded = base64.b64decode(encoded)
print("解码后字符串：", decoded.decode("utf-8"))

# 读取文件并编码为Base64
with open("README.md", "rb") as f:
    img_data = f.read()
    encoded = base64.b64encode(img_data)
    print("Base64编码前10字节：", encoded[:10])

# 解码Base64并写入新文件
with open("README.md", "wb") as f:
    f.write(base64.b64decode(encoded))

import struct

# 打包：把整数12345和浮点数3.14编码为二进制
packed = struct.pack("if", 12345, 3.14)
print("打包后的二进制数据：", packed)

# 解包：从二进制数据还原为原始数据
unpacked = struct.unpack("if", packed)
print("解包后的数据：", unpacked)

# 从typing模块导入List, Optional, Tuple类型提示
from typing import List, Optional, Tuple


# 定义一个加法函数，参数x和y都是整数类型，返回值也是整数类型
def add(x: int, y: int) -> int:
    # 返回两个数的和
    return x + y


# 定义一个问候函数，参数names是字符串列表，无返回值
def greet(names: List[str]) -> None:
    # 遍历名字列表中的每个名字
    for name in names:
        # 打印问候语和当前名字
        print("你好,", name)


# 使用类型提示
# 调用add函数计算2+3的结果
result = add(2, 3)
# 调用greet函数问候小明和小红
greet(["小明", "小红"])


# 定义一个查找用户的函数，参数是用户ID（整数类型），返回值是可选的元组（包含姓名和年龄）
# Optional[Tuple[str, int]] 表示返回值可以是一个元组，也可以是None。
def find_user(user_id: int) -> Optional[Tuple[str, int]]:
    # 假设查找不到返回None
    # 如果用户ID等于1，返回用户信息
    if user_id == 1:
        # 返回包含姓名和年龄的元组
        return ("小明", 18)
    # 如果用户ID不等于1，返回None表示未找到
    else:
        return None


# 调用函数查找ID为1的用户并打印结果
print(find_user(1))
# 调用函数查找ID为2的用户并打印结果
print(find_user(2))
