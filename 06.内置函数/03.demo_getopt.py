import getopt
import sys

opts, args = getopt.getopt(sys.argv[1:], "f:n:a:", ["verbose"])
# 解析键值到变量
config = None
name = None
age = None
verbose = False

for opt, val in opts:
    if opt == "-f":
        config = val
    elif opt == "-n":
        name = val
    elif opt == "-a":
        age = int(val)
    elif opt == "--verbose":
        verbose = True

inputs = args  # 剩余的位置参数

print("config =", config)
print("verbose =", verbose)
print("name =", name, "age =", age)
print("inputs =", inputs)

# python 06.内置函数/03.demo_getopt.py -f config.txt --verbose -n 张三 -a 20 input1.txt input2.txt
# config = config.txt
# verbose = True
# name = 张三 age = 20
# inputs = ['input1.txt', 'input2.txt']
