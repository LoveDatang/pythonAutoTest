import unittest
from base.demo import testRequest


class TestMethod1(unittest.TestCase):

    # run运行时需要选择运行整个文件 并且 使用unittest.main()方法才能使得按照
    # setUpClass，setUp，test_01，tearDown，setUp，test_02，tearDown，tearDownClass的顺序执行

    # 在全部测试用例执行之前进行执行
    @classmethod
    def setUpClass(cls) -> None:
        print("test-setUpClass")

    # 在全部测试用例执行之后进行执行
    @classmethod
    def tearDownClass(cls) -> None:
        print("test-tearDownClass")

    # 在每个测试方法前进行执行
    def setUp(self) -> None:
        self.sendRequest = testRequest()
        print("test-setUp")

    # 在每个测试方法后进行执行
    def tearDown(self) -> None:
        print("test-tearDown")

    # 所有的测试用例都要以test开头，按照字母a-z,A-Z,0-9的顺序进行执行
    def test_01(self):
        print("这个是测试方法1")

    def test_02(self):
        print("这个是测试方法2")


if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTest(TestMethod1("test_01"))
    suite.addTest(TestMethod1("test_02"))
    runner = unittest.TextTestRunner()
    runner.run(suite)

# unittest的四大组件
# 1. test fixture setup,tearDown初始化测试用例和清理释放资源
# 2. test case 通过类继承unittest.TestCase来实现，每个测试用例函数名都需要用test开头
# 3. test suite 测试套件
# 4. test runner 运行器，通过和suite配合使用进行测试用例的执行
