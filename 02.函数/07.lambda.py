# 用lambda表达式实现两个数相加
add = lambda x, y: x + y  # 定义一个匿名函数，接收x和y，返回它们的和
print(add(3, 5))  # 输出: 8

# 作为回调 / key 函数
nums = [3, -10, -2, 5]
print(sorted(nums, key=lambda x: abs(x)))     # [-2, 3, 5, -10]

# map / filter 的轻量函数
print(list(map(lambda x: x*x, [1,2,3])))      # [1, 4, 9]
print(list(filter(lambda s: s.isalpha(), ["a", "3", "bc"])))  # ['a', 'bc']

# 条件表达式
f = lambda x: "even" if x % 2 == 0 else "odd"
print(f(3))  # 'odd'
print(f(4))  # 'even'

lam = lambda s: (n := len(s)) * (n > 3)   # 长度>3则返回长度，否则返回0
sizes = list(map(lam, ["a", "bb", "ccc", "dddd"]))
print(sizes)

# 默认参数
num = 5  # 定义一个变量num，赋值为5
func = lambda i=num: i * i  # 定义一个lambda函数，参数i默认值为5，函数返回i的平方
print(func())  # 调用func函数并打印结果，由于没有传参，使用默认值5，结果为25
print(func(3))  # 调用func函数并打印结果，传参为3，结果为9