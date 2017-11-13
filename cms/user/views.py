from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.conf import settings
import requests


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'}
api_link = ""
if settings.DEBUG == False:
    global api_link
    api_link = "http://123.207.68.28/"
else:
    global api_link
    api_link = "127.0.0.1"


# Create your views here.
# 登陆页面
def login(request):
    # return HttpResponse(settings.DEBUG)
    return render(request, 'user/login.html')


# 主页
def index(request):
    # 如果cookie不存在
    if 'username' not in request.COOKIES:
        # 如果访问的路径不是/login/就跳转到/login/
        if request.path != '/user/login/':
            return redirect('/user/login/')

    username = request.COOKIES['username']
    context = {"username": username}
    return render(request, 'user/index.html', context)


def main(request):
    return render(request, 'user/main.html')


# 查看用户界面
def listUser(request):
    return render(request, 'user/listUser.html')


# 登陆处理
def login_handle(request):
    post_info = request.POST
    username = post_info.get('username')
    passwd = post_info.get('passwd')
    # 验证用户

    post_data = {"userName": username, "passWord": passwd}
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'}
    requests.post(url=api_link + "Account/Logon/",data=passwd,headers=headers)

    if username == "123" and passwd == "123":
        # 用户账号和密码正确，进入主页
        red = redirect('/user/index/')
        # request.session['username'] = username
        # request.session['user_id'] = uname
        red.set_cookie('username', username)
        context = {"username": username}
        # return
        return red
        # return render(request, 'user/index1.html', context)
    else:
        context = {'error': 'error'}
        return render(request, 'user/login.html', context)


# 注销
def logout(request):
    red = redirect('/user/login/')
    red.delete_cookie('username')
    # print(request.COOKIES['username'])
    return red


# 权限分配页面
def permissions(request):
    return render(request, 'user/permissions.html')


# 模拟获取用户数据
def getUserInfo(request):
    return JsonResponse({"code": 0, "msg": "", "count": 33, "data": [{
        "id": 10000,
        "username": "user-0",
        "status": "在线",
        "group": "系统管理员",
        "permissions": "增加用户,删除用户,更改用户密码,查看当前登陆人员，配置用户权限，查看所有日志，添加模块，启用/关闭报警方式，解除警报，控制设备，查看数据",

    },
        {
            "id": 10001,
            "username": "user-1",
            "status": "在线",
            "group": "生产管理员",
            "permissions": "添加模块，启用/关闭报警方式，解除警报，控制设备，查看数据",

        },
        {
            "id": 10002,
            "username": "user-2",
            "status": "在线",
            "group": "操作员",
            "permissions": "解除警报，控制设备，查看数据",

        },
        {
            "id": 10003,
            "username": "user-3",
            "status": "在线",
            "group": "来宾",
            "permissions": "查看数据",

        },
        {
            "id": 10000,
            "username": "user-0",
            "status": "在线",
            "group": "系统管理员",
            "permissions": "增加用户,删除用户,更改用户密码,查看当前登陆人员，配置用户权限，查看所有日志，添加模块，启用/关闭报警方式，解除警报，控制设备，查看数据",

        },
        {
            "id": 10001,
            "username": "user-1",
            "status": "在线",
            "group": "生产管理员",
            "permissions": "添加模块，启用/关闭报警方式，解除警报，控制设备，查看数据",

        },
        {
            "id": 10002,
            "username": "user-2",
            "status": "在线",
            "group": "操作员",
            "permissions": "解除警报，控制设备，查看数据",

        },
        {
            "id": 10003,
            "username": "user-3",
            "status": "在线",
            "group": "来宾",
            "permissions": "查看数据",

        },
        {
            "id": 10000,
            "username": "user-0",
            "status": "在线",
            "group": "系统管理员",
            "permissions": "增加用户,删除用户,更改用户密码,查看当前登陆人员，配置用户权限，查看所有日志，添加模块，启用/关闭报警方式，解除警报，控制设备，查看数据",

        },
        {
            "id": 10001,
            "username": "user-1",
            "status": "在线",
            "group": "生产管理员",
            "permissions": "添加模块，启用/关闭报警方式，解除警报，控制设备，查看数据",

        },
        {
            "id": 10002,
            "username": "user-2",
            "status": "在线",
            "group": "操作员",
            "permissions": "解除警报，控制设备，查看数据",

        },
        {
            "id": 10003,
            "username": "user-3",
            "status": "在线",
            "group": "来宾",
            "permissions": "查看数据",

        },
        {
            "id": 10000,
            "username": "user-0",
            "status": "在线",
            "group": "系统管理员",
            "permissions": "增加用户,删除用户,更改用户密码,查看当前登陆人员，配置用户权限，查看所有日志，添加模块，启用/关闭报警方式，解除警报，控制设备，查看数据",

        },
        {
            "id": 10001,
            "username": "user-1",
            "status": "在线",
            "group": "生产管理员",
            "permissions": "添加模块，启用/关闭报警方式，解除警报，控制设备，查看数据",

        },
        {
            "id": 10002,
            "username": "user-2",
            "status": "在线",
            "group": "操作员",
            "permissions": "解除警报，控制设备，查看数据",

        },
        {
            "id": 10003,
            "username": "user-3",
            "status": "在线",
            "group": "来宾",
            "permissions": "查看数据",

        },
        {
            "id": 10000,
            "username": "user-0",
            "status": "在线",
            "group": "系统管理员",
            "permissions": "增加用户,删除用户,更改用户密码,查看当前登陆人员，配置用户权限，查看所有日志，添加模块，启用/关闭报警方式，解除警报，控制设备，查看数据",

        },
        {
            "id": 10001,
            "username": "user-1",
            "status": "在线",
            "group": "生产管理员",
            "permissions": "添加模块，启用/关闭报警方式，解除警报，控制设备，查看数据",

        },
        {
            "id": 10002,
            "username": "user-2",
            "status": "在线",
            "group": "操作员",
            "permissions": "解除警报，控制设备，查看数据",

        },
        {
            "id": 10003,
            "username": "user-3",
            "status": "在线",
            "group": "来宾",
            "permissions": "查看数据",

        },
        {
            "id": 10000,
            "username": "user-0",
            "status": "在线",
            "group": "系统管理员",
            "permissions": "增加用户,删除用户,更改用户密码,查看当前登陆人员，配置用户权限，查看所有日志，添加模块，启用/关闭报警方式，解除警报，控制设备，查看数据",

        },
        {
            "id": 10001,
            "username": "user-1",
            "status": "在线",
            "group": "生产管理员",
            "permissions": "添加模块，启用/关闭报警方式，解除警报，控制设备，查看数据",

        },
        {
            "id": 10002,
            "username": "user-2",
            "status": "在线",
            "group": "操作员",
            "permissions": "解除警报，控制设备，查看数据",

        },
        {
            "id": 10003,
            "username": "user-3",
            "status": "在线",
            "group": "来宾",
            "permissions": "查看数据",

        },
        {
            "id": 10000,
            "username": "user-0",
            "status": "在线",
            "group": "系统管理员",
            "permissions": "增加用户,删除用户,更改用户密码,查看当前登陆人员，配置用户权限，查看所有日志，添加模块，启用/关闭报警方式，解除警报，控制设备，查看数据",

        },
        {
            "id": 10001,
            "username": "user-1",
            "status": "在线",
            "group": "生产管理员",
            "permissions": "添加模块，启用/关闭报警方式，解除警报，控制设备，查看数据",

        },
        {
            "id": 10002,
            "username": "user-2",
            "status": "在线",
            "group": "操作员",
            "permissions": "解除警报，控制设备，查看数据",

        },
        {
            "id": 10003,
            "username": "user-3",
            "status": "在线",
            "group": "来宾",
            "permissions": "查看数据",

        },
        {
            "id": 10000,
            "username": "user-0",
            "status": "在线",
            "group": "系统管理员",
            "permissions": "增加用户,删除用户,更改用户密码,查看当前登陆人员，配置用户权限，查看所有日志，添加模块，启用/关闭报警方式，解除警报，控制设备，查看数据",

        },
        {
            "id": 10001,
            "username": "user-1",
            "status": "在线",
            "group": "生产管理员",
            "permissions": "添加模块，启用/关闭报警方式，解除警报，控制设备，查看数据",

        },
        {
            "id": 10002,
            "username": "user-2",
            "status": "在线",
            "group": "操作员",
            "permissions": "解除警报，控制设备，查看数据",

        },
        {
            "id": 10003,
            "username": "user-3",
            "status": "在线",
            "group": "来宾",
            "permissions": "查看数据",

        }

    ]})


import json


def test(reqeust):
    res = {"fan": "open", "light": "close"}
    response = HttpResponse(json.dumps(res), content_type="application/json")
    response.__setitem__('Access-Control-Allow-origin', '*')
    response.__setitem__('Access-Control-Allow-Headers', 'x-requested-with,content-type')

    return response


def test_ajax(request):
    return render(request, 'user/test_ajax.html')
