# 通用装饰器
def wrapper1(fn):
    def inner(*args, **kwargs):
        print("执行函数1之前操作")
        res = fn(*args, **kwargs)
        print("执行函数1之后操作")
        return res
    return inner

def wrapper2(fn):
    def inner(*args, **kwargs):
        print("执行函数2之前操作")
        res = fn(*args, **kwargs)
        print("执行函数2之后操作")
        return res
    return inner

@wrapper1 # wrapper1(wrapper2(inner))
@wrapper2 # wrapper2(inner)
def exec(name="zhangsan"):
    print(f"{name}要学习!!!")
    return "我爱学习"

res = exec(name="lisi") # 先被wrapper1装饰，后被wrapper2装饰
print(res)
