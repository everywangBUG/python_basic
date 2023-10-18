from wsgiref.simple_server import make_server
import re
import os

BASE_DIRPATH = os.path.dirname(os.path.abspath(__file__))

def handle_htmlres(response):
    response("200 ok", [("Content-Type", "text/html;charset=utf-8")]) # html响应头

def main(enviroment, response):
    handle_htmlres(response)
    data = """
        <h2>main</h2>
        <image src="/static/images/wyz11.png">
        <h2>main页面!!!!</h2>
    """
    return [bytes(data, encoding="utf-8")]

def profile(enviroment, response):
    handle_htmlres(response)
    return [bytes("<h2>profile</h2>", encoding="utf-8")]

def error(enviroment, response):
    handle_htmlres(response)
    return [bytes("<h2>页面找不到了!_!</h2>", encoding="utf-8")]

# 图片请求处理
def image_handler(request_url):
    """图片请求处理
    Args:
        request_url (string): 客户端请求的路径
    Returns:
        list: 图片内容，1代表有图片内容，0代表没有图片内容
    """
    img_path = re.sub("/static", "/static_data", request_url)
    img_abs_path = BASE_DIRPATH + img_path
    if os.path.isfile(img_abs_path): # 不能判断相对路径，只能判断觉绝对路径
        f = open(img_abs_path, "rb")
        data = f.read()
        return [data, 1]
    return [None, 0]

def dispatch_url():
    urls ={
        "/main": main,
        "/profile": profile
    }
    return urls

def run_server(enviroment, response): # response给客户端返回的参数
    request_url = enviroment.get("PATH_INFO") # 拿到客户端请求的path
    url_list = dispatch_url()
    if request_url in url_list:
        response_data = url_list[request_url](enviroment, response)
        return response_data
    elif request_url.startswith('/static/'):
        img_data, img_status = image_handler(request_url)
        if (img_status == 1):
            response("200 ok", [("Content-Type", "image/png;charset=utf-8")])
            return [img_data]
    else:
        error_data = error(enviroment, response)
        return error_data

s = make_server("localhost", 8000, run_server)
s.serve_forever()
