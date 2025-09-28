s = "abcdefg"
print(s[1:4])  # 'bcd'
s[:3]  # 'abc'
s[4:]  # 'efg'
s[::2]  # 'aceg'
s[-4:-1]  # 'def'
s[::-1]  # 'gfedcba'  反转

# 赋值/删除切片（仅 list 等可变序列）
a = [0, 1, 2, 3, 4, 5]
a[2:5] = [20, 30]  # → [0,1,20,30,5]   # 替换并缩短
print(a)
a[2:2] = [7, 8]  # → [0,1,7,8,20,30,5]  # 在索引 2 处插入
print(a)
a[::2] = [9, 9, 9, 9]  # 步长切片赋值，右侧长度必须匹配元素个数
print(a)

del a[1:4]  # 删除片段

print(a)

# 使用 sorted
# 创建一个学生成绩列表
scores = [85, 92, 78, 90, 88, 95, 82, 87, 91, 89]

# 排序后的所有成绩
print(sorted(scores))

# 获取前5名学生的成绩
# 使用sorted函数对scores列表进行排序，并使用reverse=True参数进行降序排序
# 然后使用切片[:5]获取前5名学生的成绩
top_five = sorted(scores, reverse=True)[:5]
print("前5名成绩:", top_five)  # 输出: [95, 92, 91, 90, 89]

# 获取后3名学生的成绩
# 使用sorted函数对scores列表进行排序，并使用reverse=False参数进行升序排序
# 然后使用切片[:3]获取后3名学生的成绩
bottom_three = sorted(scores)[:3]
print("后3名成绩:", bottom_three)  # 输出: [78, 82, 85]
