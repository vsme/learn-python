# 定义一个自定义异常类，继承自Exception基类
class MyInputError(Exception):
    """自定义输入错误类型"""

    # 使用pass关键字表示类体为空，仅继承父类功能
    pass


# 定义一个检查正数的函数，接收一个数字参数
def check_positive(num):
    # 判断输入的数字是否小于等于0
    if num <= 0:
        # 主动抛出自定义异常
        # 使用raise关键字抛出自定义异常，并传递错误信息
        raise MyInputError("输入必须是正数！")
    # 如果数字为正数，则返回该数字
    return num


# 使用try-except语句处理可能出现的异常
try:
    # 调用check_positive函数，传入负数-5进行测试
    check_positive(-5)
# 捕获MyInputError类型的异常，并将异常对象赋值给变量e
except MyInputError as e:
    # 打印捕获到的自定义异常信息
    print("捕获到自定义异常：", e)


# 捕获后重新抛出异常
def func():
    try:
        1 / 0
    except ZeroDivisionError:
        print("这里先记录一下异常")
        raise  # 重新抛出异常


try:
    func()
except ZeroDivisionError:
    print("最终在这里处理异常")
