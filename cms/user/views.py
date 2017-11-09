from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect,JsonResponse


# Create your views here.
# 登陆页面
def login(request):
    return render(request, 'user/login.html')


# 主页
def index(request):
    # 如果cookie不存在
    if 'username' not in request.COOKIES:
        # 如果访问的路径不是/login/就跳转到/login/
        if request.path != '/user/login/':
            return redirect('/user/login/')

    username = request.COOKIES['username']
    context = {"username": username}
    return render(request, 'user/index.html', context)


def main(request):
    return render(request, 'user/main.html')


# 查看用户界面
def listUser(request):
    return render(request, 'user/listUser.html')


# 登陆处理
def login_handle(request):
    post_info = request.POST
    username = post_info.get('username')
    passwd = post_info.get('passwd')
    # 验证用户
    if username == "123" and passwd == "123":
        # 用户账号和密码正确，进入主页
        red = redirect('/user/index/')
        # request.session['username'] = username
        # request.session['user_id'] = uname
        red.set_cookie('username', username)
        context = {"username": username}
        # return
        return red
        # return render(request, 'user/index1.html', context)
    else:
        context = {'error': 'error'}
        return render(request, 'user/login.html', context)


# 注销
def logout(request):
    red = redirect('/user/login/')
    red.delete_cookie('username')
    # print(request.COOKIES['username'])
    return red


# 权限分配页面
def permissions(request):
    return render(request, 'user/permissions.html')

# 模拟获取用户数据
def getUserInfo(request):
    return JsonResponse({"code":0,"msg":"","count":1000,"data":[{"id":10000,"username":"user-0","sex":"女","city":"城市-0","sign":"签名-0","experience":255,"logins":24,"wealth":82830700,"classify":"作家","score":57},{"id":10001,"username":"user-1","sex":"男","city":"城市-1","sign":"签名-1","experience":884,"logins":58,"wealth":64928690,"classify":"词人","score":27},{"id":10002,"username":"user-2","sex":"女","city":"城市-2","sign":"签名-2","experience":650,"logins":77,"wealth":6298078,"classify":"酱油","score":31},{"id":10003,"username":"user-3","sex":"女","city":"城市-3","sign":"签名-3","experience":362,"logins":157,"wealth":37117017,"classify":"诗人","score":68},{"id":10004,"username":"user-4","sex":"男","city":"城市-4","sign":"签名-4","experience":807,"logins":51,"wealth":76263262,"classify":"作家","score":6},{"id":10005,"username":"user-5","sex":"女","city":"城市-5","sign":"签名-5","experience":173,"logins":68,"wealth":60344147,"classify":"作家","score":87},{"id":10006,"username":"user-6","sex":"女","city":"城市-6","sign":"签名-6","experience":982,"logins":37,"wealth":57768166,"classify":"作家","score":34},{"id":10007,"username":"user-7","sex":"男","city":"城市-7","sign":"签名-7","experience":727,"logins":150,"wealth":82030578,"classify":"作家","score":28},{"id":10008,"username":"user-8","sex":"男","city":"城市-8","sign":"签名-8","experience":951,"logins":133,"wealth":16503371,"classify":"词人","score":14},{"id":10009,"username":"user-9","sex":"女","city":"城市-9","sign":"签名-9","experience":484,"logins":25,"wealth":86801934,"classify":"词人","score":75}]})
