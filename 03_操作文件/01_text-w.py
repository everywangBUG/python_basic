# -*- coding:utf-8 -*-

f = open("name_list.txt", mode="w", encoding="utf-8") # w创建模式，如果有改文件会覆盖

f.write("zhangsan\n")
f.write("lisi\n")
f.write("王五\n")
f.write("王五111\n")
f.write("王五222\n")
f.close()