import json

# 定义一个Python字典
data = {"name": "小明", "age": 18, "score": [90, 85, 92]}

# 将Python对象转换为JSON字符串
json_str = json.dumps(data, ensure_ascii=False)  # ensure_ascii=False可以输出中文
print("转换后的JSON字符串：", json_str)

# 定义一个JSON格式的字符串
json_str = '{"name": "小明", "age": 18, "score": [90, 85, 92]}'

# 将JSON字符串转换为Python对象
data = json.loads(json_str)
print("转换后的Python对象：", data)

# 写入JSON文件
data = {"city": "北京", "temp": 25}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)

# 读取JSON文件
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
    print("从文件读取的数据：", loaded)

# 导入csv模块，用于处理CSV格式的文件
import csv

# 准备要写入CSV文件的数据，使用二维列表结构
# 第一行是表头，后面的行是具体的学生数据
rows = [
    # 表头行，定义各列的名称
    ["姓名", "年龄", "成绩"],
    # 第一个学生的信息：姓名、年龄、成绩
    ["小明", 18, 90],
    ["小红", 17, 95],
]

# 使用with语句打开文件，确保文件会被正确关闭
# 'w'表示写入模式，newline=''防止出现空行，encoding='utf-8'确保中文正确显示
with open("students.csv", "w", newline="", encoding="utf-8") as f:
    # 创建CSV写入器对象，用于将数据写入文件
    writer = csv.writer(f)
    # 一次性写入所有行数据到CSV文件
    writer.writerows(rows)
# 打印提示信息，告知用户文件写入操作已完成
print("CSV文件写入完成")

# 读取CSV文件
with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print("读取到一行：", row)

import configparser

# 创建配置解析器对象
config = configparser.ConfigParser()

# 添加内容
config["DEFAULT"] = {"username": "admin", "password": "123456"}
config["server"] = {"host": "localhost", "port": "8080"}

# 写入到文件
with open("config.ini", "w", encoding="utf-8") as f:
    config.write(f)
print("配置文件写入完成")

# 读取配置文件
config.read("config.ini", encoding="utf-8")

# 获取DEFAULT区的username
print("用户名：", config["DEFAULT"]["username"])

# 获取server区的host和port
print("服务器地址：", config["server"]["host"])
print("服务器端口：", config["server"]["port"])

import pickle

# 定义一个Python对象
data = {"name": "小明", "age": 18, "score": [90, 85, 92]}

# 序列化并写入文件
with open("data.pkl", "wb") as f:  # 注意用二进制写入
    pickle.dump(data, f)
print("对象已序列化保存")

# 从文件读取并反序列化
with open("data.pkl", "rb") as f:
    loaded = pickle.load(f)
    print("反序列化得到的对象：", loaded)
