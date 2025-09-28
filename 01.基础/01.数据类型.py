# 用单引号定义字符串
nickname = "小明"
# 用双引号定义字符串
city = "北京"
# 用三引号定义多行字符串
poem = """春眠不觉晓，
处处闻啼鸟。"""
print(nickname)  # 输出：小明
print(city)  # 输出：北京
print(poem)  # 输出多行诗句

# 字符串拼接
first_name = "张"
last_name = "三"
full_name = first_name + last_name  # 用+号拼接
print(full_name)  # 输出：张三

## 字符串和数字的拼接
# 字符串和数字拼接时，不能直接拼接，需要先将数字转换为字符串
age = 20
message = "我今年" + str(age) + "岁"
print(message)  # 输出：我今年20岁

# 字符串重复
laugh = "哈" * 5  # 字符串可以和数字相乘，表示重复
print(laugh)  # 输出：哈哈哈哈哈

# 百分号格式化
name = "小红"
age = 20
# 这是Python中的百分号格式化字符串方法
# %s 是一个占位符，表示将被字符串替换
# %d 是一个占位符，表示将被整数替换
# 括号中的(name, age)是要插入到字符串中的变量
# 变量会按顺序替换占位符：name替换%s，age替换%d
print("大家好，我叫%s，今年%d岁。" % (name, age))  # %s表示字符串，%d表示整数

# 常见的格式化占位符：
# %s - 字符串
# %d - 整数
# %f - 浮点数
# %.2f - 保留两位小数的浮点数
# %% - 输出百分号本身

# 编码为UTF-8字节
msg = "你好，世界"
msg_bytes = msg.encode("utf-8")  # 编码为字节
print(
    msg_bytes
)  # 输出：b'\xe4\xbd\xa0\xe5\xa5\xbd\xef\xbc\x8c\xe4\xb8\x96\xe7\x95\x8c'

# 解码回字符串
msg_str = msg_bytes.decode("utf-8")  # 解码为字符串
print(msg_str)  # 输出：你好，世界

s1 = "HELLO WORLD"

print(s1.lower())  # 输出: "hello world"
print(s1)  # 输出: "hello world"

# 创建一个装水果的列表
fruits = ["苹果", "香蕉", "橙子"]
print(fruits)  # 输出整个列表：['苹果', '香蕉', '橙子']
# 查看列表中有多少个元素
print(len(fruits))  # 输出：3

# 索引从0开始，依次访问每个水果
print(fruits[0])  # 输出第一个元素：苹果
print(fruits[1])  # 输出第二个元素：香蕉

# 访问最后一个元素，可以用-1
print(fruits[-1])  # 输出倒数第一个元素：橙子
# 访问不存在索引的元素会报错
# print(fruits[3])  # 报错：IndexError: list index out of range

# 在列表末尾添加一个新水果
fruits.append("葡萄")
print(fruits)  # 输出：['苹果', '香蕉', '橙子', '葡萄']
# append一次只能添加一个元素
# fruits.append("西瓜", "柠檬")  # 报错：TypeError: append() takes exactly one argument (2 given)

# 在指定位置插入一个水果，比如插到第2个位置（索引为1）
fruits.insert(1, "西瓜")
print(fruits)  # 输出：['苹果', '西瓜', '香蕉', '橙子', '葡萄']

# 删除最后一个水果
last = fruits.pop()
print(last)  # 输出被删除的水果：葡萄

# 删除指定位置的水果，比如删除第2个（索引为1）
removed = fruits.pop(1)
print(removed)  # 输出被删除的水果：西瓜
print(fruits)  # 输出：['苹果']

# 判断变量是不是元组
a = ()
b = 1
c = [2]
d = (3,)
e = (4, 5, 6)

print(isinstance(a, tuple))  # True，空元组
print(isinstance(b, tuple))  # False，b是整数
print(isinstance(c, tuple))  # False，c是列表
print(isinstance(d, tuple))  # True，只有一个元素的元组
print(isinstance(e, tuple))  # True，多个元素的元组
