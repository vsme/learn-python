import re

# 1) 查找
text = "2023-08-20 is a date, and 2024-01-01 is also a date."
m = re.search(r"\d{4}-\d{2}-\d{2}", text)  # 找第一个匹配
if m:
    m.group(0)   # 整个匹配
    m.start(), m.end()

# 2) 全部匹配
all_dates = re.findall(r"\d{4}-\d{2}-\d{2}", text)

# 3) 迭代匹配（更省内存 & 有位置信息）
for m in re.finditer(r"\b\w+\b", text):
    print(m.group(), m.span())

# 4) 替换
re.sub(r"\s+", " ", text)                   # 多空白折叠为单空格
s = "123-456-7890"
print('s', s)
re.sub(r"(\d{3})-(\d{4})", r"\1 \2", s)     # 用分组反向引用

# 5) 分割
re.split(r"[,\s]+", "a,  b   c")            # -> ['a','b','c']

# 6) 预编译（频繁使用时更快）
pat = re.compile(r"\b([A-Za-z]+)=(\d+)\b")
pat.search(text)

print(re.findall(r"[^abc]+", "abz1cxy")) # ['z1', 'xy']

s = "scatter catalog cat"
print(re.findall(r"\Bcat\B", s)) # 左右都在“单词内部”

s = "10kg 12g 8kg"
re.findall(r"\d+(?=kg)", s)  # ['10', '8']
# 解释：匹配的结果是数字本身；先行断言只检查“后面是不是 kg”。

s = "abc abc1 ab12 xyz"
re.findall(r"\b[a-zA-Z]+\b(?!\d)", s)  # ['abc', 'xyz']
# 解释：\b[a-zA-Z]+\b 是独立的字母词；(?!\d) 要求其后面不是数字。

s = "pay $12 and $3.5, not 7 or $x"
re.findall(r"(?<=\$)\d+(?:\.\d+)?", s)  # ['12', '3.5']
# 解释：只把数字取出来；(?<=\$) 确保数字前面是美元符号。

s = "visit example.com, mail a@foo.example.com"
re.findall(r"(?<!@)\bexample\.com\b", s)  # ['example.com']
# 解释：如果前面是 @（出现在邮箱里），就被排除。