def countdown(n):
    while n > 0:
        yield n  # 产出一个值并“暂停”
        n -= 1  # 下次迭代从这里继续


for x in countdown(3):  # 3, 2, 1
    print(x)


# 把迭代“委托”出去
def flatten(nested):
    for row in nested:
        yield from row  # 等价于：for x in row: yield x


# 把递归改为生成器
def inorder(root):
    if root:
        yield from inorder(root.left)
        yield root.val
        yield from inorder(root.right)


# 生成器表达式
gen = (x * x for x in range(5))  # 惰性
list(gen)  # [0, 1, 4, 9, 16]

# 典型用法：和 `sum`、`any`、`all` 等“消费一次就完”的函数搭配：
total = sum(x * x for x in range(10_000_000))


# 管道示例
def read_lines(fp):
    for line in fp:
        yield line.rstrip("\n")


def filter_nonempty(lines):
    for s in lines:
        if s.strip():
            yield s


def to_ints(lines):
    for s in lines:
        yield int(s)


with open("text.txt", "r", encoding="utf-8") as f:
    for n in to_ints(filter_nonempty(read_lines(f))):
        print(n)


# 双向通信 & 控制
def accumulator():
    total = 0
    while True:
        x = yield total  # 接收 send() 过来的值
        if x is None:  # None 表示“只想读总计”
            continue
        total += x


gen = accumulator()
next(gen)  # 预激活 → 得到初始 total=0
gen.send(10)  # -> 10
gen.send(5)  # -> 15
gen.close()  # 结束
