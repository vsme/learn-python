import subprocess

# 运行命令并获取输出（以Windows的dir命令为例，Linux下可用ls）
result = subprocess.run("dir", shell=True, capture_output=True, text=True)

# 打印命令的输出内容
print("命令输出：")
print(result.stdout)

# 运行一个命令
result = subprocess.run("ping 127.0.0.1 -n 2", shell=True)

# 判断命令是否成功执行（返回码为0表示成功）
if result.returncode == 0:
    print("命令执行成功")
else:
    print("命令执行失败，返回码：", result.returncode)
