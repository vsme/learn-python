import socket

# 创建TCP套接字
# AF_INET: 使用IPv4地址族
# SOCK_STREAM: 使用TCP协议
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接服务器
client.connect(("127.0.0.1", 8888))
# 发送数据
client.send(b"Hello, server!")
# 接收数据
data = client.recv(1024)
print("收到服务器回复：", data.decode("utf-8"))
# 关闭连接
client.close()
