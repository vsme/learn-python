# 定义一个学生类
class Student:
    count = 0  # 类属性，用于统计学生人数
    name = "Student"

    def __init__(self, name):
        self.name = name  # 实例属性，每个学生可以有不同的名字
        Student.count += 1  # 每创建一个学生，count加1


# 创建学生对象
student1 = Student("小明")  # 创建学生对象
student2 = Student("小红")  # 创建学生对象
print(Student.count)  # 输出: 2
print(student1.count)  # 输出: 2
print(student1.name)  # 输出: 小明
print(Student.name)  # 输出: Student


# 定义一个银行账户类
class BankAccount:
    interest_rate = 0.05  # 类属性，所有账户共享的利率

    def __init__(self, balance):
        self.balance = balance  # 实例属性，每个账户可以有不同的余额

    def add_interest(self):
        self.balance += self.balance * self.interest_rate  # 添加利息


# 创建银行账户对象
account1 = BankAccount(1000)  # 创建银行账户对象
account2 = BankAccount(2000)  # 创建银行账户对象
account1.add_interest()  # 添加利息
account2.add_interest()  # 添加利息
print(account1.balance)  # 输出: 1050.0
print(account2.balance)  # 输出: 2100.0

print(len((1, 2)))
