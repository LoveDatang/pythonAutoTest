from unittest import mock
# 这里的mock_method到底有没有用？感觉没有用到，是直接跳过了url，把response_data打印出来了。
def mock_test(mock_method,request_data,url,method,response_data):
    # 这个mock_method方法只会返回传入给mock.mock()方法的return_value。可以给这个mock_method传入待测试的函数名，方法名，参数等。
    mock_method = mock.Mock(return_value=response_data)
    response = mock_method(url,method,request_data)
    return response