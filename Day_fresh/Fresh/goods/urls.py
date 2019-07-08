from django.urls import path
from .views import *

urlpatterns = [
    path('index/', goods_index),  # 首页

]