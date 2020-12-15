from case.test_mock_skip_assert_report import TestMethod
import unittest

# 第一种执行方法
# unittest.main()

# 第二种测试用例添加方法：单个添加
# suite = unittest.TestSuite()
# suite.addTest(TestMethod("test_01"))
# suite.addTest(TestMethod("test_02"))
# suite.addTest(TestMethod("test_03"))
# runner = unittest.TextTestRunner()
# runner.run(suite)

# 第三种测试用例添加方法：批量添加
# 用列表的形式将测试用例添加到suite中,
# cases = [TestMethod("test_01"),TestMethod("test_02"),TestMethod("test_03")]
# suite = unittest.TestSuite()
# suite.addTests(cases)
# runner = unittest.TextTestRunner()
# runner.run(suite)

# 第四种测试用例添加方法：discover（调用其他模块中的方法）
# test_dir = "./"
# discover = unittest.defaultTestLoader.discover(test_dir,pattern="selenium*.py")
# runner = unittest.TextTestRunner()
# runner.run(discover)

# 第五种测试用例添加方法：unittest.TestLoader().loadTestsFromName
# suite = unittest.TestSuite()
# suite.addTests(unittest.TestLoader().loadTestsFromName("test_method.TestMethod"))
# runner = unittest.TextTestRunner()
# runner.run(suite)

# 第六种测试用例添加方法：
suite = unittest.TestSuite()
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMethod))
runner = unittest.TextTestRunner()
runner.run(suite)
