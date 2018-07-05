"""guest URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from sign import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.index),  # 添加index/路径配置
    url(r'^login_action/$',views.login_action),
    url(r'^event_manage/$',views.event_manage), # 添加会议管理
    url(r'^accounts/login/$',views.index),
    url(r'^search_name/$',views.search_name), # 添加姓名搜索
    url(r'^guest_manage/$',views.guest_manage), # 添加嘉宾管理
    url(r'^search_realname/$',views.search_realname) # 添加搜索嘉宾名字
]
