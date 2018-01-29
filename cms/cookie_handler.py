from django.conf import settings


# 根据用户id设置cookie
def set_cookie(userid, res):
    cookies_variable_name = 'cookies_{0}'.format(userid)
    print(cookies_variable_name)
    exec('settings.{0} = res.cookies'.format(cookies_variable_name))


# 根据用户id获取对应cookie
def get_cookie(request, user_id=""):
    if not user_id:
        userid = request.COOKIES.get("userid")
    else:
        userid = user_id
    cookies_variable_name = 'cookies_{0}'.format(userid)
    try:
        presend_cookie = settings.__getattr__(cookies_variable_name)
    except Exception as e:
        presend_cookie = ""
    return userid, presend_cookie


# 删除相应id
def remove_cookie(userid):
    try:
        cookies_variable_name = 'cookies_{0}'.format(userid)
        settings.__delattr__(cookies_variable_name)
        print("del cookie{}".format(userid))
    except:
        pass
