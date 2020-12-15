import yaml

filePath = "../file/testyml.yml"
file = open(filePath)
# 需要加上"Loader=yaml.FullLoader"，不然会报错说是不加loader类型是不安全的。
res = yaml.load(file, Loader=yaml.FullLoader)
print(res)
