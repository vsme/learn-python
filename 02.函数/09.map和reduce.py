# map 基本用法
print(list(map(abs, [-1, 2, -3])))          # [1, 2, 3]
print(list(map(str.upper, ["a", "b"])))     # ['A', 'B']

# 多个可迭代会“并行”取值，长度以最短的为准
a, b = [1, 2, 3], [10, 20]
print(list(map(lambda x, y: x + y, a, b)))  # [11, 22]

# 等价写法
print([x*x for x in range(5)])                 # 列表推导式
print(list((x*x for x in range(5))))           # 生成器表达式（同样惰性）
print([x+y for x, y in zip(a, b)])             # 多输入时配 zip

# reduce 用法
from functools import reduce
from operator import add, mul

# 求和 / 求积（其实直接用内置更好）
print(sum([1, 2, 3, 4]))        # 10
print(reduce(add, [1, 2, 3, 4], 0))     # 10
print(reduce(mul, [1, 2, 3, 4], 1))     # 24

# 把字符串拼起来（更推荐 ''.join(...)）
print(reduce(add, ["py", "thon"], ""))  # 'python'
# join 更推荐
print("".join(["py", "thon"]))   # 'python'

# 场景
# 1) 函数组合（把多个函数合成一个）
from functools import reduce
def compose(*funcs):
    return lambda x: reduce(lambda v, f: f(v), reversed(funcs), x)

f = compose(str, abs)   # 等价于 lambda x: str(abs(x))
print(f(-3))  # '3'

# 2) 自定义聚合：累加到字典/集合（也可用循环/Counter）
def merge_counts(acc, x):
    acc[x] = acc.get(x, 0) + 1
    return acc
print(reduce(merge_counts, "banana", {}))     # {'b':1,'a':3,'n':2}

# 3) 扁平化（更推荐 itertools.chain）
from itertools import chain
lists = [[1,2],[3,4],[5]]
# 不推荐：reduce(add, lists, [])  # list 拼接会 O(n^2)
print(list(chain.from_iterable(lists)))       # 更高效
