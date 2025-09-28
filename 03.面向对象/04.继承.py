class Animal:
    def speak(self):
        print("动物发出声音")  # 动物发出声音的方法


class Dog(Animal):
    def speak(self):
        super().speak()  # 调用父类的speak方法
        print("汪汪！")


dog = Dog()
dog.speak()  # 输出: 动物发出声音 汪汪！


# 定义一个形状类
class Shape:
    def area(self):
        pass  # 计算面积的方法


# 定义一个矩形类，继承自形状类
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width  # 矩形的宽度
        self.height = height  # 矩形的高度

    def area(self):
        return self.width * self.height  # 计算矩形的面积


# 定义一个圆形类，继承自形状类
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius  # 圆形的半径

    def area(self):
        return 3.14 * self.radius**2  # 计算圆形的面积


# 定义一个函数，接受形状对象
def print_area(shape):
    print(f"面积：{shape.area()}")  # 打印形状的面积


# 创建矩形和圆形对象
rect = Rectangle(5, 3)  # 创建矩形对象
circle = Circle(2)  # 创建圆形对象
print_area(rect)  # 输出: 面积：15
print_area(circle)  # 输出: 面积：12.56
