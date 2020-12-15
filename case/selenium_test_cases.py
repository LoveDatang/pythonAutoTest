from selenium import webdriver
import unittest
import time
# ddt要自己安装
from ddt import ddt, data, unpack, file_data


# 理解下来，python程序想要看懂，需要加大量注释，因为它实在是太简洁了。（笑哭）

def read_file():
    param = []
    file_path = '../param.txt'
    with (open(file_path)) as fp:
        for line in fp.readlines():
            param.append(line.strip('\n').split(','))
    return param

@ddt()
class selenium_test_cases(unittest.TestCase):
    # 用来放置可以被读取的文件信息，作为测试用例的参数输入条件

    def setUp(self) -> None:
    #     self.driver = webdriver.Chrome("../chromedriver")
    #     # self.driver.get("http://www.baidu.com")
        pass
    #
    def tearDown(self) -> None:
    #     time.sleep(5)
    #     self.driver.quit()
        pass

    # 通过ddt传入不同的参数，实现多次循环操作同一个测试用例
    # 多个参数用数据传递，账号密码数据量多可以调用excel
    # @data('你好', '晓燕')
    # def test_00(self, txt):
    #     self.driver.find_element_by_id('kw').send_keys(txt)
    #     self.driver.find_element_by_id("su").click()
    #     pass
    # 伪文件读取
    # @data(*read_file())
    # @unpack
    # def test_02(self,url,txt):
    #     self.driver.get(url)
    #     self.driver.find_element_by_id('kw').send_keys(txt)
    #     self.driver.find_element_by_id("su").click()
    #
    #     pass
    # 通过自己输入
    # @data(("haha","xixi"),('fasd','fs'))
    # @unpack
    # def test_01(self,txt1,txt2):
    #     print("txt1:"+txt1)
    #     print("--------------------------")
    #     print("txt2:"+txt2)

    # 通过文件去读取
    # @data(*read_file())
    # @unpack
    # def test_02(self,txt1,txt2):
    #     print("txt01"+txt1)
    #     print("txt02"+txt2)
    # @data(1,2,3)
    # def test_01(self,value):      #value用来接收data的数据
    #     print(value)
    # 注意yml文件的格式，空格等
    @file_data('../testyml.yml')
    def test_01(self,**kwargs):
        print(kwargs.get("name"))
        print(kwargs.get("info"))


if __name__ == '__main__':
    unittest.main()
# 要明白ddt的解析过程，这样才能更好的使用