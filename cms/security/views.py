from django.shortcuts import render


# Create your views here.
# 主要界面
def main(request):
    return render(request, 'security/main.html')


# 环境监控
def environment(request):
    return render(request, 'security/environment.html')


# 门禁管理
def guard(request):
    return render(request, 'security/guard.html')


# 视频监控
def video(request):
    return render(request, 'security/video.html')
