import os

print("当前进程ID:", os.getpid())
# 这段代码在Windows系统下无法运行
# pid = os.fork()  # 创建子进程
# if pid == 0:
#     # 子进程返回0
#     print("我是子进程，ID:", os.getpid(), "父进程ID:", os.getppid())
# else:
#     # 父进程返回子进程ID
#     print("我创建了一个子进程，子进程ID:", pid)

import os
from multiprocessing import Process


# 子进程要执行的函数
def run_task(name):
    print("子进程运行中，名字：%s，进程ID：%s" % (name, os.getpid()))


if __name__ == "__main__":
    print("父进程ID：", os.getpid())
    p = Process(target=run_task, args=("任务1",))
    print("子进程即将启动")
    p.start()  # 启动子进程
    p.join()  # 等待子进程结束
    print("子进程已结束")

# 导入进程池模块
# 导入操作系统、时间和随机数模块
import os
import random
import time
from multiprocessing import Pool


# 定义工作函数，接收任务ID作为参数
def worker(task_id):
    # 打印当前执行的任务ID和进程ID
    print("执行任务 %s (进程ID: %s)" % (task_id, os.getpid()))
    # 随机休眠0-1秒，模拟任务执行时间
    time.sleep(random.random() * 1)
    # 打印任务完成信息
    print("任务 %s 完成" % task_id)


# 主程序入口
if __name__ == "__main__":
    # 打印父进程的进程ID
    print("父进程ID：", os.getpid())
    # 创建进程池，最多同时运行3个进程
    pool = Pool(3)  # 最多同时运行3个进程
    # 循环创建5个任务
    for i in range(5):
        # 异步提交任务到进程池
        pool.apply_async(worker, args=(i,))
    # 关闭进程池，不再接受新任务
    pool.close()  # 关闭进程池，不再接受新任务
    # 等待所有子进程结束
    pool.join()  # 等待所有子进程结束
    # 打印所有任务完成信息
    print("所有任务完成")

# 导入subprocess模块，用于执行外部命令
import subprocess

# 打印提示信息，告知用户即将运行nslookup命令
print("运行nslookup命令")
# 使用subprocess.call()方法执行nslookup命令，查询www.python.org的DNS信息
# call()方法会等待命令执行完成并返回退出状态码
result = subprocess.call(["nslookup", "www.python.org"])
# 打印命令的返回码，通常0表示成功，非0表示出错
print("命令返回码:", result)


# 导入多进程模块中的Process类和Queue队列类
# 导入操作系统接口模块和时间模块
import os
from multiprocessing import Process, Queue


# 定义写入数据的函数，参数q是队列对象
def write_data(q):
    # 遍历列表中的每个值
    for value in ["A", "B", "C"]:
        # 打印正在写入的值
        print("写入:", value)
        # 将值放入队列中
        q.put(value)
        # 暂停1秒
        time.sleep(1)


# 定义读取数据的函数，参数q是队列对象
def read_data(q):
    # 无限循环读取数据
    while True:
        # 从队列中获取数据，True表示阻塞等待
        value = q.get(True)
        # 打印读取到的值
        print("读取:", value)


# 主程序入口
if __name__ == "__main__":
    # 创建一个进程间通信的队列
    q = Queue()
    # 创建写入进程，目标函数是write_data，参数是队列q
    pw = Process(target=write_data, args=(q,))
    # 创建读取进程，目标函数是read_data，参数是队列q
    pr = Process(target=read_data, args=(q,))
    # 启动写入进程
    pw.start()
    # 启动读取进程
    pr.start()
    # 等待写入进程结束
    pw.join()
    # 强制终止读取进程（因为读进程是死循环，需要强制结束）
    pr.terminate()  # 读进程是死循环，强制结束
