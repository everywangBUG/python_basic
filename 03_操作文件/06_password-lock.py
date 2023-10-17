# 要求⽤户输⼊帐号密码进⾏登陆
# ⽤户账号信息保存在⽂件内
# ⽤户密码输⼊错误三次后锁定⽤户，下次再登录，检测到是这个被锁定的⽤户，则依然不允许其它登录，提示已被锁

# 1. 遍历文件accounts
acounts = {}
f = open("acounts.txt", mode="r")
for item in f:
    line = item.strip().split(",")
    acounts[line[0]] = line
print(acounts["jack"][2] == "1")

while True: 
    user = input('请输入帐号：').strip()
    if user not in acounts:
        print(f'用户名{user}未注册')
        continue
    elif acounts[user][2] == "1":
        print(f"此账户{user}被锁定")
        break
    count = 0
    while count < 3:
        passward = input('请输入密码：').strip()
        if passward == acounts[user][1]:
            print(f"{user}登录成功")
            exit("bye...")
        else:
            print("错误的密码")
            count += 1
    print(count, "count")
    if count == 3:
        print(f"输错了{count}次密码，将锁定帐户{user}")
        # 修改dict中的用户状态
        # 把dict中的数据转为原accounts.txt数据格式，存回文件
        acounts[user][2] = "1"
        f1 = open("acounts.txt", mode="w", encoding="utf-8")
        for key, val in acounts.items():
            line = ",".join(val) + "\n"
            print(line, 'line')
            f1.write(line)
        f1.close()
        exit("bye...")