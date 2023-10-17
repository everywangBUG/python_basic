def guanjia(game):
    def inner():
        print("开挂")
        game()
        print("关闭外挂")
    return inner

@guanjia # 相当于play_dnf = guanjia(play_dnf)这段代码
def play_dnf():
    print("你好呀，我叫赛利亚，今天又是美好的一天")
    
@guanjia
def play_lol():
    print('真正的大师，永远怀着一颗学徒的心')

# play_dnf = guanjia(play_dnf)
play_dnf()
play_lol()

"""
1. 装饰器本质上是一个闭包
2. 作用：
    1): 在不改变原有函数调用的情况下，给函数增加新的功能
    2): 用户登录、记录日志等应用场景
"""
