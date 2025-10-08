def my_abs(n):
    """
    计算一个数的绝对值。

    示例：

    >>> my_abs(5)
    5
    >>> my_abs(-3)
    3
    >>> my_abs(0)
    0
    """
    # 如果n大于等于0，直接返回n，否则返回-n
    return n if n >= 0 else -n


# my_abs(5)


class EasyDict(dict):
    """
    一个可以用点号访问属性的字典。

    示例：

    >>> d = EasyDict()
    >>> d['foo'] = 123
    >>> d.foo
    123
    >>> d.bar = 456
    >>> d['bar']
    456
    >>> e = EasyDict(a=1, b=2)
    >>> e.a
    1
    >>> e['b']
    2
    >>> e['not_exist']
    Traceback (most recent call last):
        ...
    KeyError: 'not_exist'
    >>> e.not_exist
    Traceback (most recent call last):
        ...
    AttributeError: 'EasyDict' object has no attribute 'not_exist'
    """

    def __init__(self, **kwargs):
        # 初始化时，把所有关键字参数存到字典里
        super().__init__(**kwargs)

    def __getattr__(self, key):
        # 支持用点号访问属性
        try:
            return self[key]
        except KeyError:
            raise AttributeError(f"'EasyDict' object has no attribute '{key}'")

    def __setattr__(self, key, value):
        # 支持用点号赋值
        self[key] = value


def get_item(lst, idx):
    """
    获取列表指定位置的元素。

    >>> get_item([1, 2, 3], 1)
    2
    >>> get_item([1, 2, 3], 5)
    Traceback (most recent call last):
        ...
    IndexError: list index out of range
    """
    return lst[idx]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
