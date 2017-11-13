from django.shortcuts import render

# Create your views here.
# 设备管理主要界面
def main(request):
    return render(request, 'device/main.html')

def control(request):
    return render(request, 'device/control.html')
