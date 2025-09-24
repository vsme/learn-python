# 假设有一个学生名单
students = ["小明", "小红", "小刚"]
# 用for循环依次打印每个学生的名字
for student in students:
    print(student)  # 每次循环，student变量会依次等于列表中的每个名字
    
# 计算1到10的累加和
total = 0  # 用于累加的变量
# 使用range()函数生成1到10的整数序列
# range()函数可以生成一个整数序列，包含从开始到结束（不包含结束）的整数
# 例如，range(1, 11)会生成1到10的整数序列
# range(5) 会生成0到4的整数序列 [0, 1, 2, 3, 4]
for number in range(1, 11):
    total += number  # 每次循环把当前数字加到total上
print("1到10的和是：", total)  # 输出：1到10的和是：55

# for循环可用于循环字符串
for char in "Hello":
    print(char)

# 打印1到100，但遇到第一个能被7整除的数就停止
for i in range(1, 101):
    if i % 7 == 0:  # 如果i能被7整除
        print("遇到第一个能被7整除的数：", i)
        break  # 立即结束整个循环
    print(i)

# 打印1到10中的所有奇数
for i in range(1, 11):
    if i % 2 == 0:  # 如果是偶数
        continue    # 跳过本次循环，后面的print不会执行
    print(i)        # 只会打印奇数

print(list(range(5, 1, -1)))