import math

# 计算平方根
print("16的平方根：", math.sqrt(16))  # 输出4.0

# 计算绝对值
print("绝对值：", math.fabs(-5))  # 输出5.0

# 计算幂（2的3次方）
print("2的3次方：", math.pow(2, 3))  # 输出8.0

# 计算正弦、余弦、正切
print("sin(30°)：", math.sin(math.radians(30)))  # 先将角度转为弧度
print("cos(60°)：", math.cos(math.radians(60)))
print("tan(45°)：", math.tan(math.radians(45)))

# 常用常数
print("圆周率π：", math.pi)
print("自然对数e：", math.e)

# 计算自然对数（以e为底）
print("ln(10)：", math.log(10))  # 默认以e为底

# 计算以10为底的对数
print("log10(100)：", math.log10(100))  # 输出2.0

# 向上取整
print("向上取整3.2：", math.ceil(3.2))  # 输出4

# 向下取整
print("向下取整3.8：", math.floor(3.8))  # 输出3

import random

# 生成1到10之间的随机整数（包含1和10）
print("随机整数：", random.randint(1, 10))

# 生成0到1之间的随机小数
print("随机小数：", random.random())

# 从列表中随机选择一个元素
fruits = ["苹果", "香蕉", "橙子"]
print("随机选择水果：", random.choice(fruits))

# 打乱列表顺序
random.shuffle(fruits)
print("打乱后的水果列表：", fruits)

# 生成2到10之间，步长为2的随机偶数
print("随机偶数：", random.randrange(2, 11, 2))  # 可能输出2、4、6、8、10

from decimal import Decimal, getcontext

# 普通浮点数的加法（可能有精度误差）
print("0.1 + 0.2 =", 0.1 + 0.2)  # 输出0.30000000000000004

# 用Decimal进行高精度加法
a = Decimal("0.1")
b = Decimal("0.2")
print("Decimal高精度加法：", a + b)  # 输出0.3

# 设置全局小数精度为4位
getcontext().prec = 4

# 进行高精度运算
result = Decimal("1.23456") / Decimal("3")
print("保留4位有效数字的结果：", result)

from fractions import Fraction

# 创建分数1/3
f1 = Fraction(1, 3)
print("分数1/3：", f1)

# 由字符串创建分数
f2 = Fraction("2/5")
print("分数2/5：", f2)

a = Fraction(1, 3)
b = Fraction(1, 6)

# 分数加法
print("1/3 + 1/6 =", a + b)

# 分数乘法
print("1/3 * 1/6 =", a * b)

import statistics

data = [1, 2, 2, 3, 4, 5, 6]

# 计算均值
print("均值：", statistics.mean(data))

# 计算中位数
print("中位数：", statistics.median(data))

# 计算方差
# 方差指数据与均值之间的偏离程度
print("方差：", statistics.variance(data))

# 计算众数（出现次数最多的数）
print("众数：", statistics.mode(data))
