import socket

# 创建TCP套接字
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定IP和端口
server.bind(("127.0.0.1", 8888))
# 开始监听 1指的是最大连接数
server.listen(1)
print("服务器已启动，等待连接...", server.getsockname())

# 接受客户端连接
conn, addr = server.accept()
print("连接来自：", addr)
# 接收数据
data = conn.recv(1024)
print("收到客户端数据：", data.decode("utf-8"))
# 发送回复
conn.send(b"Hello, client!")
# 关闭连接
conn.close()
server.close()
