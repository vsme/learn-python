# 定义一个学生类，使用@property装饰器
class Student:
    def __init__(self):
        self._score = 0  # 私有变量，外部无法直接访问

    # @property装饰器可以将一个方法转换为属性，使得我们可以像访问属性一样调用这个方法
    # 这样可以在不改变类接口的情况下，增加对属性的控制，比如添加验证逻辑
    # 在这个例子中，它使得我们可以通过student.score来获取分数，而不是调用student.score()
    @property
    def score(self):
        return self._score  # 获取分数的方法

    # @score.setter装饰器是用于设置属性的值
    # 它将一个方法转换为属性，使得我们可以像设置属性一样调用这个方法
    # 这样可以在不改变类接口的情况下，增加对属性的控制，比如添加验证逻辑
    # 在这个例子中，它使得我们可以通过student.score = 90来设置分数，而不是调用student.score(90)
    # score指的就是score方法,setter是固定写法，这个表示设置score方法的值
    @score.setter
    def score(self, value):
        if not isinstance(value, int):  # 检查参数类型
            raise ValueError("分数必须是整数！")  # 抛出错误
        if value < 0 or value > 100:  # 检查参数范围
            raise ValueError("分数必须在0到100之间！")  # 抛出错误
        self._score = value  # 设置分数


# 创建学生对象
student = Student()  # 创建学生对象
student.score = 90  # 设置分数
print(student.score)  # 输出: 90
# student.score = 999  # ValueError: 分数必须在0到100之间！


# 定义一个屏幕类，使用@property装饰器
class Screen:
    def __init__(self):
        self._width = 0  # 私有变量，外部无法直接访问
        self._height = 0  # 私有变量，外部无法直接访问

    @property
    def width(self):
        return self._width  # 获取宽度的方法

    @width.setter
    def width(self, value):
        if not isinstance(value, int):  # 检查参数类型
            raise ValueError("宽度必须是整数！")  # 抛出错误
        if value <= 0:  # 检查参数范围
            raise ValueError("宽度必须大于0！")  # 抛出错误
        self._width = value  # 设置宽度

    @property
    def height(self):
        return self._height  # 获取高度的方法

    @height.setter
    def height(self, value):
        if not isinstance(value, int):  # 检查参数类型
            raise ValueError("高度必须是整数！")  # 抛出错误
        if value <= 0:  # 检查参数范围
            raise ValueError("高度必须大于0！")  # 抛出错误
        self._height = value  # 设置高度

    @property
    def resolution(self):
        return self._width * self._height  # 计算分辨率的方法


# 创建屏幕对象
screen = Screen()  # 创建屏幕对象
screen.width = 1024  # 设置宽度
screen.height = 768  # 设置高度
print(screen.resolution)  # 输出: 786432
