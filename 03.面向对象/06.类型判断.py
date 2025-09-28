print(isinstance(3, int))  # True
print(isinstance(True, bool))  # True
print(isinstance(True, int))  # True
print(isinstance([], (list, tuple)))  # 组合判断

print(type(True) is int)  # False  bool 是 int 的子类；而 isinstance(True, int) 为 True
print(type(True) is bool)  # True

from collections.abc import Iterable

print(isinstance("abc", Iterable))  # True
print(isinstance([1, 2, 3], Iterable))  # True
print(isinstance((1, 2, 3), Iterable))  # True
print(isinstance({1, 2, 3}, Iterable))  # True
print(isinstance({1: "a", 2: "b"}, Iterable))  # True
print(isinstance(123, Iterable))  # False

f = lambda x: x * 2

print(callable(f))  # True 是否可调用（函数/实现了 __call__ 的对象）


def X():
    def y():
        pass


x = X()


print(hasattr(x, "y"))  # False 是否有属性/方法（会触发 __getattr__/__getattribute__）


class X:
    def y(self):
        print("hi")


x = X()
print(hasattr(x, "y"))  # True
x.y()  # hi


from typing import Protocol


class Writer(Protocol):
    def write(self, s: str) -> int: ...


def dump(w: Writer):
    w.write("hi")


class A:
    def f(self):
        pass


a = A()
print(a.f)  # <bound method A.f of <A ...>>，自动绑定了 self
print(A.f)  # <function A.f at 0x...>，函数对象（未绑定）

obj = A()
print(obj.f)  # <bound method A.f of <A ...>>，自动绑定了 self
print(dir(obj))
print(
    'hasattr(obj, "f")', hasattr(obj, "f")
)  # True 是否有属性/方法（会触发 __getattr__/__getattribute__）


class ReadOnlyMapping:
    def __init__(self, data):
        self._data = dict(data)

    # 显示与布尔
    def __repr__(self):
        return f"ReadOnlyMapping({self._data!r})"

    def __bool__(self):
        return bool(self._data)

    # 容器协议
    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __contains__(self, key):
        return key in self._data

    def __getitem__(self, key):
        return self._data[key]

    # 禁止写操作
    def __setitem__(self, key, val):
        raise TypeError("read-only")

    def __delitem__(self, key):
        raise TypeError("read-only")


m = ReadOnlyMapping({"a": 1, "b": 2})
print(len(m), "a" in m, m["b"])  # 2, True, 2
print(m)  # ReadOnlyMapping({'a': 1, 'b': 2})\
print(m._data)  # {'a': 1, 'b': 2}
# m["b"] = 3  # TypeError: read-only


class User:
    def __init__(self, first, last):
        self.first, self.last = first, last

    @property
    def full(self):
        return f"{self.first} {self.last}"


# property 存在于类上；实例的 `__dict__` 里没有键 `full`
u = User("Ada", "Lovelace")
print(type(u))  # <class '__main__.User'>
# 这里的'__main__'表示当前执行的模块（或脚本）的名称

print("full" in vars(u))  # False
print(type(User.full))  # <class 'property'>
print(u.full)  # Ada Lovelace

# 判断函数类型
import types


def fn():
    pass


# 判断fn是否为函数类型
print(type(fn) == types.FunctionType)  # 输出: True
# 判断abs是否为内置函数类型
print(type(abs) == types.BuiltinFunctionType)  # 输出: True


# 定义一个动物类
class Animal:
    pass


# 定义一个狗类，继承自动物类
class Dog(Animal):
    pass


# 定义一个哈士奇类，继承自狗类
class Husky(Dog):
    pass


# 创建对象
animal = Animal()  # 创建动物对象
dog = Dog()  # 创建狗对象
husky = Husky()  # 创建哈士奇对象

# 判断对象类型
print(isinstance(husky, Husky))  # 输出: True
print(isinstance(husky, Dog))  # 输出: True
print(isinstance(husky, Animal))  # 输出: True
print(isinstance(dog, Husky))  # 输出: False
