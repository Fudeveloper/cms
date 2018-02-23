from django.shortcuts import render
import cookie_handler
from decorate import *
import requests
import json

api_link = settings.API_ADDRESS
headers = settings.HEADERS


# Create your views here.
# 设备管理主要界面
@check_permiss("getDeviceData")
def main(request):
    return render(request, 'device/main.html')


def control(request):
    return render(request, 'device/control.html')

# 获取设备数据（查看）
@check_permiss("selectAllDevice")
@auth
def getDeviceData(request):
    userid, presend_cookie = cookie_handler.get_cookie(request)
    data = {"id": "3"}
    # 从服务器获取所有设备信息
    result = requests.post(api_link + "/Api/DeviceData/List", headers=headers, cookies=presend_cookie,
                           json=data).text
    result = json.loads(result)

    # print(result)
    # 设备信息
    only_data_devices = []
    if "appendData" in result.keys():
        device_infos = result['appendData']
        # print(user_infos)
        only_data_device_count = len(only_data_devices)
        for device_info in device_infos:
            if int(device_info["DevID"]) < 100:
                only_data_devices.append(device_info)
    else:
        only_data_devices = ""
        only_data_device_count = 0
    # 用户数量
    return JsonResponse({"code": 0, "msg": "", "count": only_data_device_count, "data": only_data_devices})

# 获取可控制设备
@check_permiss("selectAllDevice")
@auth
def getContorlDevice(request):
    userid, presend_cookie = cookie_handler.get_cookie(request)
    data = {"id": "3"}
    # 从服务器获取所有设备信息
    result = requests.post(api_link + "/Api/DeviceData/List", headers=headers, cookies=presend_cookie,
                           json=data).text
    result = json.loads(result)

    # print(result)
    # 设备信息
    only_data_devices = []
    if "appendData" in result.keys():
        device_infos = result['appendData']
        # print(user_infos)
        only_data_device_count = len(only_data_devices)
        for device_info in device_infos:
            if int(device_info["DevID"]) >= 100:
                only_data_devices.append(device_info)
    else:
        only_data_devices = ""
        only_data_device_count = 0
    # 用户数量
    return JsonResponse({"code": 0, "msg": "", "count": only_data_device_count, "data": only_data_devices})

# , device_id="", operate_code=""
# 修改设备状态
@auth
def UpDataDevState(request, device_id, device_status):
    status = "false"
    #  operate_code:1为开，0为关
    userid, presend_cookie = cookie_handler.get_cookie(request)
    data = {"deviceState": device_status, "deviceID": device_id}
    result = requests.post(api_link + "/Api/DeviceData/UpDataDevState", headers=headers, cookies=presend_cookie,
                           json=data).text
    result = json.loads(result)
    print(result)
    if "errorData" in result.keys():
        if result['errorData'] == "修改设备数据成功":
            status = "true"
    print(result)
    return JsonResponse({"status": status})
