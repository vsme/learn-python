# 求绝对值
print(abs(-10))  # 输出：10

# 求最大值
print(max(3, 7, 2, 5))  # 输出：7

# 类型转换
print(int("123"))  # 字符串转整数，输出：123
print(float("3.14"))  # 字符串转浮点数，输出：3.14
print(str(456))  # 数字转字符串，输出：'456'
print(bool(0))  # 0转为布尔值，输出：False
print(bool("hi"))  # 非空字符串转为布尔值，输出：True

# abs函数只能传一个参数
# print(abs(1, 2))  # TypeError: abs() takes exactly one argument (2 given)

# abs函数不能传字符串
# print(abs("abc")) # TypeError: bad operand type for abs(): 'str'

# 给abs函数起个新名字
my_abs = abs
print(my_abs(-20))  # 输出：20


# 自定义函数
def area(r: float) -> float:
    """计算圆面积。r 为半径（米）。"""  # 函数文档
    from math import pi

    return pi * r * r  # 用return返回结果


print(area.__doc__)  # -> 计算圆面积。r 为半径（米）。
help(area)  # 会显示这段说明

# 调用自定义函数
print(area(5))  # 输出：78.539815
print(area(10))  # 输出：314.15926

# 把整数转换为十六进制字符串
n1 = 255
n2 = 1000

print(hex(n1))  # 输出：0xff
print(hex(n2))  # 输出：0x3e8
