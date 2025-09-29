# 元类示例：注册模式
class RegistryMeta(type):
    registry = {}

    def __init__(cls, name, bases, ns):
        super().__init__(name, bases, ns)
        if bases:  # 跳过根类
            RegistryMeta.registry[name] = cls


class Base(metaclass=RegistryMeta):
    pass


class A(Base):
    pass


class B(Base):
    pass


print(RegistryMeta.registry)  # {'A': <class '__main__.A'>, 'B': <class '__main__.B'>}


class RequireRunMeta(type):
    def __init__(cls, name, bases, ns):
        super().__init__(name, bases, ns)
        if bases and "run" not in ns:
            raise TypeError(f"{name} must define run()")


class Task(metaclass=RequireRunMeta):
    pass


class Good(Task):
    def run(self):
        print("Good run")


# class Bad(Task):
#     pass  # TypeError: Bad must define run()
# type 示例
# 定义一个函数，接受self参数和name参数（默认值为'world'）
def fn(self, name="world"):
    # 使用f字符串格式化输出问候语
    print(f"Hello, {name}.")


# 使用type()函数动态创建一个名为Hello的类，继承自object，包含hello方法
Hello = type("Hello", (object,), {"hello": fn})
# 创建Hello类的实例对象
h = Hello()
# 调用实例对象的hello方法
h.hello()  # Hello, world.
# 打印Hello类的类型，显示它是一个type类的实例
print(type(Hello))  # <class 'type'>
# 打印实例对象h的类型，显示它是Hello类的实例
print(type(h))  # <class '__main__.Hello'>


# 定义一个名为ListMetaclass的元类，继承自type
class ListMetaclass(type):
    # 定义__new__方法，用于创建新的类对象
    # cls 是当前类 <class '__main__.ListMetaclass'>
    # name 是创建的类的名字 MyList
    # bases 是创建的类的父类 (<class 'list'>,)
    # attrs 是创建的类的属性字典 {'__module__': '__main__', '__qualname__': 'MyList'}
    def __new__(cls, name, bases, attrs):
        # 在类的属性字典中添加一个add方法，该方法调用list的append方法
        attrs["add"] = lambda self, value: self.append(value)
        # 调用type的__new__方法创建并返回新的类对象
        return type.__new__(cls, name, bases, attrs)


# 使用ListMetaclass元类创建一个名为MyList的类，继承自list
# list是Python内置的列表类型，这里MyList继承自list，获得了列表的所有功能
# metaclass=ListMetaclass 指定使用ListMetaclass作为元类来创建MyList类
class MyList(list, metaclass=ListMetaclass):
    # 空类体，不添加任何额外的方法或属性
    pass


# 创建MyList类的一个实例对象
L = MyList()
# 调用通过元类添加的add方法，向列表中添加元素1
L.add(1)
# 打印列表内容，输出结果为[1]
print(L)
