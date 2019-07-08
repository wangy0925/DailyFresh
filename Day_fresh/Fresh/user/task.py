# 使用celery

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


# 在任务处理者加

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fresh.settings')
django.setup()
#
# # 创建一个实例对象
# app = Celery('celery_task.task', broker='redis://127.0.0.1:6379/10')
# app.autodiscover_tasks()

# 定义任务函数
@shared_task
def send_register_active_email(to_email, username, token):
    """
    :param to_email:
    :param username:
    :param token:
    :return: 发送邮件
    """
    # 注册成功之后, 跳转到登录页面
    # 发送激活链接, 包含链接: 激活链接中需要包含用户的身份信息(需加密) 163邮箱为例
    # 发邮件
    subject = '天天生鲜'  # 主题
    message = '<h1>%s, 欢迎您成为天天生鲜会员, 请点击下面链接激活您的账户' \
              '<br/><a href="http://127.0.0.1:8000/user/active/%s">http://127.0.0.1:8000/user/active/%s</a></h1>' % (
              username, token, token)  # 邮件正文
    sender = settings.EMAIL_FROM  # 发件人
    recipient_list = [to_email]  # 收件人列表
    send_mail(subject=subject, from_email=sender, recipient_list=recipient_list, html_message=message, message='111')
    