import requests
import json
import re
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, FileResponse, StreamingHttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import logging
import base64

logger = logging.getLogger('cms.views')

# status = False
# 权限信息
permissons = {"lala":True}
api_link = settings.__getattr__("API_ADDRESS")


# 权限验证装饰器
def check_permiss(permiss_name):
    print("验证{}权限".format(permiss_name))

    def inner_check_permiss(func):
        print("装饰器初始化")

        def inner(*args, **kwargs):
            print("验证权限")
            try:
                permiss_result = permissons[permiss_name]
            except:
                permiss_result = ""
            if permiss_result:
                print("通过验证")
                return_value = func(*args, **kwargs)
                return return_value
            else:
                print("未通过验证")
                return HttpResponse("您暂无权限访问此页面")

        return inner

    return inner_check_permiss


# 登录验证装饰器
def auth(func):
    def inner(request, *args, **kwargs):
        username = request.COOKIES.get('username')
        if not username:
            return redirect('/user/login/')
        return func(request, *args, **kwargs)

    return inner


# 请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'}


# 服务器地址


# if settings.DEBUG == False:
#     global api_link
#     api_link = "http://123.207.68.28/"
# else:
#     global api_link
#     api_link = "127.0.0.1"


# Create your views here.
# 登陆页面
def login(request):
    # print(settings.__getattr__("API_ADDRESS"))
    # return HttpResponse(settings.DEBUG)
    return render(request, 'user/login.html')


# 主页
def index(request):
    # # 如果cookie不存在
    # if 'username' not in request.COOKIES:
    #     # 如果访问的路径不是/login/就跳转到/login/
    #     return redirect('/user/login/')

    name = request.COOKIES['name']
    name_decode = base64.b64decode(name)
    context = {"name": name_decode}
    return render(request, 'user/index.html', context)


@auth
def main(request):
    return render(request, 'user/main.html')


# 查看用户界面
# @check_permiss("listUser")
@check_permiss("lala")
@auth
def listUser(request):
    return render(request, 'user/listUser.html')


# 登陆处理
def login_handle(request):
    # 获取并设置用户ua
    global headers
    ua = request.META.get('HTTP_USER_AGENT', 'unknown')
    headers = {'User-Agent': ua}
    # 取得用户提交的用户名和密码
    post_info = request.POST
    username = post_info.get('username')
    passwd = post_info.get('passwd')
    # 与服务器通信,验证用户
    post_data = {"userName": username, "passWord": passwd}
    res = requests.post(url=api_link + "/Api/Account/Logon", data=post_data, headers=headers)
    # 正确返回登录成功
    result = json.loads(res.text)
    print(result)
    response_data = ""
    try:
        response_data = result['errorData']
    except Exception as e:
        logger.error(e)
    if response_data == "登录成功":
        print("登录成功")
        # 用户账号和密码正确，进入主页
        red = redirect('/user/index/')

        # 查询用户真实姓名
        intent_name = requests.get(api_link + "/Api/Account/UserInfo", headers=headers).text
        print(intent_name)
        data = json.loads(intent_name)
        name = data['appendData']['name']
        print(name)
        name2 = base64.b64encode(str(name).encode("utf-8"))
        print(name2)
        # 将用户信息存入cookie
        red.set_cookie('username', username)
        red.set_cookie('name', name2)
        return red

    # elif response_data == "登录成功":
    #     # 用户名密码错误处理
    #     context = {'result': 'error'}
    #     return render(request, 'user/login.html', context)

    elif response_data == "该用户未注册":
        context = {'result': 'unregister'}
        return render(request, 'user/login.html', context)

    elif response_data == "该用户未激活":
        context = {'result': 'not active'}
        return render(request, 'user/login.html', context)

    else:
        context = {'result': 'unknow'}
    return render(request, 'user/login.html', context)


# 注销
@auth
def logout(request):
    # 服务器上登出用户
    res = requests.post(url=api_link + "/Api/Account/LogOut/", headers=headers)
    response_data = ""
    try:
        response_data = json.loads(res.text)['errorData']
    except Exception as e:
        logger.error(e)
    print(response_data)

    # 本地浏览器退出
    red = redirect('/user/login/')
    red.delete_cookie('username')
    red.delete_cookie('name')
    # print(request.COOKIES['username'])
    return red


# 权限分配页面
@auth
def permissions(request):
    return render(request, 'user/permissions.html')


# 列出所有用户


@auth
def getUserInfo(request):
    # 从服务器获取所有用户信息
    result = requests.get(api_link + "/Api/Account/UserInfoList", headers=headers).text
    json_result = json.loads(result)
    print(json_result)
    # 用户信息
    user_infos = json_result['appendData']
    print(user_infos)
    # 用户数量
    user_count = len(user_infos)
    return JsonResponse({"code": 0, "msg": "", "count": user_count, "data": user_infos})


def test(reqeust):
    res = {"fan": "open", "light": "close"}
    response = HttpResponse(json.dumps(res), content_type="application/json")
    response.__setitem__('Access-Control-Allow-origin', '*')
    response.__setitem__('Access-Control-Allow-Headers', 'x-requested-with,content-type')

    return response


def test_ajax(request):
    return render(request, 'user/test_ajax.html')


# 修改密码
@auth
@csrf_exempt
def PassWordChange(request, user_id):
    # 向服务器发送修改密码请求
    post_info = request.POST
    new_passwd = post_info.get('passWordNew')
    data = {"passWordOld": "null", "passWordNew": new_passwd}
    result = requests.put(api_link + "/Api/Account/PassWordChange?id={}".format(user_id), json=data,
                          headers=headers).text

    if re.findall('密码修改成功', result):
        status = 'true'
    else:
        status = 'false'
    print("status:" + status)
    json_data = {"status": status}
    return JsonResponse(json_data)
