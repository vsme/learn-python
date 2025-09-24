# 生成器函数：用 yield 按需产出元素；天然是迭代器。
def countdown(n):
    while n > 0:
        yield n   # 产出 n，并暂停在这里
        n -= 1    # 下次继续从这里往后跑

g = countdown(3)
next(g)     # 3
next(g)     # 2
next(g)     # 1
# next(g)     # StopIteration 异常（迭代结束）

# 通常用 for 最方便：
for x in countdown(3):  # 3, 2, 1
    print(x)

# 列表推导（立即生成列表，占用对应内存）
lst = [x*x for x in range(10)]   # [0, 1, 4, ..., 81]

# 生成器表达式（惰性，不占大内存）
gen = (x*x for x in range(10))

print(next(gen))      # 0
print(next(gen))      # 1
print(list(gen))      # [4, 9, 16, 25, 36, 49, 64, 81]  # 把剩下的取完
# 生成器表达式是迭代器，只能遍历一次
# 遍历完后，再次遍历会抛出 StopIteration 异常
print(list(gen))      # []  已经耗尽

iterable_iter = iter([1,2,3])    # 从可迭代得到迭代器
next(iterable_iter)              # -> 1

# itertools 小而美（懒序列工具箱）
from itertools import islice, count, chain

print(list(islice(count(10, 2), 3)))  # [10, 12, 14]  无限序列切片
print(list(chain([1,2], [3,4])))      # [1,2,3,4]

message = 'Python'
for char in message:
    print(char, end='\n')
