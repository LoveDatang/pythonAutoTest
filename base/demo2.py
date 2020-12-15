# coding：utf-8
import requests
import json

url = "https://www.baidu.com/s?"
data = {
    "wd": "test"
}
# 返回格式必须是json格式的才能用
# 1. response.json()
# 2. json.loads(response.text)
response = requests.get(url, data)

url1 = "https://api.binstd.com/train/ticket"

data1 = {
    "appkey": "7b9b0b62d0f5551e",
    "start": "杭州",
    "end": "北京",
    "date": "2020-12-01"
}

response2 = requests.post(url1, data1)
# 把返回的json类型的值转换成字典类型的值
print(type(json.loads(response2.text)))

# 返回json格式的数据
print(response2.text)

# 将json格式的数据转换为字典形式
print(response2.json())

print("----------------------")


# 测试发车的起始点是不是"杭州"和"北京"
def test_start_end():
    print("8888888888888")
    print(type(response2.json()))
    print(type(response2.json()["result"]))
    print(type(response2.json()["result"]["list"]))
    print(response2.json()["result"]["list"])

    # list里面每个值都是字典类型的，所以不存在station值，但是可以通过遍历list中的每个dict型的值得到每个dict的station。
    # * print(type(response2.json()["result"]["list"]["station"]))

    print("8888888888888")

    for list in response2.json()["result"]["list"]:
        # list中的每个值都是字典类型的。
        print(type(list))
        print(type(list["station"]))
        # 断言"杭州"是不是在一个可遍历的字符串中
        assert "杭州" in list["station"]
        assert "北京" in list["endstation"]


# "测试发车点"
def test_date():
    for date in response2.json()["result"]["list"]:
        assert "20101201" in list["startdate"]


test_start_end()
assert 1 == 1
