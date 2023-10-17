print(ord("a"))
print(ord("'"))

print(round(1.220, 1)) # 保留几位小数

l = list(range(10))

def compare(x):
    return x > 5

for i in filter(compare, l):
    print(i)