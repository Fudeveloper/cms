from django.shortcuts import render
from decorate import *
# Create your views here.


# 报警管理主要界面（开启/关闭报警模块）
@auth
def main(request):
    return render(request, 'warn/main.html')

