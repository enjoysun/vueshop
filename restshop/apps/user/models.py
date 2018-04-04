from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserCenter(AbstractUser):
    """
    默认继承AbstractUser的字段，以下只需要补充即可
    verbose_name:相当于列的注释
    用户
    """
    name = models.CharField(max_length=16, null=True, blank=True, verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name='生日')
    mobile = models.CharField(max_length=11, null=False, blank=False, verbose_name='电话')
    gender = models.CharField(max_length=6, choices=((0, '男'), (1, '女')), default=0, verbose_name='性别')
    email = models.CharField(max_length=24, null=True, blank=True, verbose_name='邮箱地址')

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"

    def __str__(self):
        return self.name
