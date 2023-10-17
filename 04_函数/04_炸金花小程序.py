# 1. 允许⽤户⼀次性输⼊多个玩家姓名，不限个数，然后为每个玩家随机⽣成3张牌
# 2. 你只有⼀付扑克牌，确保发出去的每张牌不重样
# 3. 牌需要有⿊桃、红桃、⽅⽚、梅花之分
# 4. 规则：

import random

def user_input():
    """ 输入玩家
    """
    users = {}
    user_number = input("请输入用户数量2-6人：")
    user_number = int(user_number)
    if user_number < 2 or user_number > 6:
        exit("请输入2到6人！")
    while int(user_number):
        name = input("请输入用户姓名：")
        users[name] = []
        user_number -= 1
    return users

def init_poker():
    """ 初始化扑克牌
    """
    poker = []
    color = ["黑桃", "红桃", "方块", "梅花"]
    number = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    for color_i in color:
        for number_i in number:
            poker.append(color_i + "_" + number_i)
    return poker

def deal_poker(users, poker=[]):
    """ 发牌
    :param: users用户数
    :param: poker去除大王小王扑克
    :return: plaer_dic玩家获得牌
    """
    player_dic = {}
    for user in users:
        selected_poker = random.sample(poker, 3)
        # 去除重复牌
        for c in selected_poker:
            poker.remove(c)
        player_dic[user] = selected_poker
        
    for user in player_dic:
        print(user, ":", player_dic[user])

    return player_dic

users = user_input()
poker = init_poker()
deal_poker(users, poker)