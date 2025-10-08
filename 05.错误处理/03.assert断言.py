# def calculate_average(score_str):
#     # 将字符串转为整数
#     score = int(score_str)
#     # 打印score的值，方便调试
#     print("当前分数为：", score)
#     # 计算平均分
#     return 100 / score


# def main():
#     # 这里传入字符串'0'，会导致后面出错
#     calculate_average("0")


# main()

# 断言适合用来检查那些“理论上不应该出错”的地方，帮助我们提前发现潜在问题。
def calculate_average(score_str):
    score = int(score_str)
    # 断言分数不能为0，否则会报错
    assert score != 0, "分数不能为0！"
    return 100 / score


def main():
    calculate_average("0")


main()
