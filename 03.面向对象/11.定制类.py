class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __len__(self):
        return 2

    def __iter__(self):
        yield from (self.x, self.y)


v1, v2 = Vector(1, 2), Vector(3, 4)
print(v1 + v2)  # Vector(4, 6)  ← 定制了加法
print(len(v1))  # 2              ← 定制了长度
x, y = v1  # 可解包/迭代


# 定义一个学生类
class Student:
    def __init__(self, name, age):
        self.name = name  # 学生的名字
        self.age = age  # 学生的年龄

    def __str__(self):
        return f"学生: {self.name}, 年龄: {self.age}"  # 返回学生信息

    # 此方法在对此实例调用repr()时会被自动调用
    # 此方法的返回值会作为对象的描述信息
    # 此方法的返回值必须是字符串
    def __repr__(self):
        return f'Student(name="{self.name}", age={self.age})'  # 返回开发者信息


# 创建学生对象
student = Student("小明", 18)  # 创建学生对象
print(student)  # 输出: 学生: 小明, 年龄: 18
print(repr(student))  # 输出: Student(name="小明", age=18)


# 定义一个斐波那契数列类
class Fibonacci:
    def __init__(self, max_value):
        self.max_value = max_value  # 最大值
        self.a, self.b = 0, 1  # 初始化两个数

    # 此方法在对此实例调用iter()时会被自动调用
    # 此方法的返回值会作为迭代器
    def __iter__(self):
        return self  # 返回迭代器

    # 此方法在对此实例调用next()时会被自动调用
    def __next__(self):
        # 把a的值赋值给result
        result = self.a
        # 把b的值赋值给a，并把a和b的值相加赋值给b
        self.a = self.b
        self.b = self.a + self.b
        # 如果超过最大值
        if self.a > self.max_value:
            # raise StopIteration()是一种用于停止迭代的机制，当迭代器没有更多元素时抛出此异常。
            # raise 抛出错误
            # 抛出StopIteration错误
            raise StopIteration()  # 停止迭代
        return result  # 返回当前数


# 创建斐波那契数列对象
fib = Fibonacci(100)  # 创建斐波那契数列对象
# 使用iter()函数创建迭代器
iter_fib = iter(fib)
# 使用next()函数获取迭代器的下一个元素
print(next(iter_fib))  # 0
# 使用next()函数获取迭代器的下一个元素
print(next(iter_fib))  # 1
# 使用next()函数获取迭代器的下一个元素
print(next(iter_fib))  # 2
print("for")
# 使用for循环遍历斐波那契数列
for num in fib:
    print(num)
# 输出:
# 4
# 8
# 16
# 32


# 定义一个数字序列类
class NumberSequence:
    # 定义一个列表
    def __init__(self):
        self.numbers = [1, 2, 3, 4, 5]

    # 重写__getitem__方法
    def __getitem__(self, n):
        return self.numbers[n]


# 创建数字序列对象
seq = NumberSequence()  # 创建数字序列对象
print(seq[0])  # 输出: 1
print(seq[1])  # 输出: 1
print(seq[2])  # 输出: 2
print(seq[3])  # 输出: 3
print(seq[4])  # 输出: 5


# 定义一个学生类
class Student:
    def __init__(self, name):
        self.name = name  # 学生的名字

    # 此方法会在访问不存在的属性时被自动调用
    # 它允许我们动态处理属性访问
    def __getattr__(self, attr):
        if attr == "age":  # 如果属性是age
            return 18  # 返回年龄
        # 如果属性不存在 抛出错误
        # raise 抛出错误
        # AttributeError 属性错误
        raise AttributeError(f"学生没有{attr}属性")  # 抛出错误


# 创建学生对象
student = Student("小明")  # 创建学生对象
print(student.name)  # 输出: 小明
print(student.age)  # 输出: 18
# print(student.score)  # 错误: 学生没有score属性


# 定义一个学生类
class Student:
    def __init__(self, name):
        self.name = name  # 学生的名字

    # 此方法会在对象被调用时被自动调用
    def __call__(self):
        print(f"我是{self.name}")  # 打印学生信息


# 创建学生对象
student = Student("小明")  # 创建学生对象
# 调用__call__方法
student()  # 输出: 我是小明
