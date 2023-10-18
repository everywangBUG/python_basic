from wsgiref.simple_server import make_server

def recive_res(response):
    response("200 ok", [("Content-Type", "text/html;charset=utf-8")]) # 响应头

def main(enviroment, response):
    recive_res(response)
    return [bytes("<h2>main</h2>", encoding="utf-8")]

def profile(enviroment, response):
    recive_res(response)
    return [bytes("<h2>profile</h2>", encoding="utf-8")]

def error(enviroment, response):
    recive_res(response)
    return [bytes("<h2>页面找不到了!_!</h2>", encoding="utf-8")]

def dispatch_url():
    urls ={
        "/main": main,
        "/profile": profile
    }
    return urls
    

def run_server(enviroment, response): # response给客户端返回的参数
    request_url = enviroment.get("PATH_INFO") # 拿到客户端请求的path
    print(request_url)
    url_list = dispatch_url()
    if request_url in url_list:
        response_data = url_list[request_url](enviroment, response)
        return response_data
    else:
        error_data = error(enviroment, response)
        return error_data

s = make_server("localhost", 8000, run_server)
s.serve_forever()
