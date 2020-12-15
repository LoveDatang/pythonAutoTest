# coding：utf-8
# 将request的调用封装成类
import requests

url1 = "https://api.binstd.com/shouji/query?appkey=7b9b0b62d0f5551e&shouji=13916991486"
url2 = "https://api.binstd.com/shouji/query"
data1 = {
    "appkey": "7b9b0b62d0f5551e",
    "shouji": "13916991486"
}
method = "post"

url3 = "https://api.binstd.com/train/station2s"
data2 = {
    "appkey": "7b9b0b62d0f5551e",
    "start": "杭州",
    "end": "北京",
    "ishigh": 0
}


class TestRequest:

    def send_requests(self, method, url):
        response = requests.request(method, url)
        return response

    def send_post(self, url, data):
        response = requests.post(url, data)
        return response

    def send_get(self, url):
        response = requests.get(url)
        return response

    def choose_method_to_send(self, url, method, data=None):
        response = None
        if method == "get":
            response = self.send_get(url)
        else:
            response = self.send_post(url, data)
        return response


test = TestRequest()

test.send_requests(method, url2)
test.send_post(url2, data1)
test.send_get(url1)
test.choose_method_to_send(url2, data1, "post")

print(test.send_get(url1))
print((test.send_get(url1).text))

# 知识点：
# 1. requests.get(),requests.post,requests.request()分别可以使用get，post，或者通过传入调用方法进行相应的接口方式的调用
# 2. 在函数外定义变量，函数内进行使用
# 3. 可以使用自定义函数来决定使用哪种调用方法
# 4. 如果自定义函数有些参数可以没有，那就让在形参列表里给它个默认值None
# 5. 用类进行封装
