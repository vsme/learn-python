# 语法 partial(func, /, *args, **kwargs)
# 返回 newfunc，调用时执行 func(*args, *new_args, **kwargs, **new_kwargs)。
from functools import partial

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)   # 先把 exp 固定为 2
print(square(9))                 # 81  —— 等价 power(9, exp=2)

# partialmethod
# partialmethod(func, /, *args, **kwargs) 是一个描述符（descriptor），专门用于在类里定义“预先固定了一部分参数”的方法。
# 调用效果等价：func(self, *pre_args, *call_args, **pre_kwargs, **call_kwargs)
from functools import partialmethod

class Greeter:
    def speak(self, who, punct="!"):
        return f"Hello, {who}{punct}"

    hi = partialmethod(speak, punct=" :)")  # 预绑定 punct

g = Greeter()
print(g.speak("World"))  # Hello, World!
print(g.hi("World"))     # Hello, World :)

# 对比差异
class A:
    def add(self, x, y):
        return x + y

    add5_wrong = partial(add, 5)         # ❌ 不会绑定 self
    add5       = partialmethod(add, 5)   # ✅ 正确：先把 self 绑定，再把 5 拼上

a = A()
# print(a.add5_wrong(10))   # TypeError: missing 'self'
print(a.add5(10))           # 15
