from decorate import *
import requests
import cookie_handler

api_link = settings.API_ADDRESS
headers = settings.HEADERS

# 获取&返回 登录日志
def get_Login_Log(request):
    userid, presend_cookie = cookie_handler.get_cookie(request)
    data = request.GET
    page = data.get('page')
    limit = data.get('limit')
    result = requests.get(api_link + "/Api/Login_Log/List", headers=headers, cookies=presend_cookie).text
    return result


# Create your views here.
# 主要界面
def main(request):
    return render(request, 'log/main.html')


# @check_permiss("selectLoginLog")
@check_permiss(get_data_func=get_Login_Log)
def loginLog(request, return_context):
    if "basedata" in return_context.keys():
        user_infos = return_context["basedata"]['appendData']
        user_count = len(user_infos)
        return_context["data"] = user_infos
        return_context["count"] = user_count
        print(user_infos)
        print(user_count)
    return render(request, 'log/loginLog.html', context=return_context)


def operateLog(request):
    return render(request, 'log/operateLog.html')


def warnLog(request):
    return render(request, 'log/warnLog.html')


def warn_drawing(request):
    return render(request, 'log/warn_drawing.html')
