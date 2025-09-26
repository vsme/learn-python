# 只保留偶数
print(list(filter(lambda x: x % 2 == 0, range(10))))   # [0, 2, 4, 6, 8]

# 去掉空白行
lines = ["a", " ", "", "b"]
print(list(filter(str.strip, lines)))                  # ['a', 'b']

# 过滤掉“假值”
xs = [0, 1, "", "hi", None, [], [1]]
print(list(filter(None, xs)))                          # [1, 'hi', [1]]

# 等价于推导式
print([x for x in range(10) if x % 2 == 0])
print(list(s for s in lines if s.strip()))      # 惰性：生成器表达式

# 例子：筛选出所有能被3整除的数
nums = list(range(1, 21))
# 用lambda表达式直接写判断逻辑
divisible_by_3 = filter(lambda x: x % 3 == 0, nums)
print(list(divisible_by_3))  # 输出: [3, 6, 9, 12, 15, 18]

# sort 排序
names = ["Tom", "alice", "BOB"]
print(sorted(names))                     # ['BOB','Tom','alice']（默认大小写先大写）
print(sorted(names, key=str.lower))      # ['alice','BOB','Tom']（忽略大小写）
print(sorted(names, key=str.casefold))   # 更稳的大小写折叠

# 多字段排序
from operator import attrgetter

records = [
    {"name":"A", "age":30, "score":90},
    {"name":"B", "age":30, "score":85},
    {"name":"C", "age":25, "score":95},
]
# 先按 age 升序，再按 score 降序
print(sorted(records, key=lambda r: (r["age"], -r["score"])))
# → [{'name': 'C', 'age': 25, 'score': 95},
#    {'name': 'B', 'age': 30, 'score': 85},
#    {'name': 'A', 'age': 30, 'score': 90}]

# 对对象：
class Emp:
    def __init__(self, name, dept, age):
        self.name = name
        self.dept = dept
        self.age = age

objs = [
    Emp("Alice", "Sales", 30),
    Emp("Bob",   "Sales", 25),
    Emp("Caro",  "Tech",  28),
]

# 先按 dept 升序，再按 age 升序（稳定排序）
out = sorted(objs, key=attrgetter("dept", "age"))
print('out', out)
print([(o.name, o.dept, o.age) for o in out]) 
# → [('Alice','Sales',30), ('Bob','Sales',25), ('Caro','Tech',28)]  # 注意稳定性

# 字典相关的排序
d = {"x": 5, "y": 2, "z": 9}
print(sorted(d))                          # ['x','y','z']  —— 按键
print(sorted(d.items(), key=lambda kv: kv[1], reverse=True))  # 按值
# 若想得到“按值排序后”的字典（Py3.7+字典保持插入顺序）：
print(dict(sorted(d.items(), key=lambda kv: kv[1])))
# → {'y': 2, 'x': 5, 'z': 9}

# 处理 None/缺失值
rows = [{"age": 30}, {"age": None}, {"age": 20}]
# 让 None 排在最后：
print(sorted(rows, key=lambda r: (r["age"] is None, r["age"])))
# → [{'age': 20}, {'age': 30}, {'age': None}]

# 小抄
xs = ["bb", "a", "ccc", "aa", "b", "d"]
print(sorted(xs))                              # 基本
print(sorted(xs, reverse=True))                # 降序
print(sorted(xs, key=len))                     # 按长度
print(sorted(xs, key=lambda s: (len(s), s)))   # 多键 先按长度，再按字母序

d = {"x": 5, "y": 2, "z": 9, "w": 2}
print(sorted(d.items(), key=lambda kv: kv[1])) # 字典按值
