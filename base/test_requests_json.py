# coding：utf-8
import requests
import json

url = "https://www.baidu.com/s?"
data = {
    "wd": "test"
}
response = requests.get(url, data)

url1 = "https://api.binstd.com/train/ticket"
data1 = {
    "appkey": "7b9b0b62d0f5551e",
    "start": "杭州",
    "end": "北京",
    "date": "2020-12-01"
}
response2 = requests.post(url1, data1)

# 返回str类型的数据
print(response2.text)
print(type(response2.text))

# 将字典转成一个json，并且格式化的形式输出
print(json.dumps(response2.json(), indent=4, ensure_ascii=False))

# 把返回的json类型的值转换成字典类型的值
print(type(json.loads(response2.text)))
# 将json格式的数据转换为字典形式
print(type(response2.json()))

# 测试发车的起始点是不是"杭州"和"北京"
def test_start_end():
    print(type(response2.json()))
    print(type(response2.json()["result"]))
    print(type(response2.json()["result"]["list"]))
    print(response2.json()["result"]["list"])

    # list里面每个值都是字典类型的，所以不存在station值，但是可以通过遍历list中的每个dict型的值得到每个dict的station。
    # * print(type(response2.json()["result"]["list"]["station"]))

    # 通过xxx[s]取得字典中某个元素's'的值
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

# 将一个json数据转成一个字典
# 1. response.json()
# 2. json.loads(response.text)


# 将字典转成一个json，并且格式化的形式输出
# json.dumps(response.json(), indent=4, ensure_ascii=False)

