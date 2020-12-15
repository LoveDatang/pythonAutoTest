import json
import unittest
from base.demo import testRequest


class TestMethod1(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("类执行之前的方法")

    # 类执行后的方法为什么不在类执行后进行调用呢？
    @classmethod
    def tearDownClass(cls) -> None:
        print("类执行之后的方法")

    # 在每个测试方法前进行执行
    def setUp(self) -> None:
        self.sendRequest = testRequest()
        print("test-setUp")

    # 在每个测试方法后进行执行
    def tearDown(self) -> None:
        print("test-tearDown")

    # 所有的测试用例都要以test开头
    def test_01(self):
        print("这个是测试方法3")

    def test_02(self):
        print("这个是测试方法3")
