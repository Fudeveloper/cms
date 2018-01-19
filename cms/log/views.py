from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from decorate import *
import json
import requests
import cookie_handler

api_link = settings.API_ADDRESS
headers = settings.HEADERS


# Create your views here.
# 主要界面
def main(request):
    return render(request, 'log/main.html')


@check_permiss("selectAllLog")
def loginLog(request):
    return render(request, 'log/loginLog.html')


def loginLog_handler(request):
    userid, presend_cookie = cookie_handler.get_cookie(request)
    data = request.GET
    page = data.get('page')
    limit = data.get('limit')
    # print(page)
    # print(limit)
    result = requests.get(api_link + "/Api/Login_Log/List", headers=headers, cookies=presend_cookie).text
    json_result = json.loads(result)
    # 用户信息
    user_infos = json_result['appendData']
    # 用户数量
    user_count = len(user_infos)
    return JsonResponse({"code": 0, "msg": "", "count": user_count, "data": user_infos})


def operateLog(request):
    return render(request, 'log/operateLog.html')


def warnLog(request):
    return render(request, 'log/warnLog.html')


def warn_drawing(request):
    return render(request, 'log/warn_drawing.html')
