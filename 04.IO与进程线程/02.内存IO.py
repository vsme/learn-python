from io import BytesIO, StringIO

buf = StringIO()
buf.write("hello\nworld")
buf.seek(0)
print(buf.read())

b = BytesIO()
b.write(b"\x00\x01\x02")
print(len(b.getvalue()))

# 创建 BytesIO 对象
f = BytesIO()

# 写入二进制数据，注意要先把字符串编码成 bytes
f.write("你好，世界".encode("utf-8"))  # encode('utf-8') 把字符串转为字节

# 用 getvalue() 获取所有写入的字节内容
print(
    f.getvalue()
)  # 输出：b'\xe4\xbd\xa0\xe5\xa5\xbd\xef\xbc\x8c\xe4\xb8\x96\xe7\x95\x8c'
