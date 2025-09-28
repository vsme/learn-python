def greet(fn):  # 装饰器：接收函数 → 返回函数
    def wrapper(*args, **kwargs):  # 包一层，添加前后逻辑
        print(">>> before")
        result = fn(*args, **kwargs)
        print("<<< after")
        return result

    return wrapper


@greet  # 等价于: say = greet(say)
def say(name):
    print(f"Hello, {name}")


say("Alice")

# 定义一个装饰器，计算函数执行时间
import time


def timer(func):
    def wrapper(*args, **kw):
        start = time.time()  # 记录开始时间
        result = func(*args, **kw)  # 调用原函数
        end = time.time()  # 记录结束时间
        print(f"函数 {func.__name__} 执行了 {end - start:.2f} 秒")  # 打印执行时间
        return result  # 返回原函数的结果

    return wrapper  # 返回包装后的函数


# 使用装饰器
@timer
def slow_function():
    time.sleep(1)  # 模拟耗时操作
    print("函数执行完毕")


slow_function()
# 函数执行完毕
# 函数 slow_function 执行了 1.02 秒
print(slow_function.__name__)  # 输出: wrapper，而不是slow_function

import asyncio, time
from functools import wraps


def atime(fn):
    @wraps(fn)
    async def w(*a, **kw):
        t = time.perf_counter()
        try:
            return await fn(*a, **kw)
        finally:
            print("cost:", time.perf_counter() - t)

    return w


@atime
async def fetch():
    await asyncio.sleep(1)  # 模拟耗时操作
    print("函数执行完毕")


asyncio.run(fetch())  # 输出: cost: 1.0058417919790372

# 使用functools.wraps保留原函数的元信息
from functools import wraps


def log(func):
    # functools.wraps也是一个装饰器，可以把原函数的元信息添加到包装函数（wrapper）中
    # wraps的原理是：
    # 1. 获取原函数的元信息（如函数名、文档字符串等）
    # 2. 将这些元信息添加到包装函数（wrapper）中
    # 3. 返回包装后的函数
    @wraps(func)  # 保留原函数的元信息
    def wrapper(*args, **kw):
        print("开始执行函数:", func.__name__)  # 打印函数名
        result = func(*args, **kw)  # 调用原函数
        print("函数执行完毕")  # 打印结束信息
        return result  # 返回原函数的结果

    return wrapper  # 返回包装后的函数


# 使用装饰器
@log
def hello():
    print("你好，世界！")


print(hello.__name__)  # 输出: hello，而不是wrapper


# 定义一个权限验证装饰器
def require_auth(func):
    def wrapper(*args, **kw):
        print("验证权限...")  # 模拟权限验证
        if True:  # 假设验证通过
            return func(*args, **kw)  # 调用原函数
        else:
            print("权限不足")  # 验证失败

    return wrapper  # 返回包装后的函数


# 使用装饰器
@require_auth
def admin_page():
    print("欢迎来到管理页面")


admin_page()  # 输出: 验证权限...\n欢迎来到管理页面


# 方法装饰器
def log_call(fn):
    @wraps(fn)
    def w(self, *a, **kw):
        print(f"call {fn.__name__} with", a, kw)
        return fn(self, *a, **kw)

    return w


class Svc:
    @log_call
    def run(self, x):
        return x * 2


s = Svc()
s.run(3)  # 输出: call run with (3,) {}
print(s.run.__name__)  # 输出: run，而不是wrapper


# 类装饰器
def add_repr(cls):
    # __repr__ 是 Python 内置的特殊方法，用于返回对象的“官方”字符串表示，方便调试和日志记录
    # 当打印实例时，会输出 "<类名 实例属性字典>" 的格式
    cls.__repr__ = lambda self: f"<{cls.__name__} {self.__dict__}>"
    return cls


@add_repr
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y


p = Point(3, 4)
print(p)  # 输出: <Point {'x': 3, 'y': 4}>

from functools import wraps


# 装饰器工厂：带重试次数参数
def retry(times=3):
    def deco(fn):
        @wraps(fn)
        def wrapper(*a, **kw):
            last = None
            for attempt in range(1, times + 1):
                try:
                    return fn(*a, **kw)
                except Exception as e:
                    last = e
                    # 打印每次失败信息，方便调试
                    print(f"[retry {attempt}/{times}] {e}")
            # 所有重试都失败后，抛出最后一次异常
            raise last

        return wrapper

    return deco


@retry(times=5)
def flaky():
    import random

    # 把随机种子固定，确保每次运行结果一致，方便观察重试过程
    # random.seed(1)
    if random.randint(0, 1) == 0:
        raise ValueError("随机失败")
    return "成功"


print(flaky())  # 有 50% 的概率成功，否则抛出 ValueError

from functools import wraps


def deco(n):  # 外层：装饰器工厂（接参数）
    print("factory called with", n)

    def decorator(func):  # 内层：真正装饰器（接函数）
        print("decorating", func.__name__)

        @wraps(func)
        def wrapper(*a, **kw):
            print("n is", n)  # 用到外层参数（闭包捕获）
            return func(*a, **kw)

        return wrapper

    return decorator


@deco(5)
def hello():
    print("hello")


hello()
