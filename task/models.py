# coding=utf-8
from datetime import datetime
from django.db import models
from rest_framework.settings import api_settings


class Task(models.Model):
    """
    task model
    """
    id = models.AutoField(primary_key=True, unique=True, verbose_name='任务id')
    content = models.CharField(blank=False, max_length=1000, verbose_name='任务内容')
    create_date = models.DateTimeField(auto_now_add=True,blank=False, verbose_name='任务创建时间')
    expire_date = models.DateField(verbose_name='任务截止时间')
    status = models.IntegerField(default=0, verbose_name='任务状态 0:未完成，1：已完成')
    priority = models.IntegerField(default=0, verbose_name='任务优先级 数字越大优秀级越高')
