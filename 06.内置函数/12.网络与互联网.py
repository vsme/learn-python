from urllib import parse, request

# 发送GET请求，获取网页内容
response = request.urlopen("https://www.example.com")
# 读取网页内容（字节类型）
html = response.read()
# 将字节内容解码为字符串
print("网页内容：", html.decode("utf-8"))

url = "https://www.example.com/search?q=python&lang=zh"
# 解析URL为各部分
result = parse.urlparse(url)
print("协议：", result.scheme)
print("主机：", result.netloc)
print("路径：", result.path)
print("查询参数：", result.query)

# 字典转为URL参数字符串
params = {"q": "python", "lang": "zh"}
query_str = parse.urlencode(params)
print("编码后的参数：", query_str)

# URL参数字符串转为字典
parsed = parse.parse_qs("q=python &lang=zh")
print("解码后的参数：", parsed)

import http.client

# 创建HTTP连接对象
conn = http.client.HTTPSConnection("www.example.com")
# 发送GET请求
conn.request("GET", "/")
# 获取响应
response = conn.getresponse()
print("状态码：", response.status)
print("响应内容：", response.read().decode("utf-8"))
# 关闭连接
conn.close()

# 创建一个HTTPS连接对象，连接到www.example.com服务器
conn = http.client.HTTPSConnection("www.example.com")
# 定义要发送的POST数据，格式为URL编码的字符串
params = "name=Tom&age=18"
# 设置HTTP请求头，指定内容类型为表单数据格式
headers = {"Content-type": "application/x-www-form-urlencoded"}
# 发送POST请求到/submit路径，包含参数和请求头
conn.request("POST", "/submit", params, headers)
# 获取服务器的响应对象
response = conn.getresponse()
# 读取响应内容并解码为UTF-8格式，然后打印输出
print("POST响应内容：", response.read().decode("utf-8"))
# 关闭HTTP连接，释放资源
conn.close()

from email.mime.text import MIMEText

# 邮件内容
msg = MIMEText("你好，这是一封测试邮件。", "plain", "utf-8")
# 发件人、收件人、主题
msg["From"] = "from@qq.com"
msg["To"] = "to@qq.com"
msg["Subject"] = "测试邮件"

# 连接QQ邮箱SMTP服务器并登录
# server = smtplib.SMTP_SSL("smtp.qq.com", 465)
# server.login("from@qq.com", "your_password")
# 发送邮件
# server.sendmail("from@qq.com", ["to@qq.com"], msg.as_string())
# 关闭连接
# server.quit()
print("邮件发送成功")
