import yaml
filePath = "../testyml.yml"
file = open(filePath)
res = yaml.load(file,Loader=yaml.FullLoader)
print(res)