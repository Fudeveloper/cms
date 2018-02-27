from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
import cookie_handler
import requests
import json

permissions = {}


# 权限验证装饰器
# 所有被装饰的方法后，都要接收return_context参数
def check_permiss(get_data_func):
    def inner_check_permiss(func):
        def inner(request, *args, **kwargs):
            result = get_data_func(request, *args, **kwargs)
            print("++++++++++++++++++")
            print(*args, **kwargs)
            print("++++++++++++++++++")
            json_result = json.loads(result)
            # print("----------------{}".format(json_result))
            if "message" in json_result.keys():
                if json_result['message'] == "无权限":
                    context = {"has_permiss": "false"}
                elif json_result['message'] == "非法访问":
                    context = {"has_permiss": "notlogin"}
                elif json_result['message'] == "该用户未登录":
                    context = {"has_permiss": "notlogin"}
                else:
                    context = {"has_permiss": "true", "basedata": json_result}
            return func(request, *args, **kwargs, return_context=context)

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
