from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect

permissions = {}


# 权限验证装饰器
def check_permiss(permiss_name):
    print("装饰器初始化")

    def inner_check_permiss(func):
        print("验证{}权限".format(permiss_name))

        def inner(request, *args, **kwargs):
            print("验证权限")
            userid = request.COOKIES.get('userid')
            print(userid)
            variable_name = 'permissions_{0}'.format(userid)
            global permissions
            try:
                permissions = settings.__getattr__(variable_name)
            except:
                return HttpResponse("当前会话已结束，请重新登录")
            print(permissions)
            if permiss_name in permissions:
                print("通过验证")
                return_value = func(request, *args, **kwargs)
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


def only_check_permiss(permiss_name):
    if permiss_name in permissions:
        return True
    else:
        return False
