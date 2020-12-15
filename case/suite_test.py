from case.test_method import TestMethod
import unittest

# 第一种测试用例添加方法：单个添加
suite = unittest.TestSuite()
# suite.addTest(TestMethod("test_01"))
# suite.addTest(TestMethod("test_02"))
# suite.addTest(TestMethod("test_03"))
# runner = unittest.TextTestRunner()
# runner.run(suite)




# 用列表的形式将测试用例添加到suite中,
# 第二种测试用例添加方法：批量添加
# cases = [TestMethod("test_01"),TestMethod("test_02"),TestMethod("test_03")]
# suite.addTests(cases)
# runner = unittest.TextTestRunner()
# runner.run(suite)

# 第三种测试用例添加方法：discover
# testdir = "./"
# discover = unittest.defaultTestLoader.discover(testdir,pattern="sele*.py")
# runner = unittest.TextTestRunner()
# runner.run(discover)


# 第四种测试用例添加方法：unittest.TestLoader().loadTestsFromName
# suite.addTests(unittest.TestLoader().loadTestsFromName("test_method.TestMethod"))
# runner = unittest.TextTestRunner()
# runner.run(suite)
# 第五种测试用例添加方法：
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMethod))
runner = unittest.TextTestRunner()
runner.run(suite)