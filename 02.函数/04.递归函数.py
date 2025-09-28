# 阶乘
def fact(n):
    # 终止条件 / 边界情形
    if n <= 1:
        return 1
    # 拆解规则 / 递归展开（规模收敛：n -> n-1）
    return n * fact(n - 1)


fact(5)


# 二分查找
def binary_search(arr, target, left, right):
    # 基本情况：如果左边界大于右边界，说明没找到
    if left > right:
        return -1
    # 计算中间位置
    # `//` 是整除（向下取整的除法，floor division）运算符
    mid = (left + right) // 2
    # 如果找到目标值，返回位置
    if arr[mid] == target:
        return mid
    # 如果中间值大于目标值，在左半部分查找
    if arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    # 如果中间值小于目标值，在右半部分查找
    return binary_search(arr, target, mid + 1, right)


# 测试函数
numbers = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
result = binary_search(numbers, target, 0, len(numbers) - 1)
print(f"数字{target}在列表中的位置是：{result}")
