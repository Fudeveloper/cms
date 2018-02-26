from django.shortcuts import render
import cookie_handler
from decorate import *
import requests
import json

before_data = ""

api_link = settings.API_ADDRESS
headers = settings.HEADERS
EQUIPID_COMPANY = settings.EQUIPID_COMPANY
EQUIPID_OUR = settings.EQUIPID_OUR


def get_Device_Data(request):
    userid, presend_cookie = cookie_handler.get_cookie(request)
    data = {"id": "3"}
    # 从服务器获取所有设备信息
    result = requests.post(api_link + "/Api/DeviceData/List", headers=headers, cookies=presend_cookie,
                           json=data).text
    # print(result)
    return result


# 设备管理（查看）
@check_permiss(get_Device_Data)
def main(request, return_context):
    if "basedata" in return_context.keys():
        infos = return_context["basedata"]['appendData']
        only_data_devices = []

        for info in infos:
            # if info["EquipID"] =="01":
            #
            # if info["EquipID"] == "100":

            try:
                if int(info["DevID"]) < 100:
                    only_data_devices.append(info)
            except:
                pass
        count = len(only_data_devices)
        return_context["data"] = only_data_devices
        return_context["count"] = count
    return render(request, 'device/main.html', context=return_context)


# 设备管理（控制）
@check_permiss(get_Device_Data)
def control(request, return_context):
    if "basedata" in return_context.keys():
        infos = return_context["basedata"]['appendData']
        only_data_devices = []
        for info in infos:
            try:
                if int(info["DevID"]) >= 100:
                    only_data_devices.append(info)
            except:
                pass
        count = len(only_data_devices)
        return_context["data"] = only_data_devices
        return_context["count"] = count
    return render(request, 'device/control.html', context=return_context)


# 获取设备数据（查看）
# def getDeviceData(request):
#     print("----------ininin")
#     result = get_Device_Data(request)
#     result = json.loads(result)
#
#     only_data_devices = []
#     if "appendData" in result.keys():
#         device_infos = result['appendData']
#         # print(user_infos)
#         only_data_device_count = len(only_data_devices)
#         for device_info in device_infos:
#             print(device_info)
#             try:
#                 if int(device_info["DevID"]) < 100:
#                     only_data_devices.append(device_info)
#             except:
#                 pass
#
#     else:
#         only_data_devices = ""
#         only_data_device_count = 0
#     # 用户数量
#     print(only_data_device_count)
#     return JsonResponse({"code": 0, "msg": "", "count": only_data_device_count, "data": only_data_devices})


# 获取设备数据 (控制)
# def getContorlDevice(request):
#     result = get_Device_Data(request)
#     result = json.loads(result)
#
#     # print(result)
#     # 设备信息
#     only_data_devices = []
#     if "appendData" in result.keys():
#         device_infos = result['appendData']
#         # print(user_infos)
#         only_data_device_count = len(only_data_devices)
#         for device_info in device_infos:
#             try:
#                 if int(device_info["DevID"]) >= 100:
#                     only_data_devices.append(device_info)
#             except:
#                 pass
#     else:
#         only_data_devices = ""
#         only_data_device_count = 0
#     # 用户数量
#     return JsonResponse({"code": 0, "msg": "", "count": only_data_device_count, "data": only_data_devices})


# , device_id="", operate_code=""
# 修改设备状态
@auth
def UpDataDevState(request, equip_id, device_id, device_status):
    status = "false"
    #  operate_code:1为开，0为关
    userid, presend_cookie = cookie_handler.get_cookie(request)
    data = {"deviceState": device_status, "deviceID": device_id, "EquipID": equip_id}
    result = requests.post(api_link + "/Api/DeviceData/UpDataDevState", headers=headers, cookies=presend_cookie,
                           json=data).text
    result = json.loads(result)
    print(result)
    if "errorData" in result.keys():
        if result['errorData'] == "修改设备数据成功":
            status = "true"
    print(result)
    return JsonResponse({"status": status})


@check_permiss(get_Device_Data)
def api_get_device_Data(request, return_context):
    if "basedata" in return_context.keys():

        infos = return_context["basedata"]['appendData']
        only_data_devices = []
        print(infos)
        for info in infos:
            try:
                if int(info["DevID"]) < 100:
                    only_data_devices.append(info)
            except:
                pass
        if only_data_devices == before_data:
            return JsonResponse({"data_change": "false"})
        else:
            global before_data
            before_data = only_data_devices
            count = len(only_data_devices)

        return JsonResponse({"data_change": "true", "code": 0, "msg": "", "count": count, "data": only_data_devices})
    else:
        return JsonResponse({"code": 0, "msg": "", "count": 0, "data": {}, "data_change": "false"})
