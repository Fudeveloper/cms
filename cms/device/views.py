from django.shortcuts import render
import cookie_handler
from decorate import *
import requests
import json

api_link = settings.API_ADDRESS
headers = settings.HEADERS
EQUIPID_COMPANY = settings.EQUIPID_COMPANY
EQUIPID_OUR = settings.EQUIPID_OUR


# 获取所有设备数据
def get_Device_Data(request):
    userid, presend_cookie = cookie_handler.get_cookie(request)
    data = {"id": "3"}
    # 从服务器获取所有设备信息
    result = requests.post(api_link + "/Api/DeviceData/List", headers=headers, cookies=presend_cookie,
                           json=data).text
    # print(result)
    return result


# 根据EquipID查询设备数据
def get_Device_Data_by_EquipID(request, EquipID, *args, **kwargs):
    print("00000000000000000000000000000000")
    print(EquipID)
    print("00000000000000000000000000000000")
    userid, presend_cookie = cookie_handler.get_cookie(request)
    data = {"EquipID": EquipID}
    # print(data)
    # 从服务器获取所有设备信息
    result = requests.post(api_link + "/Api/DeviceData/ListByEquipID", headers=headers, cookies=presend_cookie,
                           json=data).text
    print(result)
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
        # print(infos)
        for info in infos:
            try:
                if int(info["DevID"]) < 100:
                    only_data_devices.append(info)
            except:
                pass
        count = len(only_data_devices)
        # test_data = {'DevDataName': '大门', 'DevDataUnit': '', 'EquipID': 100, 'DevDataType': 0, 'DevID': '1', 'DevData': '1110'}
        # {'DevDataName': '大门', 'DevDataUnit': '', 'EquipID': '100', 'DevDataType': 0, 'DevID': '103', 'DevData': '0'}
        return JsonResponse({"code": 0, "msg": "", "count": count, "data": only_data_devices})
    else:
        return JsonResponse({"code": 0, "msg": "", "count": 0, "data": {}})


def first(request):
    return render(request, 'device/first.html')


@check_permiss(get_data_func=get_Device_Data_by_EquipID)
def renderByEquipID(request, EquipID, readonly, return_context):
    render_template = 'device/renderByEquipID_readonly.html'
    if "basedata" in return_context.keys():
        infos = return_context["basedata"]['appendData']
        return_context["readonly"] = readonly
        # DevID>=100的只需显示数据的设备
        if readonly == "1":
            only_data_devices = []
            for info in infos:
                try:
                    if int(info["DevID"]) < 100:
                        only_data_devices.append(info)
                except:
                    pass
            infos = only_data_devices
        # DevID>=100的为控制设备
        elif readonly == "0":
            only_data_devices = []
            for info in infos:
                try:
                    if int(info["DevID"]) >= 100:
                        only_data_devices.append(info)
                except:
                    pass
            infos = only_data_devices
            render_template = "device/renderByEquipID_control.html"
        print(infos)
        count = len(infos)
        return_context["data"] = infos
        return_context["count"] = count
    return render(request, render_template, context=return_context)
