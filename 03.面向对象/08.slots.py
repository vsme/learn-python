# 定义一个学生类，使用__slots__限制属性
class Student:
    __slots__ = ("name", "age")  # 只允许实例绑定name和age属性

    def __init__(self, name, age):
        self.name = name  # 初始化name属性
        self.age = age  # 初始化age属性


# 创建学生对象
student = Student("小明", 20)  # 创建学生对象
print(student.name)  # 输出: 小明
print(student.age)  # 输出: 20
# student.score = 90  # 错误，AttributeError: 'Student' object has no attribute 'score' and no __dict__ for setting new attributes


# 定义一个学生类，不使用__slots__
class Student:
    __slots__ = "name"


# 创建学生对象
student = Student()  # 创建学生对象
student.name = "小明"  # 动态绑定name属性
print(student.name)  # 输出: 小明
# print(student.age)
# AttributeError: 'Student' object has no attribute 'age' and no __dict__ for setting new attributes


# 定义一个学生类，不使用__slots__
class Student:
    __slots__ = ("name", "age")
    pass


# 定义一个函数作为实例方法
def set_age(self, age):
    self.age = age  # 设置age属性


# 创建学生对象
student = Student()  # 创建学生对象

# types模块提供了Python内置类型的访问方式
# MethodType用于创建绑定方法对象，将函数绑定到实例上
# 这里会报错：AttributeError: 'Student' object has no attribute 'set_age' and no __dict__ for setting new attributes
# 原因是我们使用了__slots__限制了属性，且没有包含'set_age'
# 使用MethodType将set_age函数绑定到student实例
# student.set_age = MethodType(set_age, student) # AttributeError: 'Student' object has no attribute 'age'
# student.set_age(20)  # 调用set_age方法
# print(student.age)
