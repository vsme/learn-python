# 导入枚举类
from enum import Enum, unique  # 导入枚举类

# 定义一个月份枚举类
Month = Enum(
    "Month",
    (
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ),
)  # 定义月份枚举类

# 遍历月份枚举类
for name, member in Month.__members__.items():  # 遍历月份枚举类
    print(name, "=>", member, ",", member.value)  # 输出月份名称、成员和值

# Jan => Month.Jan , 1
# Feb => Month.Feb , 2
# Mar => Month.Mar , 3
# Apr => Month.Apr , 4
# May => Month.May , 5
# Jun => Month.Jun , 6
# Jul => Month.Jul , 7
# Aug => Month.Aug , 8
# Sep => Month.Sep , 9
# Oct => Month.Oct , 10
# Nov => Month.Nov , 11
# Dec => Month.Dec , 12


# 定义一个星期枚举类
class Weekday(Enum):  # 定义星期枚举类
    Sun = 0  # 星期日
    Mon = 1  # 星期一
    Tue = 2  # 星期二
    Wed = 3  # 星期三
    Thu = 4  # 星期四
    Fri = 5  # 星期五
    Sat = 6  # 星期六


# 访问星期枚举类
day1 = Weekday.Mon  # 获取星期一
print(day1)  # 输出: Weekday.Mon
print(Weekday.Tue)  # 输出: Weekday.Tue
print(Weekday["Tue"])  # 输出: Weekday.Tue
print(Weekday.Tue.value)  # 输出枚举的值 2


# 定义一个性别枚举类
@unique  # 使用unique装饰器确保没有重复值
class Gender(Enum):  # 定义性别枚举类
    Male = 0  # 男性
    Female = 1  # 女性


# 定义一个学生类
class Student:  # 定义学生类
    def __init__(self, name, gender):  # 初始化方法
        self.name = name  # 学生名字
        self.gender = gender  # 学生性别


# 创建学生对象
bart = Student("Bart", Gender.Male)  # 创建学生对象
if bart.gender == Gender.Male:  # 判断性别
    print("测试通过!")  # 输出: 测试通过!
else:
    print("测试失败!")


# 定义一个颜色枚举类
@unique  # 使用unique装饰器确保没有重复值
class Color(Enum):  # 定义颜色枚举类
    Red = 1  # 红色
    Green = 2  # 绿色
    Blue = 3  # 蓝色


# 通过成员名称访问
print(Color.Red)  # 输出: Color.Red
# 通过成员值访问
print(Color.Red.value)  # 输出: 1
# 通过成员索引访问
print(Color["Red"])  # 输出: Color.Red
