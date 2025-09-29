# 定义一个动物类
class Animal:
    def __init__(self, name):
        self.name = name  # 动物的名字


# 定义一个可跑类
class Runnable:
    def run(self):
        print(f"{self.name}正在跑...")  # 跑的方法


# 定义一个可飞类
class Flyable:
    def fly(self):
        print(f"{self.name}正在飞...")  # 飞的方法


# 定义一个狗类，继承自动物类和可跑类
class Dog(Animal, Runnable):
    pass


# 定义一个蝙蝠类，继承自动物类和可飞类
class Bat(Animal, Flyable):
    pass


# 创建狗和蝙蝠对象
dog = Dog("旺财")  # 创建狗对象
bat = Bat("小蝙蝠")  # 创建蝙蝠对象
dog.run()  # 旺财正在跑...
bat.fly()  # 小蝙蝠正在飞...


# 定义一个动物类
class Animal:
    def __init__(self, name):
        self.name = name  # 动物的名字


# 定义一个哺乳类，继承自动物类
class Mammal(Animal):
    pass


# 定义一个鸟类，继承自动物类
class Bird(Animal):
    pass


# 定义一个可跑类
class Runnable:
    def run(self):
        print(f"{self.name}正在跑...")  # 跑的方法


# 定义一个可飞类
class Flyable:
    def fly(self):
        print(f"{self.name}正在飞...")  # 飞的方法


# 定义一个狗类，继承自哺乳类和可跑类
class Dog(Mammal, Runnable):
    pass


# 定义一个蝙蝠类，继承自哺乳类和可飞类
class Bat(Mammal, Flyable):
    pass


# 定义一个鹦鹉类，继承自鸟类和可飞类
class Parrot(Bird, Flyable):
    pass


# 定义一个鸵鸟类，继承自鸟类和可跑类
class Ostrich(Bird, Runnable):
    pass


# 创建狗、蝙蝠、鹦鹉和鸵鸟对象
dog = Dog("旺财")  # 创建狗对象
bat = Bat("小蝙蝠")  # 创建蝙蝠对象
parrot = Parrot("小鹦鹉")  # 创建鹦鹉对象
ostrich = Ostrich("小鸵鸟")  # 创建鸵鸟对象
dog.run()  # 输出: 旺财正在跑...
bat.fly()  # 输出: 小蝙蝠正在飞...
parrot.fly()  # 输出: 小鹦鹉正在飞...
ostrich.run()  # 输出: 小鸵鸟正在跑...
