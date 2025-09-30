# 写入文件操作
# 使用with语句以写入模式打开test.txt文件，会覆盖原有内容
with open("test.txt", "w") as f:  # 以写入模式打开文件
    # 向文件中写入指定的字符串内容
    f.write("Hello, world!")  # 写入文件内容

# 读取文件操作
# 使用with语句以只读模式打开test.txt文件，确保文件会被正确关闭
with open("test.txt", "r") as f:  # 以只读模式打开文件
    # 读取文件的全部内容并存储到content变量中
    content = f.read()  # 读取文件内容
    # 将读取到的文件内容打印到控制台
    print(content)  # 打印文件内容

# 追加文件操作
# 使用with语句以追加模式打开test.txt文件，在文件末尾添加内容
with open("test.txt", "a") as f:  # 以追加模式打开文件
    # 在文件末尾追加换行符和新的字符串内容
    f.write("\nHello, world!2")  # 追加文件内容

with open("test.txt", "rb") as f:
    f.seek(-4, 2)  # 定位到文件末尾前4字节
    print(f.read(4))  # b'ld!2'

# JSON（文本、可读性好）
import json

data = {"user": "Alice", "score": 95}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("data.json", "r", encoding="utf-8") as f:
    data2 = json.load(f)

# CSV
import csv

rows = [{"name": "A", "age": 20}, {"name": "B", "age": 30}]
with open("people.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerows(rows)

# Pickle（二进制序列化，**只用于可信数据源**）
import pickle

obj = {"x": 1}
with open("obj.pkl", "wb") as f:
    pickle.dump(obj, f)

with open("obj.pkl", "rb") as f:
    obj2 = pickle.load(f)  # 警告：加载不可信来源文件有安全风险
