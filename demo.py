# coding：utf-8
import requests
import json
url = "https://www.baidu.com/s?"
method = "post"
response = requests.request(method, url)
print(response)
print(type(response))
def send_requests(method,url):
    response = requests.request(method,url)
    print(response)

data = {
    "wd":"test"
}
def send_post(url,data):
    response = requests.post(url,data)
    print(response)


send_requests(method,url)
send_post(url,data)