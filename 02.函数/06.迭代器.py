# 可以使用 isinstance () 函数来检查一个对象是否为可迭代对象或迭代器。
from collections.abc import Iterable, Iterator

# 创建一个列表（可迭代对象）
fruits = ["苹果", "香蕉", "橙子"]
# 检查是否为可迭代对象
print(isinstance(fruits, Iterable))  # 输出：True
# 迭代对象不是迭代器
print(isinstance(fruits, Iterator))  # 输出：False

# 将可迭代对象转换为迭代器
fruit_iterator = iter(fruits)
# 检查是否为迭代器
print(isinstance(fruit_iterator, Iterable))  # 输出：True
# 迭代器是可迭代对象
print(isinstance(fruit_iterator, Iterator))  # 输出：True

# for x in obj 的幕后
obj = [10, 20, 30]
it = iter(obj)  # 调 obj.__iter__() 得到迭代器
while True:
    try:
        x = next(it)  # 调 it.__next__()
    except StopIteration:
        break
    # 使用 x

# 把可迭代对象变成迭代器
it = iter([10, 20, 30])
print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
# next(it)  # StopIteration


# 自定义迭代器
class CountDown:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self  # 迭代器返回自身

    def __next__(self):
        if self.n <= 0:
            raise StopIteration  # 告诉外界“没有更多元素了”
        self.n -= 1
        return self.n + 1


for x in CountDown(3):  # 3, 2, 1
    print(x)


# 迭代器工厂
def countdown(n):
    while n > 0:
        yield n
        n -= 1


# `raise` 关键词，抛出异常用的语句。抛出后，当前流程会立刻中断，转去寻找匹配的 `except` 处理；若没人接住，程序就报错结束。
# raise ValueError("bad input")           # 抛出内置异常
# raise MyError("oops")                   # 抛出自定义异常
# raise RuntimeError from exc             # 异常链（把原因exc附带上）


# `StopIteration` 异常类，表示迭代已经结束，这是迭代器协议里规定的“终止信号”。
# `for` 循环、`list(iterable)` 等迭代消费者看见这个异常就会正常停止，不会把它当错误显示出来。
# - 在生成器函数（用 `yield` 的函数）内部，不要手动 `raise StopIteration` 来结束
# 正确做法是自然走到函数末尾或 `return 值`（`return` 的值会成为 `StopIteration.value`）
# Python 3.7 起 `StopIteration` 从生成器冒出，会被转成 `RuntimeError`（PEP 479）
def gen_ok():
    yield "ok"
    return 66  # 推荐：结束并带“返回值”


g = gen_ok()

try:
    print(next(g))  # 'ok'
    next(g)  # 触发结束
except StopIteration as e:
    print("返回值：", e.value)  # 66


def gen_bad():
    yield "bad"
    raise StopIteration(33)  # 会被改写成 RuntimeError("generator raised StopIteration")


bad = gen_bad()

try:
    print(next(bad))  # bad
    next(bad)  # 触发结束
except RuntimeError as e:
    print("返回值：", e)  # generator raised StopIteration


g = gen_bad()
print(next(g))  # bad

try:
    next(g)
except RuntimeError as e:
    # “曲线救国”：从 RuntimeError.__cause__ 里抠（非常不推荐）
    cause = e.__cause__
    if isinstance(cause, StopIteration):
        print("返回值：", cause.value)  # 33
