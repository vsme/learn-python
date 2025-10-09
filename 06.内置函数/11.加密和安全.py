import hashlib

# 原始字符串
text = "hello world"

# 创建MD5哈希对象
md5 = hashlib.md5()
# 必须先将字符串编码为字节
md5.update(text.encode("utf-8"))
# 获取16进制的哈希值
print("MD5哈希值：", md5.hexdigest())
# 导入hashlib模块，用于计算各种哈希值

# 使用with语句打开文件，'rb'模式表示以二进制只读方式打开
# 打开文件，读取内容
with open("README.md", "rb") as f:
    # 创建一个SHA1哈希对象
    sha1 = hashlib.sha1()
    # 使用无限循环来分块读取文件内容，这样可以处理大文件而不会占用过多内存
    # 分块读取，适合大文件
    while True:
        # 每次读取1024字节的数据
        data = f.read(1024)
        # 如果读取到的数据为空，说明文件已经读取完毕
        if not data:
            # 跳出循环
            break
        # 将读取到的数据块更新到SHA1哈希对象中
        sha1.update(data)
    # 计算最终的SHA1哈希值并以十六进制字符串形式输出
    print("文件的SHA1哈希值：", sha1.hexdigest())

text = "python123"

# 计算MD5
md5 = hashlib.md5(text.encode("utf-8")).hexdigest()
print("MD5:", md5)

# 计算SHA1
sha1 = hashlib.sha1(text.encode("utf-8")).hexdigest()
print("SHA1:", sha1)

# 计算SHA256
sha256 = hashlib.sha256(text.encode("utf-8")).hexdigest()
print("SHA256:", sha256)

import hashlib
import hmac

# 消息内容
message = b"hello, world"
# 密钥（双方约定的“密码”）
key = b"my_secret_key"

# 创建HMAC对象，指定密钥和哈希算法
h = hmac.new(key, message, digestmod=hashlib.sha256)
# 获取16进制的HMAC值
print("HMAC签名：", h.hexdigest())


def verify_hmac(message, key, received_hmac):
    # 重新生成HMAC
    h = hmac.new(key, message, digestmod=hashlib.sha256)
    # 比较HMAC值
    return h.hexdigest() == received_hmac


# 假设收到如下数据
msg = b"hello, world"
key = b"my_secret_key"
received = hmac.new(key, msg, digestmod=hashlib.sha256).hexdigest()

# 校验
if verify_hmac(msg, key, received):
    print("数据未被篡改，校验通过")
else:
    print("数据被篡改，校验失败")


# 校验
if verify_hmac(msg + b"extra", key, received):
    print("数据未被篡改，校验通过")
else:
    print("数据被篡改，校验失败")
