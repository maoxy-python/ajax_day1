# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=128, verbose_name='用户名')
    password = models.CharField(max_length=256, verbose_name='密码')
    email = models.EmailField(verbose_name='邮箱')
    sex = models.CharField(max_length=12, default='1', verbose_name='性别')
    c_time = models.DateTimeField(auto_now_add=True)
    has_confirmed = models.BooleanField(default=False, verbose_name='是否确认')

    class Meta:
        db_table = 'User'


class ConfirmString(models.Model):

    code = models.CharField(max_length=256, verbose_name='注册码')
    user = models.OneToOneField('User', on_delete=models.CASCADE, verbose_name='关联的用户')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='注册码生成时间')

    class Meta:
        db_table = 'ConfirmString'

