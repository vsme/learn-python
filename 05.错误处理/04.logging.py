import logging

# 设置日志输出级别为INFO
logging.basicConfig(level=logging.INFO)


def calculate_average(score_str):
    # 将字符串转换为整数
    score = int(score_str)
    # 用logging记录调试信息
    logging.info("分数已转换为整数：%d", score)
    # 计算平均分
    return 100 / score


def main():
    calculate_average("0")


main()
