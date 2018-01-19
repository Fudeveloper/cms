import json
import logging

import base64
import re
import requests
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import cookie_handler
from decorate import *

logger = logging.getLogger('cms.views')

# 权限信息
api_link = settings.API_ADDRESS
headers = settings.HEADERS


# 请求头


# 服务器地址


# if settings.DEBUG == False:
#     global api_link
#     api_link = "http://123.207.68.28/"
# else:
#     global api_link
#     api_link = "127.0.0.1"


# 登陆页面
def login(request):
    # print(settings.__getattr__("API_ADDRESS"))
    # return HttpResponse(settings.DEBUG)
    return render(request, 'user/login.html')


# 主页
@auth
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
@check_permiss("selectAllUsers")
@auth
def listUser(request):
    userid, presend_cookie = cookie_handler.get_cookie(request)
    intent_name = requests.get(api_link + "/Api/Account/UserInfo", headers=headers, cookies=presend_cookie).text
    data = json.loads(intent_name)
    print("--------------------" + intent_name + "------------------------")
    alterUserPassword = only_check_permiss("alterUserPassword")
    alterUserPermiss = only_check_permiss("alterUserPermiss")
    delUser = only_check_permiss("delUser")
    # alterUserPassword
    context = {
        "alterUserPassword": alterUserPassword,
        "alterUserPermiss": alterUserPermiss,
        "delUser": delUser
    }
    return render(request, 'user/listUser.html', context=context)


# 登陆处理
def login_handle(request):
    # 获取并设置用户ua
    # ua = request.META.get('HTTP_USER_AGENT', 'unknown')
    # 取得用户提交的用户名和密码
    post_info = request.POST
    username = post_info.get('username')
    passwd = post_info.get('passwd')
    # 与服务器通信,验证用户
    post_data = {"userName": username, "passWord": passwd}
    res = requests.post(url=api_link + "/Api/Account/Logon", data=post_data, headers=headers)
    print(res.cookies)
    # 正确返回登录成功
    result = json.loads(res.text)
    # print(result)
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
        data = json.loads(intent_name)
        print(data)
        append_data = data['appendData']
        if not append_data:
            context = {'result': 'unknow'}
            return render(request, 'user/login.html', context)
        name = append_data['name']
        userid = append_data['id']

        cookie_handler.set_cookie(userid, res)

        name2 = base64.b64encode(str(name).encode("utf-8"))
        # 将用户信息存入cookie
        red.set_cookie('username', username)
        red.set_cookie('name', name2)
        red.set_cookie('userid', userid)
        permissions_result = requests.get(api_link + "/Api/Permiss/GetData?userId={}".format(userid),
                                          headers=headers).text
        permissions_result = json.loads(permissions_result)['appendData']

        permissions = []
        if permissions_result==None:
            context = {'result': 'unknow'}
            return render(request, 'user/login.html', context)
        for i in range(len(permissions_result)):
            permissions.append(permissions_result[i]['permissName'])
            print(permissions_result[i])
        # 动态创建变量名
        permissions_variable_name = 'permissions_{0}'.format(userid)
        print(permissions_variable_name)
        exec('settings.{0} = permissions'.format(permissions_variable_name))
        return red

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
    print("-----------------------------")
    userid, presend_cookie = cookie_handler.get_cookie(request)

    # 本地浏览器退出
    red = redirect('/user/login/')
    red.delete_cookie('username')
    red.delete_cookie('name')
    red.delete_cookie('userid')
    # 服务器上登出用户
    res = requests.post(url=api_link + "/Api/Account/LogOut/", headers=headers, cookies=presend_cookie)
    response_data = ""
    try:
        response_data = json.loads(res.text)['errorData']
    except Exception as e:
        logger.error(e)
    # print(response_data)
    cookie_handler.remove_cookie(userid)
    return red


# 权限分配页面

@auth
@check_permiss("alterUserPermiss")
def permissions(request):
    return render(request, 'user/permissions.html')


# 列出所有用户


@auth
def getUserInfo(request):
    userid, presend_cookie = cookie_handler.get_cookie(request)
    # 从服务器获取所有用户信息
    result = requests.get(api_link + "/Api/Account/UserInfoList", headers=headers, cookies=presend_cookie).text
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
