from django.shortcuts import render
import cookie_handler
from decorate import *
import requests
import json

api_link = settings.API_ADDRESS
headers = settings.HEADERS


# Create your views here.
# 设备管理主要界面
def main(request):
    return render(request, 'device/main.html')


def control(request):
    return render(request, 'device/control.html')


@auth
def getDeviceData(request):
    userid, presend_cookie = cookie_handler.get_cookie(request)
    data = {"id": "3"}
    # 从服务器获取所有用户信息
    result = requests.post(api_link + "/Api/DeviceData/List", headers=headers, cookies=presend_cookie,
                           json=data).text
    result = json.loads(result)

    print(result)
    # 用户信息
    if "appendData" in result.keys():
        user_infos = result['appendData']
        # print(user_infos)
        user_count = len(user_infos)
    else:
        user_infos = ""
        user_count = 0
    # print(user_infos)
    # 用户数量
    return JsonResponse({"code": 0, "msg": "", "count": user_count, "data": user_infos})


# , device_id="", operate_code=""
def UpDataDevState(request):
    status = "false"
    #  operate_code:1为开，0为关
    userid, presend_cookie = cookie_handler.get_cookie(request)
    data = {"deviceState": "0", "deviceID": "3"}
    result = requests.post(api_link + "/Api/DeviceData/UpDataDevState", headers=headers, cookies=presend_cookie,
                           json=data).text
    result = json.loads(result)
    if "errorData" in result.keys():
        if result['errorData'] == "修改设备数据成功":
            status = "true"
    print(result)
    return JsonResponse({"status": status})
