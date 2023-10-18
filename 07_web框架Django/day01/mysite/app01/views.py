from django.shortcuts import render, HttpResponse

# Create your views here.

def main_view(request):
    # request是客户端的各种参数
    print(dir(request))
    print("执行业务逻辑，第一次请求")
    return HttpResponse("<h1 style='color:red'>第一次请求!</h1>")

def login_view(request):
    # 打开文件，返回给前端
    return render(request, 'login.html')
