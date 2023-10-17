def calc(name, age, address = "浙江省杭州市", *args, **kwargs): # **kwargs等价接收默认参数
    print(f"{age}的{name}在{address}上班")
    print(args[0], args[1]) # list
    print(kwargs) # dic

calc("zhangsan", 18, "江西省南昌市", "高高兴兴上班去", "快快乐乐下班", job="software engernier")
