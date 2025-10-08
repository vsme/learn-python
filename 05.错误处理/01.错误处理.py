# 即使发生异常，文件也会被正确关闭。
try:
    file = open("test.txt", "w")  # 打开文件
    file.write("Hello, world!")
    # 故意制造一个异常
    1 / 0
except ZeroDivisionError:
    print("除零错误！")
finally:
    # 无论是否出错，这里都会执行
    file.close()
    print("文件已关闭")

# 可以针对不同的错误给出不同的提示
try:
    # 获取用户输入并转换为整数，可能抛出ValueError异常
    num = int(input("请输入一个整数："))  # 可能输入非数字
    # 执行除法运算，可能抛出ZeroDivisionError异常
    result = 10 / num  # 可能除以0
# 捕获值错误异常（输入的不是有效数字时）
except ValueError:
    # 输出错误提示信息
    print("输入的不是有效的整数！")
# 捕获零除错误异常（除数为0时）
except ZeroDivisionError:
    # 输出错误提示信息
    print("不能除以0！")
# 如果try块中没有发生任何异常，则执行else块
else:
    # 如果没有发生异常，会执行这里
    # 输出计算结果
    print("计算结果是：", result)
# 无论是否发生异常，finally块都会被执行
finally:
    # 输出程序结束提示
    print("程序结束。")


def func1():
    return 10 / 0  # 这里会抛出异常


def func2():
    return func1()  # 异常会传递到这里


try:
    func2()  # 在这里捕获异常
except ZeroDivisionError as e:
    print("捕获到异常：", e)


def a():
    return 1 / 0  # 这里出错


def b():
    return a()


def c():
    return b()


# c()  # 没有捕获异常，Python会输出完整的错误信息

import logging  # 导入日志模块

try:
    10 / 0  # 故意制造异常
except Exception:
    # 记录异常信息到日志
    logging.error("程序出错了：", exc_info=True)

print("程序继续运行")
