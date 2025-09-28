# 使用 `python -m chapter03.mod01` 运行模块
# 可以直接导入 `utils.xyz` 模块
import utils  # 输出："初始化 utils"

print("version", utils.version)

from utils.xyz import world

print(world())

# 导入 utils.abc 模块
from utils.abc import hello

print(hello())
