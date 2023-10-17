is_login = False

def login_verify(fn):
    def inner(*args, **kwargs):
        global is_login
        if is_login == False:
            while 1:
                print("用户还未登录")
                name = input("请输入姓名：")
                password = input("请输入密码：")
                if name == "admin" and password == "123":
                    print("登录成功")
                    is_login = True
                    break
                else:
                    print("登录失败，用户名或密码错误")
        res = fn(*args, **kwargs)
        return res
    return inner
    
    
@login_verify
def add():
    print("添加员工信息")

@login_verify
def delete():
    print("删除员工信息")

@login_verify
def change():
    print("改变员工信息")

@login_verify
def search():
    print("查询员工信息")
    
add()
delete()
change()
search()