
from .views import *
from django.urls import path

urlpatterns = [
    path('register/', register),  # 注册
    path('active/<str:token>/', register_active),  # 激活用户
    path('login/', login),  # 登录
    path('info/', user_info),  # 个人中心
    path('orders/', user_orders),  # 个人中心-全部订单
    path('receive/address/', user_address),  # 个人中心-收货地址
]