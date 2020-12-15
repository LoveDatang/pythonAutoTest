import requests


# reques调用封装成方法

def send_requests(method, url):
    response = requests.request(method, url)
    return response


def send_post(url, data):
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


url1 = "https://api.binstd.com/train/station2s"

data1 = {
    "appkey": "7b9b0b62d0f5551e",
    "start": "杭州",
    "end": "北京",
    "ishigh": 0
}
print(send_post(url1, data1).text)
