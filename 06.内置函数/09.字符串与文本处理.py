import re

# 判断字符串是否是手机号（以1开头，11位数字）
phone = "13812345678"
pattern = r"^1\d{10}$"  # 正则表达式：1开头，后面10个数字
if re.match(pattern, phone):
    print("手机号格式正确")
else:
    print("手机号格式不正确")

# 提取字符串中的所有数字
text = "小明今年18岁，身高175cm"
numbers = re.findall(r"\d+", text)  # 匹配所有连续数字
print("提取到的数字：", numbers)
# 提取到的数字： ['18', '175']

# 把字符串中的数字全部替换为X
text = "房间号：308，电话：123456"
new_text = re.sub(r"\d+", "X", text)
print("替换后的文本：", new_text)
# 替换后的文本： 房间号：X，电话：X

import string

# 获取所有小写字母
print("小写字母：", string.ascii_lowercase)
# 小写字母： abcdefghijklmnopqrstuvwxyz
# 获取所有大写字母
print("大写字母：", string.ascii_uppercase)
# 大写字母： ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 获取所有数字字符
print("数字字符：", string.digits)
# 数字字符： 0123456789

# 用f-string格式化字符串（推荐）
name = "小明"
age = 18
print(f"大家好，我是{name}，今年{age}岁。")

# 用str.format格式化字符串
print("大家好，我是{}，今年{}岁。".format(name, age))


import textwrap

# 一段很长的文本
long_text = "Python是一门非常流行的编程语言。它语法简洁，功能强大，应用广泛。"

# 自动换行，每行最多20个字符
wrapped = textwrap.fill(long_text, width=20)
print(wrapped)

# 带有缩进的多行文本
text = """
    这是第一行。
        这是第二行，有更多缩进。
    这是第三行。
"""

# 去除所有行的多余缩进
dedented = textwrap.dedent(text)
print(dedented)

import difflib

text1 = "Python是一门很棒的语言。"
text2 = "Python是一门非常棒的语言！"

# 生成差异对比
diff = difflib.ndiff(text1, text2)
print("\n".join(diff))

text1 = """Python是一门很棒的语言。
适合新手学习。"""
text2 = """Python是一门非常棒的语言！
适合零基础新手学习。"""

# 生成HTML格式的差异报告
d = difflib.HtmlDiff()
html = d.make_file(text1.splitlines(), text2.splitlines())
with open("diff_report.html", "w", encoding="utf-8") as f:
    f.write(html)
print("差异报告已生成：diff_report.html")
