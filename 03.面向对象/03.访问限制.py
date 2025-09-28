# 定义一个学生类，使用私有变量
class Student:
    def __init__(self, name, score):
        self.__name = name  # 私有变量，外部无法直接访问
        self.__score = score  # 私有变量，外部无法直接访问

    def get_name(self):
        return self.__name  # 获取名字的方法

    def get_score(self):
        return self.__score  # 获取分数的方法

    def set_score(self, score):
        if 0 <= score <= 100:  # 检查分数是否有效
            self.__score = score  # 设置分数
        else:
            raise ValueError("分数必须在0到100之间")  # 抛出错误


# 创建学生对象
student = Student("小明", 90)  # 创建学生对象
print(student.get_name())  # 输出: 小明
print(student.get_score())  # 输出: 90

student.set_score(80)  # 设置有效分数
print(student.get_score())  # 输出: 80

print(student._Student__name)  # 输出: 小明

# 尝试设置无效分数
try:
    student.set_score(150)  # 设置无效分数
except ValueError as e:
    print(e)  # 输出: 分数必须在0到100之间


# 定义一个汽车类，使用私有类变量
class Car:
    __total_cars = 0  # 私有类变量，外部无法直接访问

    def __init__(self, brand, model):
        self.__brand = brand  # 私有变量，外部无法直接访问
        self.__model = model  # 私有变量，外部无法直接访问
        Car.__total_cars += 1  # 增加汽车总数

    def get_total_cars(self):
        return Car.__total_cars  # 获取汽车总数的方法


# 创建汽车对象
car1 = Car("丰田", "卡罗拉")  # 创建汽车对象
print(car1.get_total_cars())  # 输出: 1

car2 = Car("本田", "思域")  # 创建汽车对象
# print(Car.__total_cars) # AttributeError: type object 'Car' has no attribute '__total_cars'
print(car1.get_total_cars())  # 输出: 2
print(car2.get_total_cars())  # 输出: 2

# 访问私有属性 不推荐
# 在Python中，以双下划线开头的属性会被自动改名为：_类名__属性名
# 这就是为什么可以通过 _Student__name 访问 __name 属
# 这种机制称为名称改写(name mangling)，是Python实现属性私有化的方式
# 虽然技术上可以访问，但这违背了封装原则，应该使用getter方法
print(car1._Car__brand)  # 输出: 丰田
print(car2._Car__brand)  # 输出: 本田
