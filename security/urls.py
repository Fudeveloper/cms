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
    url(r'^main/$', views.main, name='main'),
    # 环境监控
    url(r'^environment/$', views.environment, name='environment'),
    # 门禁管理
    url(r'^guard/$', views.guard, name='guard'),
    # 视频监控
    url(r'^video/$', views.video, name='video'),
    #
    url(r'^attendance/$', views.attendance, name='attendance'),
    url(r'^get_envir_data/$', views.get_envir_data, name='get_envir_data'),


]
