import unittest  # 导入unittest模块

from mydict import MyDict  # 假设上面的类保存在mydict.py文件中


# 定义一个测试类，继承自unittest.TestCase
class TestMyDict(unittest.TestCase):
    def test_init(self):
        # 测试初始化和属性访问
        d = MyDict(a=1, b="hello")
        self.assertEqual(d.a, 1)  # 检查属性a的值
        self.assertEqual(d.b, "hello")  # 检查属性b的值
        self.assertTrue(isinstance(d, dict))  # 检查d是否是dict的子类

    def test_key_access(self):
        # 测试通过key访问和赋值
        d = MyDict()
        d["x"] = 100
        self.assertEqual(d.x, 100)  # 检查属性x的值

    def test_attr_set(self):
        # 测试通过属性赋值
        d = MyDict()
        d.y = 200
        self.assertIn("y", d)  # 检查字典里是否有'y'
        self.assertEqual(d["y"], 200)  # 检查key为'y'的值

    def test_key_error(self):
        # 测试访问不存在的key时抛出KeyError
        d = MyDict()
        # 使用with self.assertRaises(KeyError)来检查是否抛出了KeyError异常
        with self.assertRaises(KeyError):
            _ = d["not_exist"]

    def test_attr_error(self):
        # 测试访问不存在的属性时抛出AttributeError
        d = MyDict()
        with self.assertRaises(AttributeError):
            _ = d.not_exist

    def setUp(self):
        # 每个测试方法运行前都会执行这里的代码
        print("准备测试环境...")

    def tearDown(self):
        # 每个测试方法运行后都会执行这里的代码
        print("清理测试环境...")


if __name__ == "__main__":
    unittest.main()  # 运行所有测试
