# 导入线程模块，用于创建和管理线程
import threading
import time

# 导入时间模块，用于线程休眠


# 定义工作函数，作为线程的执行目标
def worker():
    # 打印当前线程开始执行的信息
    print("线程 %s 开始" % threading.current_thread().name)
    # 让当前线程休眠2秒，模拟耗时操作
    time.sleep(2)
    # 打印当前线程结束执行的信息
    print("线程 %s 结束" % threading.current_thread().name)


# 主程序入口
if __name__ == "__main__":
    # 创建第一个线程对象，指定目标函数为worker，线程名为Worker-1
    t1 = threading.Thread(target=worker, name="Worker-1")
    # 创建第二个线程对象，指定目标函数为worker，线程名为Worker-2
    t2 = threading.Thread(target=worker, name="Worker-2")
    # 启动第一个线程
    t1.start()
    # 启动第二个线程
    t2.start()
    # 等待第一个线程执行完毕
    t1.join()
    # 等待第二个线程执行完毕
    t2.join()
    # 所有线程都结束后，打印完成信息
    print("所有线程结束")


# 定义共享变量，初始值为0
counter = 0


# 定义加法函数
def add():
    # 声明使用全局变量counter
    global counter
    # 循环100000次，每次将counter加1
    for _ in range(100000):
        counter += 1


# 定义减法函数
def subtract():
    # 声明使用全局变量counter
    global counter
    # 循环100000次，每次将counter减1
    for _ in range(100000):
        counter -= 1


# 创建第一个线程，目标函数为add
t1 = threading.Thread(target=add)
# 创建第二个线程，目标函数为subtract
t2 = threading.Thread(target=subtract)
# 启动第一个线程
t1.start()
# 启动第二个线程
t2.start()
# 等待第一个线程执行完毕
t1.join()
# 等待第二个线程执行完毕
t2.join()
# 打印最终counter的值
print("最终counter的值：", counter)


counter = 0
lock = threading.Lock()


def add():
    global counter
    for _ in range(100000):
        with lock:  # 临界区
            counter += 1


def subtract():
    global counter
    for _ in range(100000):
        with lock:  # 临界区
            counter -= 1


t1 = threading.Thread(target=add)
t2 = threading.Thread(target=subtract)
t1.start()
t2.start()
t1.join()
t2.join()
print("最终counter的值：", counter)  # 现在应稳定为 0

# 导入线程和多进程模块
import multiprocessing
import threading


# 定义一个忙等待函数，用于占用CPU资源
def busy_loop():
    # 创建无限循环
    while True:
        pass  # 死循环，占用CPU


# 启动和CPU核心数一样多的线程
# 遍历CPU核心数量
for i in range(multiprocessing.cpu_count()):
    # 创建新线程，目标函数为busy_loop
    t = threading.Thread(target=busy_loop)
    # 启动线程
    # t.start()

# 导入线程模块
import threading

# 创建一个全局的ThreadLocal对象
local_data = threading.local()


# 定义处理数据的函数
def process_data():
    # 直接访问local_data的属性，相当于访问当前线程自己的数据
    value = local_data.value
    # 打印当前线程名称和读取到的值
    print("线程 %s 读取到 value = %s" % (threading.current_thread().name, value))


# 定义线程任务函数
def thread_task(val):
    # 给当前线程绑定一个value属性
    local_data.value = val
    # 调用处理数据函数
    process_data()


# 创建两个线程，分别绑定不同的数据
# 创建第一个线程，目标函数为thread_task，参数为'苹果'，线程名为'线程A'
t1 = threading.Thread(target=thread_task, args=("苹果",), name="线程A")
# 创建第二个线程，目标函数为thread_task，参数为'香蕉'，线程名为'线程B'
t2 = threading.Thread(target=thread_task, args=("香蕉",), name="线程B")
# 启动第一个线程
t1.start()
# 启动第二个线程
t2.start()
# 等待第一个线程执行完毕
t1.join()
# 等待第二个线程执行完毕
t2.join()

# 创建ThreadLocal对象
user_local = threading.local()


def show_user():
    # 直接读取当前线程的user属性
    print("当前线程：%s，用户：%s" % (threading.current_thread().name, user_local.user))


def login(user_name):
    # 给当前线程绑定user属性
    user_local.user = user_name
    show_user()


# 启动两个线程，分别绑定不同的用户
t1 = threading.Thread(target=login, args=("Alice",), name="登录线程1")
t2 = threading.Thread(target=login, args=("Bob",), name="登录线程2")
t1.start()
t2.start()
t1.join()
t2.join()
