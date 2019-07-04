import os
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from db.base_model import BaseModel
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from django.conf import settings


# Create your models here.

# def avatar_upload_path():
#     """
#     :param instance: 用户上传头像路径
#     :param filename:
#     :return:
#     """
#     name = 'user/avatar/user_{0}_avatar.jpg'.format(str(uuid.uuid1()))
#     file_path = os.path.join(settings.MEDIA_ROOT, name)
#     # 删除已上传的头像
#     if os.path.exists(file_path):
#         os.remove(file_path)
#     return name


# class Avatar(BaseModel):
#     """
#     个人头像表
#     """
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     avatar = models.ImageField(null=True, blank=True, verbose_name='用户头像', upload_to=avatar_upload_path)
#
#     class Meta:
#         verbose_name = '用户头像'
#         verbose_name_plural = verbose_name
#
#         def __str__(self):
#             return '<用户头像：%s>' % self.user.username
#
#
# class UserInfo(BaseModel):
#     """'
#     个人信息表
#
#     """
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     nickname = models.CharField(max_length=25, verbose_name='用户姓名')
#     email = models.EmailField(max_length=30, verbose_name='用户邮箱')
#
#     class Meta:
#         verbose_name = '用户信息'
#         verbose_name_plural = '用户信息'
#
#     def __str__(self):
#         return '<用户信息: %s-%s>' % (self.nickname, self.user.username)


class User(AbstractUser, BaseModel):
    """"
    用户模型类
    """
    def generate_active_token(self):
        """
        :return: 生成用户签名字符串
        """
        serializer = Serializer(settings.SECRET_KEY, 3600)
        info = {'confirm': self.id}
        token = serializer.dumps(info)
        return token.decode()
    class Meta:
        db_table = 'df_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name



class Address(BaseModel):
    """
    地址模型類
    """
    user = models.ForeignKey(User, verbose_name='所屬用戶', on_delete=models.CASCADE)
    receiver = models.CharField(max_length=20, verbose_name='收件人')
    addr = models.CharField(max_length=256, verbose_name='收貨地址')
    zip_code = models.CharField(max_length=6, null=True, verbose_name='邮政编码')
    phone = models.CharField(max_length=11, verbose_name='手机号码')
    is_default = models.BooleanField(default=False, verbose_name='是否默认')

    class Meta:
        db_table = 'db_address'
        verbose_name = '地址'
        verbose_name_plural = verbose_name

        def __str__(self):
            return '<用户-地址表: %s-%s>' % (self.user.username(), self.addr)