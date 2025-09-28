# 定义一个计算绝对值的函数
def my_abs(num):
    # 如果num大于等于0，直接返回num
    if num >= 0:
        return num
    # 否则返回-num
    else:
        return -num


# 调用函数，传入-8
print(my_abs(-8))  # 输出：8


# 多个返回值
def split_pair(s):
    return s[: len(s) // 2], s[len(s) // 2 :]


left, right = split_pair("abcd")  # 左右解包

print(left)  # 输出：ab
print(right)  # 输出：cd


# 定义一个什么都不做的函数
def do_nothing():
    pass  # pass表示占位，什么也不做 这样代码不会报错


# 定义一个只接受数字参数的绝对值函数
def safe_abs(x):
    # 检查x是不是整数或浮点数
    if not isinstance(x, (int, float)):
        raise TypeError("参数类型必须是数字")
    if x >= 0:
        return x
    else:
        return -x


# safe_abs("abc")  # 这一行会报TypeError: 参数类型必须是数字


# 定义一个函数，计算商品折扣后的价格
def calculate_discount(original_price, discount_rate):
    # 计算折扣金额
    discount_amount = original_price * discount_rate
    # 计算最终价格
    final_price = original_price - discount_amount
    # 返回折扣金额和最终价格
    return discount_amount, final_price


# 测试不同商品
# 一件原价100元的衣服，打8折
discount, price = calculate_discount(100, 0.2)  # 0.2表示20%的折扣
print(f"原价100元的衣服：")  # 原价100元的衣服：
print(f"折扣金额：{discount}元")  # 折扣金额：20.0元
print(f"最终价格：{price}元")  # 最终价格：80.0元

# 一双原价200元的鞋子，打7折
discount, price = calculate_discount(200, 0.3)  # 0.3表示30%的折扣
print(f"\n原价200元的鞋子：")  # 原价200元的鞋子：
print(f"折扣金额：{discount}元")  # 折扣金额：60.0元
print(f"最终价格：{price}元")  # 最终价格：140.0元
