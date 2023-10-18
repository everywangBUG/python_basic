## 概述
* Django是python下的一个最强大的web框架
* Django是全球第五大web框架
* Instgram是已Django作为后端服务器语言开发

## http协议
* 基于TCP/IP协议
* 短链接
* 被动响应
* 无状态

## web框架的本质
1. 浏览器是socket客户端，网站是socket服务端
2. wsgi是一个规范，wsgiref实现了这个规范并在其内部实现了socket服务端
3. 根据url的不同执行不同的函数，即：路由系统
4. 使用函数式编程处理业务逻辑
5. 图片、css、js文件统一称为静态文件，需要读取内容直接返回给客户端

### 使用django创建一个web项目
* `django-admin startproject mysite`
* ![](./assets/django架构解释图.png)

### 使用django创建一个app
* `python manage.py startapp app01` 
* 一个项目中可以有多个app，每个app的功能都不同，例如支付宝、微信、淘宝等业务代码
```python
  polls/
    __init__.py # 包
    admin.py # 数据库后台
    apps.py # 把项目和app关联起来的文件
    migrations/ # 数据库相关
        __init__.py
    models.py # 数据库操作地方
    tests.py # 单元测试
    views.py # 业务逻辑函数
​```
```

## 第一次请求
1. 匹配路由，路由分发器查找用户的url对应关系
   1. 找到业务函数，调用
   2. 找不到，报404
2. 返回数据给浏览器

### django中的第一次请求
* ![](/07_web框架Django/assets/第一次请求.png)

### 启动web服务器
1. 编写路由
2. 在view.py中写业务函数
3. 通过HttpResponse方法返回数据给前端，HttpResponse是django中把响应头等内容封装的函数
4. 在mysite目录下执行命令`python manage.py runserver`，启动服务
   
## 模板配置
1. 配置setting.py，django找到模板的html的template文件
2. 调用render函数