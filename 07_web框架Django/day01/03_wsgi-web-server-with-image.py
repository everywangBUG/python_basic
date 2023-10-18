from wsgiref.simple_server import make_server
import re
import os

BASE_DIRPATH = os.path.dirname(os.path.abspath(__file__))

def handle_htmlres(response):
    response("200 ok", [("Content-Type", "text/html;charset=utf-8")]) # html响应头

def main(environ, response):
    handle_htmlres(response)
    data = """
        <div>
            <link rel="stylesheet" type="text/css" href="/static/css/main.css" />
            <div class="main"></div>
            <h2>main</h2>
            <image src="/static/images/wyz11.png">
            <h2>main页面!!!!</h2>
            <script src="/static/js/firstday.js"></script>
        </div>
    """
    return [bytes(data, encoding="utf-8")]

def profile(environ, response):
    handle_htmlres(response)
    data = """
        <div>
            <h2>profile</h2>
            <script src="/static/js/firstday.js"></script>
        </div>
    """
    return [bytes("<h2>profile</h2>", encoding="utf-8")]

def error(environ, response):
    handle_htmlres(response)
    return [bytes("<h2>页面找不到了!_!</h2>", encoding="utf-8")]
    """css请求处理
    Args:
        request_url (string): 客户端请求的路径
    Returns:
        list: css内容，1代表有js内容，0代表没有css内容
    """
    css_path = re.sub("/static", "/static_data", request_url)
    print(css_path)
    css_abs_path = BASE_DIRPATH + css_path
    if os.path.isfile(css_abs_path): # 不能判断相对路径，只能判断觉绝对路径
        f = open(css_abs_path, "rb")
        data = f.read()
        return [data, 1]
    return [None, 0]

def replace_path_readb(request_url):
    """静态资源请求处理
    Args:
        request_url (string): 客户端请求的路径
    Returns:
        list: 静态资源内容，1代表有内容，0代表没有内容
    """
    path = re.sub("/static", "/static_data", request_url)
    abs_path = BASE_DIRPATH + path
    if os.path.isfile(abs_path): # 不能判断相对路径，只能判断觉绝对路径
        f = open(abs_path, "rb")
        data = f.read()
        return [data, 1]
    return [None, 0]

def dispatch_url():
    urls ={
        "/main/": main,
        "/profile": profile
    }
    return urls

def run_server(environ, response): # response给客户端返回的参数
    request_url = environ.get("PATH_INFO") # 拿到客户端请求的path
    url_list = dispatch_url()
    if request_url in url_list:
        response_data = url_list[request_url](environ, response)
        return response_data
    elif request_url.startswith('/static/images'):
        img_data, img_status = replace_path_readb(request_url)
        if (img_status == 1):
            response("200 ok", [("Content-Type", "image/png;charset=utf-8")])
            return [img_data]
    elif request_url.startswith('/static/js'):
        js_data, js_status = replace_path_readb(request_url)
        if (js_status == 1):
            response("200 ok", [("Content-Type", "application/javascript;charset=utf-8")])
            return [js_data]
    elif request_url.startswith('/static/css'):
        css_data, css_status = replace_path_readb(request_url)
        if (css_status == 1):
            response("200 ok", [("Content-Type", "text/css;charset=utf-8")])
            return [css_data]
    else:
        error_data = error(environ, response)
        return error_data

s = make_server("localhost", 8000, run_server)
s.serve_forever()
