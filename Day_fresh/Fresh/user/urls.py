from django.conf.urls import url
from .views import *
from django.urls import path

urlpatterns = [
    path('register/', register),  # 注册
    path('active/<str:token>/', register_active),  # 激活用户
    path('login/', login),  # 登录
]