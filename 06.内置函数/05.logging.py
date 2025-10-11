import logging  # 导入logging模块


# 定义颜色代码
class ColoredFormatter(logging.Formatter):
    """自定义彩色日志格式化器"""

    # ANSI颜色代码
    COLORS = {
        "DEBUG": "\033[36m",  # 青色
        "INFO": "\033[32m",  # 绿色
        "WARNING": "\033[33m",  # 黄色
        "ERROR": "\033[31m",  # 红色
        "CRITICAL": "\033[35m",  # 紫色
        "RESET": "\033[0m",  # 重置颜色
    }

    # \033[36m 是 ANSI 转义序列 （ANSI Escape Sequences），这是一种在终端中控制文本颜色和格式的标准方法。让我详细解释一下：
    # ANSI 转义序列的构成
    # 格式： \033[<参数>m
    # - \033 - 这是 ESC 字符的八进制表示（ASCII 码 27）
    # - [ - 左方括号，表示开始控制序列
    # - 36 - 颜色代码参数
    # - m - 表示这是一个颜色/样式控制命令
    # 前景色（文字颜色）：
    # - 30 - 黑色
    # - 31 - 红色
    # - 32 - 绿色
    # - 33 - 黄色
    # - 34 - 蓝色
    # - 35 - 紫色（洋红）
    # - 36 - 青色（蓝绿色）
    # - 37 - 白色
    # 背景色：
    # - 40-47 - 对应的背景色（比如 41 是红色背景）

    def format(self, record):
        # 获取原始格式化的消息
        log_message = super().format(record)
        # 只给级别名称添加颜色
        color = self.COLORS.get(record.levelname, self.COLORS["RESET"])
        colored_levelname = f"{color}{record.levelname}{self.COLORS['RESET']}"
        # 替换原始消息中的级别名称为彩色版本
        log_message = log_message.replace(record.levelname, colored_levelname)
        return log_message


# 创建logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # 改为DEBUG级别，这样所有级别的日志都会显示

# 日志级别从低到高排序：
# 1. DEBUG (10) - 最低级别
# 2. INFO (20)
# 3. WARNING (30)
# 4. ERROR (40)
# 5. CRITICAL (50) - 最高级别

# 创建控制台处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)  # 处理器级别也改为DEBUG

# 创建彩色格式化器
colored_formatter = ColoredFormatter(
    fmt="%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)

# 将格式化器添加到处理器
console_handler.setFormatter(colored_formatter)

# 将处理器添加到logger
logger.addHandler(console_handler)

# 记录一条信息
logging.info("这是一条普通信息")  # 现在会显示，因为级别设置为INFO

# 记录一条警告
logging.warning("这是一个警告信息")

# 记录一条错误
logging.error("这是一个错误信息")

# 添加更多示例来展示不同颜色
logging.debug("这是调试信息")  # 青色（需要将级别改为DEBUG才能看到）
logging.critical("系统崩溃")  # 紫色

# 创建一个日志统计报告
print("\n========== 日志统计报告 ==========")
levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
counts = [10, 20, 8, 2, 0]
total = sum(counts)

print("级别\t|数量\t|占比")
for level, count in zip(levels, counts):
    percentage = (count / total * 100) if total > 0 else 0
    print(f"{level}\t|{count}\t|{percentage:.1f}%")
print(f"总计\t|{total}\t|100.0%")
print("=" * 35)
