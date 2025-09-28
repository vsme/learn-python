# 定义一个学生类
class Student:
    # __init__ 是Python的特殊方法，用于初始化对象，会在创建对象时自动调用
    # 初始化方法的第一个参数通常是self，表示对象本身
    # 初始化方法，接收名字和分数两个参数
    def __init__(self, name, score):
        # 将传入的名字赋值给实例变量name
        self.name = name
        # 将传入的分数赋值给实例变量score
        self.score = score

    # 方法的第一个参数通常是self，表示对象本身
    def print_score(self):
        # 使用f-string格式化输出学生的名字和分数
        print(f"{self.name}的分数是{self.score}")


# 创建一个名为"小明"、分数为90的学生实例
student1 = Student("小明", 90)
# 调用学生实例的print_score方法，打印小明的分数
student1.print_score()


# 定义一个银行账户类
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # 私有属性，外部无法直接访问

    def deposit(self, amount):
        self.__balance += amount  # 存款方法

    def get_balance(self):
        return self.__balance  # 获取余额方法


bankAccount = BankAccount(1000)
print(bankAccount.get_balance())  # 输出: 1000
bankAccount.deposit(500)
print(bankAccount.get_balance())  # 输出: 1500


class Animal:
    def __init__(self, name):
        self.name = name  # 动物的名字

    def speak(self):
        pass  # 动物发出声音的方法


# 定义一个狗类，继承自动物类
class Dog(Animal):
    def speak(self):
        return f"{self.name}说：汪汪！"  # 狗发出声音


# 定义一个猫类，继承自动物类
class Cat(Animal):
    def speak(self):
        return f"{self.name}说：喵喵！"  # 猫发出声音


# 创建狗对象
dog = Dog("旺财")  # 创建狗对象
print(dog.speak())  # 输出: 旺财说：汪汪！

# 创建猫对象
cat = Cat("咪咪")  # 创建猫对象
print(cat.speak())  # 输出: 咪咪说：喵喵！
