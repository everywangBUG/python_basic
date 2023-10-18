from wsgiref.simple_server import make_server

def run_server(arg1, response): # response给客户端返回的参数
    response("200 ok", [("Content-Type", "text/html;charset=utf-8")]) # 响应头
    return [bytes("<h2>第一个服务端程序</h2>", encoding="utf-8")]

s = make_server("localhost", 8000, run_server)
s.serve_forever()
