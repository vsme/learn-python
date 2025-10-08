import argparse

parser = argparse.ArgumentParser(description="示例：读取配置并处理输入文件")
parser.add_argument("-f", "--config", required=True, help="配置文件路径")
parser.add_argument("--verbose", action="store_true", help="开启详细日志")
parser.add_argument("-n", "--name", required=True, help="你的名字")
parser.add_argument("-a", "--age", type=int, required=True, help="你的年龄")
parser.add_argument("inputs", nargs="+", help="要处理的输入文件")

args = parser.parse_args()

print("config =", args.config)
print("verbose =", args.verbose)
print("name =", args.name, "age =", args.age)
print("inputs =", args.inputs)

# python 06.内置函数/04.demo_argparse.py -f config.txt --verbose -n 张三 -a 20 input1.txt input2.txt
# config = config.txt
# verbose = True
# name = 张三 age = 20
# inputs = ['input1.txt', 'input2.txt']
