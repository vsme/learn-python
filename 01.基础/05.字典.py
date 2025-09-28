book = {"title": "Fluent Python", "price": 88, ("pub", "year"): 2021}

d = {"a": 1}

# 查
print(d["a"])  # 1；键不存在会 KeyError
print(d.get("x", 0))  # 0；更安全：给默认值
print("x" in d)  # False
print(d.get("y"))  # 0；更安全：给默认值

# 增改
d["b"] = 2
print(d)
d.update({"c": 3, "a": 9})  # 批量合并/覆盖
print(d)

d |= {"d": 4}  # 3.9+ 合并运算
print(d)
{**d, **{"e": 5}}  # 解包合并成新字典
print({**d, **{"e": 5}})

# 删
del d["b"]
print(d)

# d.pop("xxx")               # 键不存在会 KeyError
d.pop("c", None)  # 带默认值更稳
print(d)

d.clear()  # 清空
print(d)

# for k in d: ...              # 键
# for k, v in d.items(): ...   # 键值对
# d.keys(), d.values(), d.items()  # 动态“视图”，随字典变化而变

squares = {x: x * x for x in range(5)}  # {0:0, 1:1, ...}
print(squares)
