from django.db import models

# Create your models here.
from django.db import models


class Admin(models.Model):
    #管理员
    username = models.CharField(max_length=32,verbose_name="姓名")
    password = models.CharField(max_length=64,verbose_name="密码")

    def __str__(self):
        return self.username


class Department(models.Model):
    title = models.CharField(max_length=32,verbose_name="标题")

    def __str__(self):
        return self.title