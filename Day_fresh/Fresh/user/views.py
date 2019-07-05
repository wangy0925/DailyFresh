import re
from django.shortcuts import render, redirect
from .models import *
from itsdangerous import TimedJSONWebSignatureSerializer as dangerous_serializer
from itsdangerous import SignatureExpired
from django.http import HttpResponse
from django.conf import settings
from celery_task.task import send_register_active_email
import time


# Create your views here.

def register(request):
    """
    :param request:
    :return: 用户注册
    """
    if request.method == 'GET':
        return render(request, 'user/register.html')
    else:
        user_name = request.POST.get('user_name')
        pwd = request.POST.get('pwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')
        # 首先判断 是否为空
        if not all([user_name, pwd, email, allow]):
            # 参数为空情况下
            return render(request, 'user/register.html', {'error_message': '数据不完整'})
        # 其次判断 邮箱是否标准
        if not re.match("^[a-z0-9A-Z]+[- | a-z0-9A-Z . _]+@([a-z0-9A-Z]+(-[a-z0-9A-Z]+)?\\.)+[a-z]{2,}$", email):
            return render(request, 'user/register.html', {'error_message': '邮箱格式不正确不完整'})
        if not allow == 'on':
            return render(request, 'user/register.html', {'error_message': '请勾选协议'})
            
        # 再次判断用户是否已经存在
        try:
            user = User.objects.get(username=user_name)
        except User.DoesNotExist:
            # 不存在的情况下注册
            user_obj = User.objects.create_user(username=user_name, password=pwd, email=email)
            user_obj.is_active = False
            user_obj.save()
            se = dangerous_serializer(settings.SECRET_KEY, 3600)  # 3600 过期时间
            info = {
                'confirm': user_obj.id,
            }
            token = se.dumps(info)  # 得到加密byte
            token = token.decode('utf-8')
            
            # 异步发送邮件
            send_register_active_email.delay(email, user_name, token)
            # 跳转到首页
            return render(request, 'goods/goods.html')
        else:
            return render(request, 'user/register.html', {'error_message': '此用户已注册'})


def register_active(request, token):
    """
    :param request: 激活用户
    :return:
    """
    if request.method == 'GET':
        # 获取要激活的用户信息
        se = dangerous_serializer(settings.SECRET_KEY, 3600)  # 3600 过期时间
        try:
            info = se.loads(token)
            # 获取激活用户id
            user_id = info['confirm']
            # 获取用户信息
            user = User.objects.get(id=user_id)
            user.is_active = True
            user.save()
            # 跳转到登录页面
            return redirect('/user/login/')
        except SignatureExpired as e:
            # 如果剖出 过期异常, 激活链接已过期
            return HttpResponse('激活链接已过期')
            
           
def login(request):
    """
    :param request:
    :return: 登录
    """
    return render(request, 'user/login.html')