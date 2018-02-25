from django.conf import settings

api_link = settings.API_ADDRESS
headers = settings.HEADERS
from decorate import *


# Create your views here.

# 获得设备数据
def get_Device_Data(request):
    userid, presend_cookie = cookie_handler.get_cookie(request)
    data = {"id": "3"}
    # 从服务器获取所有设备信息
    result = requests.post(api_link + "/Api/DeviceData/List", headers=headers, cookies=presend_cookie,
                           json=data).text
    # print(result)
    return result


# 主要界面
def main(request):
    return render(request, 'security/main.html')


# 环境监控
@check_permiss(get_Device_Data)
def environment(request, return_context):
    if "basedata" in return_context.keys():
        temprature = humidity = light = ""
        infos = return_context["basedata"]['appendData']
        return_context["basedata"] = ""
        for info in infos:
            if info["DevID"] == '7':
                temprature = info["DevData"]
            elif info["DevID"] == '8':
                humidity = info["DevData"]
            elif info["DevID"] == '9':
                light = info["DevData"]

        return_context["temprature"] = temprature
        return_context["humidity"] = humidity
        return_context["light"] = light
    print("-------")
    print(return_context)
    print("-------")
    return render(request, 'security/environment.html', context=return_context)


# 门禁管理
def guard(request):
    return render(request, 'security/guard.html')


# 视频监控
def video(request):
    return render(request, 'security/video.html')


def attendance(request):
    return render(request, 'security/attendance.html')


# 获取环境数据
def get_envir_data(request):
    status = "false"
    temprature = humidity = light = ""
    userid, presend_cookie = cookie_handler.get_cookie(request)
    data = {"id": "3"}
    # 从服务器获取所有设备信息
    result = requests.post(api_link + "/Api/DeviceData/List", headers=headers, cookies=presend_cookie,
                           json=data).text
    json_result = json.loads(result)
    if "appendData" in json_result.keys():
        infos = json_result["appendData"]
        if infos:
            for info in infos:
                if info["DevID"] == '7':
                    temprature = info["DevData"]
                elif info["DevID"] == '8':
                    humidity = info["DevData"]
                elif info["DevID"] == '9':
                    light = info["DevData"]
            for i in [temprature, humidity, light]:
                if i:
                    status = "true"
            print("--------light:{}".format(light))
    return JsonResponse({"temprature": temprature, "humidity": humidity, "light": light, "status": status})
