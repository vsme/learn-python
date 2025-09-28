# 纯函数
# 纯函数没有副作用，副作用是指函数除了返回值之外，还对外部环境产生了影响。
def square(x):
    return x * x


# map / filter / reduce（functools.reduce 需导入）
from functools import reduce

nums = [1, 2, 3, 4]
squares = list(map(square, nums))  # [1, 4, 9, 16]
evens = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]
total = reduce(lambda a, b: a + b, nums)  # 10

# 列表/字典推导（更 Pythonic——符合 Python 风格的 的 map/filter）
squares2 = [x * x for x in nums]
evens2 = [x for x in nums if x % 2 == 0]

# 偏函数 / 组合
from functools import partial
import operator

add10 = partial(operator.add, 10)  # add10(x) == 10 + x

# 不可变类型
point = (3, 4)  # tuple 不可变
tags = frozenset({"a", "b"})


# 高阶函数
def process_numbers(numbers, filter_func, map_func):
    """
    处理数字列表
    :param numbers: 数字列表
    :param filter_func: 过滤函数
    :param map_func: 映射函数
    :return: 处理后的列表
    """
    # 先过滤，再映射
    filtered = [n for n in numbers if filter_func(n)]  # 使用过滤函数
    result = [map_func(n) for n in filtered]  # 使用映射函数
    return result


# 定义过滤和映射函数
def is_even(n):  # 判断是否为偶数
    return n % 2 == 0


def double(n):  # 将数字翻倍
    return n * 2


# 使用高阶函数处理数据
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = process_numbers(numbers, is_even, double)
print(f"处理结果: {result}")  # 输出: [4, 8, 12, 16, 20]


# 应用函数式编程
def create_counter():
    """
    创建一个计数器函数
    :return: 计数器函数
    """
    count = 0  # 计数器初始值

    def counter():  # 内部函数
        # nonlocal 关键字用于声明使用外部变量
        nonlocal count  # 声明使用外部变量
        count += 1  # 计数器加1
        return count  # 返回当前计数

    return counter  # 返回计数器函数


# 测试代码
counter1 = create_counter()  # 创建第一个计数器
counter2 = create_counter()  # 创建第二个计数器

print("第一个计数器：")
print(counter1())  # 输出: 1
print(counter1())  # 输出: 2
print(counter1())  # 输出: 3

print("\n第二个计数器：")
print(counter2())  # 输出: 1
print(counter2())  # 输出: 2


# 闭包 返回函数
def count(n):
    fs = []
    for i in range(1, 4):
        fs.append(lambda i=i: i * i)
    return fs


fs = count(3)
print(fs)
print(fs[0]())
print(fs[1]())
print(fs[2]())
