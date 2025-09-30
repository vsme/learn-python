import pickle  # 导入pickle模块

# 创建一个字典对象
person = {"name": "Alice", "age": 25, "score": 90}

# 使用pickle.dumps()将对象序列化为bytes
data_bytes = pickle.dumps(person)
print(data_bytes)  # 输出一串二进制内容，不是人能直接读懂的

data = {"user": "Alice", "scores": [95, 88, 76]}

# 保存到文件
with open("data.pkl", "wb") as f:  # 二进制写
    pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)

# 从文件读取
with open("data.pkl", "rb") as f:  # 二进制读
    obj = pickle.load(f)
    print(obj)

# 直接得到/还原字节串（不落盘）
b = pickle.dumps(data, protocol=pickle.HIGHEST_PROTOCOL)
obj2 = pickle.loads(b)
print(obj2)

import json  # 导入json模块

# 创建一个字典对象
student = {"name": "Tom", "age": 18, "score": 95}

# 使用json.dumps()将对象转为JSON格式的字符串
json_str = json.dumps(student)
print(json_str)  # 输出：{"name": "Tom", "age": 18, "score": 95}

# 一个JSON格式的字符串
data = '{"name": "Tom", "age": 18, "score": 95}'

# 使用json.loads()将字符串转为Python对象
student_obj = json.loads(data)
print(student_obj)  # 输出：{'name': 'Tom', 'age': 18, 'score': 95}

# 创建一个学生字典，包含姓名、年龄和分数信息
student = {"name": "Alice", "age": 25, "score": 90, "is_student": True}
# 保存到文件
# 以写入模式打开student.json文件，设置UTF-8编码
with open("student.json", "w", encoding="utf-8") as f:
    # 将学生字典直接写入JSON文件
    json.dump(student, f)  # 直接写入文件

# 从文件读取
# 以读取模式打开student.json文件，设置UTF-8编码
with open("student.json", "r", encoding="utf-8") as f:
    # 从JSON文件中加载数据到变量
    loaded_student = json.load(f)
    # 打印读取到的学生信息
    print(loaded_student)


# 定义一个学生类
class Student:
    # 初始化方法，接收姓名、年龄和分数参数
    def __init__(self, name, age, score):
        # 设置学生姓名属性
        self.name = name
        # 设置学生年龄属性
        self.age = age
        # 设置学生分数属性
        self.score = score


# 创建一个学生对象
# 创建名为Lily、年龄19、分数88的学生实例
stu = Student("Lily", 19, 88)


# 定义一个转换函数，把Student对象变成字典
# 定义将Student对象转换为字典的函数
def student_to_dict(obj):
    # 返回包含学生信息的字典
    return {"name": obj.name, "age": obj.age, "score": obj.score}


# 序列化时传入default参数
# 使用json.dumps将学生对象序列化为JSON字符串，指定转换函数
json_str = json.dumps(stu, default=student_to_dict)
# 打印序列化后的JSON字符串
print(json_str)  # 输出：{"name": "Lily", "age": 19, "score": 88}


# 反序列化时用object_hook参数把字典转回Student对象
# 定义将字典转换为Student对象的函数
def dict_to_student(d):
    # 根据字典中的数据创建并返回Student对象
    return Student(d["name"], d["age"], d["score"])


# 使用json.loads将JSON字符串反序列化为Student对象，指定转换函数
stu_obj = json.loads(json_str, object_hook=dict_to_student)
# 打印反序列化后的学生对象的属性
print(stu_obj.name, stu_obj.age, stu_obj.score)  # 输出：Lily 19 88
