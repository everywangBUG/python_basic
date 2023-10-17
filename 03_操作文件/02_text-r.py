f = open("name_list", mode="r", encoding="utf-8") # r只读模式
print(f.readline()) # 读取一行
print('----------')
print(f.read()) # 读取所有内容
