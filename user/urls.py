"""cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    # 登陆
    url(r'^login/$', views.login, name='login'),
    # 首页
    url(r'^index/$', views.index, name='index'),
    # 主要
    url(r'^main/$', views.main, name='main'),
    # 登陆处理
    url(r'^login_handle/$', views.login_handle, name='login_handle'),
    # 注销
    url(r'^logout/$', views.logout, name='logout'),
    # 权限分配
    url(r'^permissions/(\d*)$', views.permissions, name='permissions'),
    # 查看用户
    url(r'^listUser/$', views.listUser, name='listUser'),

    # url(r'^getUserInfo/$', views.getUserInfo, name='getUserInfo'),
    url(r'^PassWordChange/(\d*)$', views.PassWordChange, name='PassWordChange'),

    url(r'^change_permissions_handler/$', views.change_permissions_handler, name='change_permissions_handler'),
    url(r'^del_user/(\d*)$', views.del_user, name='del_user'),



    # url(r'^GetUserPermiss/(\d*)$', views.GetUserPermiss, name='GetUserPermiss'),

]
