# -*- coding: utf-8 -*
from django.shortcuts import render


# Create your views here.
# 主要界面
def main(request):
    return render(request, 'product/main.html')


# ERP系统
def erp(request):
    return render(request, 'product/erp.html')


# 设备信息
def deviceManage(request):
    return render(request, 'product/deviceManage.html')


# 质量管理
def qualityManage(request):
    return render(request, 'product/qualityManage.html')


# 用户图纸
def drawing(request):
    return render(request, 'product/drawing.html')


# 拓展
def expand(request):
    return render(request, 'product/expand.html')
