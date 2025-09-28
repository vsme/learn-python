# 位置参数（positional-only）
def calculate_area(length, width):
    """
    计算矩形面积
    length: 长度
    width: 宽度
    """
    return length * width  # 返回长度乘以宽度的结果


# 调用函数
print(calculate_area(5, 3))  # 输出：15


# / 分隔符
def f(a, b, /, c, d):
    print(a, b, c, d)


f(1, 2, 3, 4)  # ✅ 都用位置传
f(1, 2, c=3, d=4)  # ✅ c、d 可关键字传
# f(a=1, b=2, c=3, d=4)  # ❌ TypeError：a、b 是仅限位置

# 命名关键字参数（keyword-only parameters）


# 调用时必须用“参数名=值”的形式传入，不能当位置参数传。
def f(x, *, a, b=0):
    print(x, a, b)


f(10, a=1, b=2)  # ✅
# f(10, 1, 2)       # ❌ TypeError：a/b 必须用关键字传


# 可以和 `*args` 一起用
def g(*args, a, b=0):
    print(args, a, b)


g(1, 2, a=3)  # args=(1,2), a=3, b=0

# 可变位置参数（var-positional） → `*args`


def sum_all(*nums):
    return sum(nums)


sum_all(1, 2, 3)  # 6
sum_all()  # 0（空元组）

# 位置不确定 → 用 `*args`
# 关键字不确定 → 用 `**kwargs`
# 既有固定参数、又想允许“更多” → 组合使用
# 还想限制/命名某些关键字 → 配合命名关键字参数


# 综合使用示例
def api_call(endpoint, /, *path_params, method="GET", timeout=5, **query):
    """
    endpoint      位置仅限参数（/ 前）
    *path_params  不定数量的位置片段
    method/timeout  命名关键字参数（必须用名字传）
    **query       任意数量的关键字参数（作为查询串）
    """
    print(endpoint, path_params, method, timeout, query)


api_call("/v1/user", 25, method="POST", timeout=3, sort="desc", limit=10)
# 输出：
# /v1/user (25,) POST 3 {'sort': 'desc', 'limit': 10}
