from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect


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
        # return render(request, 'user/index.html', context)
    else:
        context = {'error': 'error'}
        return render(request, '/user/login.html', context)


def logout(request):
    red = redirect('/user/login/')
    red.delete_cookie('username')
    print(request.COOKIES['username'])
    return red
