# 定义一个动物类
class Animal:
    def speak(self):
        pass  # 动物发出声音的方法


# 定义一个狗类，继承自动物类
class Dog(Animal):
    def speak(self):
        return "汪汪！"  # 狗发出声音


# 定义一个猫类，继承自动物类
class Cat(Animal):
    def speak(self):
        return "喵喵！"  # 猫发出声音


# 定义一个乌龟类，继承自动物类
class Tortoise(Animal):
    def speak(self):
        return "咕噜咕噜！"  # 乌龟发出声音


# 定义一个函数，接受动物对象
def animal_speak(animal):
    print(animal.speak())  # 调用动物的speak方法


# 创建狗、猫和乌龟对象
dog = Dog()  # 创建狗对象
cat = Cat()  # 创建猫对象
tortoise = Tortoise()  # 创建乌龟对象
animal_speak(dog)  # 输出: 汪汪！
animal_speak(cat)  # 输出: 喵喵！
animal_speak(tortoise)  # 输出: 咕噜咕噜！
