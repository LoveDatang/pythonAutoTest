from unittest import mock
# 这里的mock_method到底有没有用？感觉没有用到，是直接跳过了url，把response_data打印出来了。
def mock_test(mock_method,request_data,url,method,response_data):
    mock_method = mock.Mock(return_value=response_data)
    response = mock_method(url,method,request_data)
    return response