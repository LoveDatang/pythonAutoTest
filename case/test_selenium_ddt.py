from selenium import webdriver
import unittest
import time
from ddt import ddt, data, unpack, file_data


# 理解下来，python程序想要看懂，需要加大量注释，因为它实在是太简洁了。（笑哭）
# 将参数文件中的内容放在一个list中，并且返回这个list
def read_file():
    param = []
    file_path = '../file/param1.txt'
    with (open(file_path)) as fp:
        for line in fp.readlines():
            param.append(line.strip('\n').split(','))
    return param


@ddt()
class TestSelenium(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome("../util/chromedriver")
        self.driver.get("http://www.baidu.com")

    #
    def tearDown(self) -> None:
        time.sleep(3)
        self.driver.quit()

    @data(1, 2, 3)
    def test_01(self, value):  # value用来接收data的数据
        print(value)

    # 通过ddt传入不同的参数，实现多次循环操作同一个测试用例
    # 多个参数用数据传递，账号密码数据量多可以调用excel
    @data('你好', '晓燕')
    def test_02(self, txt):
        self.driver.find_element_by_id('kw').send_keys(txt)
        self.driver.find_element_by_id("su").click()

    # 伪文件读取
    @data(*read_file())
    @unpack
    def test_03(self, txt1, txt2):
        self.driver.find_element_by_id('kw').send_keys(txt1)
        self.driver.find_element_by_id('kw').send_keys(txt2)
        self.driver.find_element_by_id("su").click()

    # 通过自己输入
    @data(("haha", "xixi"), ('fasd', 'fs'))
    @unpack
    def test_04(self, txt1, txt2):
        print("txt1:" + txt1)
        print("txt2:" + txt2)

    # 注意yml文件的格式，空格等
    @file_data('../file/testyml.yml')
    def test_05(self, **kwargs):
        print(kwargs.get("name"))
        print(kwargs.get("info"))

    def test_06(self):
        print("why")


if __name__ == '__main__':
    unittest.main()

# 被ddt装饰的函数想要用suite进行测试用例添加时，需要额外的测试用例名改写，比较繁琐，
# 所以一般用其他几种方法来操作运行即可

# 要明白ddt的解析过程，这样才能更好的使用
# ddt的使用（首先import后再class前面加@ddt）
# 1. @data，进行参数化
# 2. @data配合@unpack进行参数化,需要对文件中数据处理
# 3. @file_data引入参数化的文件，直接拿文件中数据应用
