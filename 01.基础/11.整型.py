# 其他类型转整型
print("类型转换:")
print(f"int(3.14) = {int(3.14)}")  # 浮点数转整型 (截断小数)
print(f"int(-2.99) = {int(-2.99)}")  # -2
print(f"int('100') = {int('100')}")  # 字符串转整型
print(f"int('1010', 2) = {int('1010', 2)}")  # 二进制字符串转十进制
print(f"int('FF', 16) = {int('FF', 16)}")  # 十六进制字符串转十进制
print(f"int(True) = {int(True)}")  # 布尔值转整型 (True=1)
print(f"int(False) = {int(False)}")  # 布尔值转整型 (False=0)

# 进制转换函数
number = 10
print(f"\n数字 {number} 的不同进制表示:")
print(f"二进制: {bin(number)}")  # 0b1010
print(f"八进制: {oct(number)}")  # 0o12
print(f"十六进制: {hex(number)}")  # 0xa


import sys

"""显示整型的内存占用"""
numbers = [0, 1, 10, 100, 1000, 10**10, 10**100]

print("整型内存占用:")
for num in numbers:
    size = sys.getsizeof(num)
    print(f"数字 {num}: {size} 字节")


# 定义一个函数，使用异或运算交换两个数的值
# 异或运算：相同为0，不同为1
def swap(a, b):
    # 第一步：a变为a^b
    a = a ^ b
    # 第二步：b变为a^b^b，即a
    b = a ^ b
    # 第三步：a变为a^b^a，即b
    a = a ^ b
    # 返回交换后的a和b
    return a, b


# 初始化x和y的值
x, y = 5, 3
# 调用swap函数交换x和y
x, y = swap(x, y)
# 打印交换后的x和y
print(f"交换后: x={x}, y={y}")

print(r"\.交换后: x={x}, y={y}")

print(True + True)

# 复数0
print(bool(0j))
