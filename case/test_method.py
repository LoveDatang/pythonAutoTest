import json
import unittest
from TestRunner import HTMLTestRunner
from base.demo import testRequest
from mock.mock_demo import mock_test


# self用来调用它类里面本身的东西
class TestMethod(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("test_setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("test_tearDownClass")

    def setUp(self) -> None:
        self.sendRequest = testRequest()
        print("test-setUp")

    def tearDown(self) -> None:
        print("test-tearDown")

    def test_01(self):
        url2 = "https://api.binstd.com/shouji/query"
        data = {
            "appkey": "7b9b0b62d0f5551e",
            "shouji": "13916991486"
        }
        method = "post"
        # 不太理解这里
        response = self.sendRequest.choose_method_to_send(url2, method, data)
        # response.json()是将一个json数据转成一个字典
        # 格式化的打印json数据,intend可以控制显示json的格式，indent = 4是空4个格，ensure_ascii是不使用ascii，即可以显示中文
        print(json.dumps(response.json(), indent=4, ensure_ascii=False))
        # print("这个是测试方法1")
        print(type(response.json()))
        # 进行断言
        # assert方法成功没有任何返回，失败返回参数msg里面的内容
        # 为什么用self.assertEqual而不是直接用assertEqual不得而知
        self.assertEqual(response.json()["msg"], "ok", "如果fist，second不相同那就测试失败")
        # if (response.json()["msg"] == "ok"):
        #     print("测试成功")
        # else:
        #     print("测试失败")

    # 所有的测试用例都要以test开头
    # @unittest.skip('理由：不想执行')
    # 测试用例失败了也不承认是失败的。
    @unittest.expectedFailure
    def test_02(self):
        print("这个是测试方法2")

    @unittest.skip('test_03')
    def test_03(self):
        print("这个是测试方法3")

    # 1>2是false状态，所以skip没有生效
    @unittest.skipIf(1 < 2, "不对")
    def test_04(self):
        url2 = "https://api.binstd.com/shouji/query"
        data = {
            "appkey": "7b9b0b62d0f5551e",
            "shouji": "13916991486"
        }
        return_data = {
            "status": 0,
            "msg": "ok",
            "result": {
                "shouji": "13916991486",
                "province": "",
                "city": "",
                "company": "中国移动",
                "cardtype": None
            }
        }
        method = "post"
        # 不太理解这里
        res = mock_test(self.sendRequest.choose_method_to_send, data, url2, method, return_data)
        print(res)
        # mock_data = mock.Mock(return_value=data)
        # self.sendRequest.choose_method_to_send = mock_data
        # response = self.sendRequest.choose_method_to_send(url2, method, data)
        # print(response)
        print("这个是测试方法4")


if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTest(TestMethod("test_01"))
    suite.addTest(TestMethod("test_02"))
    suite.addTest(TestMethod("test_03"))
    suite.addTest(TestMethod("test_04"))
    unittest.TextTestRunner().run(suite)

    # filepath = "../report/result.html"
    # with 生成的是一个流 stream，作为HTMLTestRunner的第一个参数
    # with(open('../report/result.html', 'wb')) as fp:
    #     runner = HTMLTestRunner(stream=fp, title='<我的测试框架实践>的测试报告', description='总共4个测试用例，跳过了一个')
    #     runner.run(suite)

# 如何进行接口串联测试
# 1. 可以用一个case的返回值放在setUp的变量里面供其他case调用
# 2. 可以在一个case里面设置全局变量，但是要注意设置的全局变量一定要在被调用的case之前的case里面，因为unittest是按照函数名称排序执行的。

# 思考如何管理不同py文件的执行
# 四种skip

# suite
