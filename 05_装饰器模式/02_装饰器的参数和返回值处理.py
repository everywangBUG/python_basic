def guanjia(game):
    def inner(*args, **kwargs):
        print("开挂")
        res = game(*args, **kwargs) # 如果玩游戏有返回值，那么执行之后需要返回
        print("关闭外挂")
        return res
    return inner

@guanjia
def play_dnf(user_name, pass_word):
    print(f"{user_name}登录成功，开始玩，密码{pass_word}正确")
    print("你好呀，我叫赛利亚，今天又是美好的一天")
    return "闪光了!!!"
    
@guanjia
def play_lol(user_name, pass_word, hero):
    print(f"{user_name}登录成功，开始玩，密码{pass_word}正确， 玩的英雄是{hero}")
    print('真正的大师，永远怀着一颗学徒的心')

res = play_dnf("zhangsan", "123456")
print(res)
play_lol("李四", '12345678', "德玛西亚")