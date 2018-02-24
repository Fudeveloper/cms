from django.shortcuts import render
import cookie_handler
from decorate import *
import requests
import json

api_link = settings.API_ADDRESS
headers = settings.HEADERS


def get_Device_Data(request):
    userid, presend_cookie = cookie_handler.get_cookie(request)
    data = {"id": "3"}
    # 从服务器获取所有设备信息
    result = requests.post(api_link + "/Api/DeviceData/List", headers=headers, cookies=presend_cookie,
                           json=data).text
    # print(result)
    return result


# Create your views here.
# 设备管理主要界面
@check_permiss(get_Device_Data)
def main(request,return_context):
    return render(request, 'device/main.html',context=return_context)


@check_permiss(get_Device_Data)
def control(request,return_context):
    return render(request, 'device/control.html',context=return_context)


# 获取设备数据（查看）
@auth
def getDeviceData(request):
    print("----------ininin")
    result = get_Device_Data(request)
    result = json.loads(result)

    # print(result)
    # 设备信息
    only_data_devices = []
    if "appendData" in result.keys():
        device_infos = result['appendData']
        # print(user_infos)
        only_data_device_count = len(only_data_devices)
        for device_info in device_infos:
            print(device_info)
            try:
                if int(device_info["DevID"]) < 100:
                    only_data_devices.append(device_info)
            except:
                    pass

    else:
        only_data_devices = ""
        only_data_device_count = 0
    # 用户数量
    print(only_data_device_count)
    return JsonResponse({"code": 0, "msg": "", "count": only_data_device_count, "data": only_data_devices})


# 获取可控制设备
@auth
def getContorlDevice(request):
    result = get_Device_Data(request)
    result = json.loads(result)

    # print(result)
    # 设备信息
    only_data_devices = []
    if "appendData" in result.keys():
        device_infos = result['appendData']
        # print(user_infos)
        only_data_device_count = len(only_data_devices)
        for device_info in device_infos:
            try:
                if int(device_info["DevID"]) >= 100:
                    only_data_devices.append(device_info)
            except:
                    pass
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
