# 下面这个类继承自Python内置的dict，实现了通过属性访问字典内容的功能
class MyDict(dict):
    def __init__(self, **kwargs):
        # 调用父类dict的初始化方法，把传入的关键字参数存到字典里
        super().__init__(**kwargs)

    def __getattr__(self, key):
        # 当用d.a方式访问属性时，会调用这个方法
        try:
            return self[key]  # 尝试从字典中取值
        except KeyError:
            # 如果没有这个key，抛出属性错误
            raise AttributeError(f"'MyDict'对象没有属性'{key}'")

    def __setattr__(self, key, value):
        # 当用d.a = 1方式设置属性时，会调用这个方法
        self[key] = value  # 实际上是往字典里存数据


# 创建一个MyDict实例，传入初始参数a=1, b=2
d = MyDict(a=1, b=2)
# 通过属性方式访问字典中的值，输出1
print(d.a)
# 通过属性方式修改字典中的值
d.a = 3
# 再次输出修改后的值，输出3
print(d.a)
