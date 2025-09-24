age = 21  # 定义一个变量age，表示年龄

# 基础语法
if age >= 18:  # 如果年龄大于等于18
    print("你已经成年啦！")  # 满足条件时执行
    print("可以独立做很多事情。")  # 这行也会被执行
# 如果age小于18，这两行不会被执行

# elif 用法
score = 72

if score >= 90:
    print("优秀")
elif score >= 75:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
# 程序会从上往下判断，遇到第一个满足条件的分支就执行，然后跳过后面的分支


# 小明的身高和体重
height = 1.75  # 单位：米
weight = 80.5  # 单位：千克

# 计算BMI指数，公式：体重 / (身高的平方)
bmi = weight / (height ** 2)
print(f"小明的BMI指数为：{bmi:.2f}")  # 保留两位小数

# 根据BMI指数判断健康状况
if bmi < 18.5:
    print("体重过轻")
elif bmi < 25:
    print("体重正常")
elif bmi < 28:
    print("体重偏重")
elif bmi < 32:
    print("肥胖")
else:
    print("严重肥胖")

# 如果用户输入的不是数字，int()会报错
user_input = input("请输入一个数字：")
try:
    number = int(user_input)  # 尝试转换为整数
    print("你输入的数字是：", number)
except ValueError:
    print("输入的内容不是有效的数字，请重新输入。")