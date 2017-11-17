import requests
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.conf import settings

# 请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'}
# 服务器地址
api_link = "http://120.78.62.39:8088/"


# if settings.DEBUG == False:
#     global api_link
#     api_link = "http://123.207.68.28/"
# else:
#     global api_link
#     api_link = "127.0.0.1"


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

    name = request.COOKIES['name']
    context = {"name": name}
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

    # 与服务器通信,验证用户
    post_data = {"userName": username, "passWord": passwd}
    res = requests.post(url=api_link + "/Api/Account/Logon/", data=post_data, headers=headers)
    # 正确返回登录成功
    result = json.loads(res.text)
    response_data = result['errorData']
    # if username == "123" and passwd == "123":
    if response_data == "登录成功":
        # 用户账号和密码正确，进入主页
        red = redirect('/user/index/')
        # request.session['username'] = "123"
        # request.session['user_id'] = uname

        # 查询用户真实姓名
        intent_name = requests.get("http://120.78.62.39:8088/Api/Account/UserInfo/", headers=headers).text
        data = json.loads(intent_name)
        name = data['appendData']['name']

        # 将用户信息存入cookie
        red.set_cookie('username', username)
        red.set_cookie('name', name)

        return red

    else:
        context = {'result': 'error'}
        return render(request, 'user/login.html', context)


# 注销
def logout(request):
    # 服务器上登出用户
    res = requests.post(url=api_link + "/Api/Account/LogOut/", headers=headers)
    response_data = json.loads(res.text)['errorData']
    print(response_data)

    # 本地浏览器退出
    red = redirect('/user/login/')
    red.delete_cookie('username')
    # print(request.COOKIES['username'])
    return red


# 权限分配页面
def permissions(request):
    return render(request, 'user/permissions.html')


# 模拟获取用户数据
def getUserInfo(request):
    # 从服务器获取所有用户信息
    result = requests.get(api_link + "/Api/Account/UserInfoList", headers=headers).text
    json_result = json.loads(result)
    # 用户信息
    user_infos = json_result['appendData']
    # 用户数量
    user_count = len(user_infos)
    return JsonResponse({"code": 0, "msg": "", "count": user_count, "data": user_infos})


import json


def test(reqeust):
    res = {"fan": "open", "light": "close"}
    response = HttpResponse(json.dumps(res), content_type="application/json")
    response.__setitem__('Access-Control-Allow-origin', '*')
    response.__setitem__('Access-Control-Allow-Headers', 'x-requested-with,content-type')

    return response


def test_ajax(request):
    return render(request, 'user/test_ajax.html')
