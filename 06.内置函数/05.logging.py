import logging  # 导入logging模块

# 记录一条信息
logging.info("这是一条普通信息")  # 默认不会显示，因为默认级别是WARNING

# 记录一条警告
logging.warning("这是一个警告信息")

# 记录一条错误
logging.error("这是一个错误信息")

# 配置日志输出格式和级别
logging.basicConfig(
    level=logging.INFO,  # 设置日志级别为INFO
    format="%(asctime)s - %(levelname)s - %(message)s",  # 设置输出格式
)

logging.info("程序启动")
logging.warning("警告：磁盘空间不足")
logging.error("错误：文件未找到")
