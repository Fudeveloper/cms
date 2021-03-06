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
    url(r'^control/$', views.control, name='control'),
    # url(r'^getDeviceData/$', views.getDeviceData, name='getDeviceData'),

    # equip_id, device_id, device_status
    url(r'^UpDataDevState/(\d*)/(\d*)/(\d*)/$', views.UpDataDevState, name='UpDataDevState'),
    # url(r'^getContorlDevice/$', views.getContorlDevice, name='getContorlDevice'),

    url(r'^api_get_device_Data/(\d*)/([0-1])/$', views.api_get_device_Data, name='api_get_device_Data'),

    url(r'^first/$', views.first, name='first'),

    url(r'^renderByEquipID/(\d*)/([0-1])/$', views.renderByEquipID, name='renderByEquipID'),

]
