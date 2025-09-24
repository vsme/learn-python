# [ 表达式  for 变量 in 可迭代对象  if 条件 ]
# 等价于
# out = []
# for 变量 in 可迭代对象:
#     if 条件:
#         out.append(表达式)

# 平方表
squares = [x*x for x in range(6)]              # [0,1,4,9,16,25]
print(squares)

# 过滤：只要偶数的平方
even_sq = [x*x for x in range(10) if x % 2 == 0]  # [0,4,16,36,64]
print(even_sq)

# 条件表达式（内联三元运算）
labels = ["odd" if x % 2 else "even" for x in range(5)]
# 等价循环：if…else 放在表达式位置，不是过滤
print(labels)

# 笛卡尔积（所有配对）
pairs = [(i, j) for i in range(3) for j in range(2)]
print(pairs)
# → [(0,0),(0,1),(1,0),(1,1),(2,0),(2,1)]  # 左到右依次展开

# 扁平化二维列表
matrix = [[1,2,3],[4,5,6]]
flat = [x for row in matrix for x in row]      # [1,2,3,4,5,6]
print(flat)

data = ["a","b","c"]
with_idx = [(i, x) for i, x in enumerate(data, start=1)]  # [(1,'a'),...]
print(with_idx)
zipped   = [a+b for a, b in zip("ABC", "xyz")]            # ['Ax','By','Cz']
print(zipped)

# 集合推导：自动去重
s = {x % 3 for x in range(10)}                 # {0,1,2}
print(s)

# 字典推导：键值对
d = {x: x*x for x in range(5)}                 # {0:0, 1:1, ...}
print(d)

lines = ["  a b c ", " d e f ", " g h i "]
# 清洗数据：去空白并过滤空串
clean = [s.strip() for s in lines if s.strip()]
print(clean)

# 展开并过滤
words = [w.lower() for line in lines for w in line.split() if w]
print(words)

# 仅保留字母数字
import re
strings = ["a123", "b456", "c789"]
norm = [re.sub(r"\W+", "", s) for s in strings]
print(norm)

# 海象运算符 := 表达式里复用中间结果
# n 只算一次，既做过滤又收集
import os
sizes = [n for s in os.listdir(".") if (n := os.path.getsize(os.path.join(".", s))) > 0]
print('sizes', sizes)

# 创建一个学生成绩列表
scores = [
    {'name': '小明', 'score': 85},
    {'name': '小红', 'score': 92},
    {'name': '小华', 'score': 78},
    {'name': '小李', 'score': 90}
]

# 获取所有及格学生的名字
passing_students = [student['name'] for student in scores if student['score'] >= 60]
print("及格学生:", passing_students)  # 输出: ['小明', '小红', '小华', '小李']

# 计算每个学生的成绩等级
grade_list = [
    f"{student['name']}: {'优秀' if student['score'] >= 90 else '良好' if student['score'] >= 80 else '及格' if student['score'] >= 60 else '不及格'}"
    for student in scores
]
print("成绩等级:", grade_list)