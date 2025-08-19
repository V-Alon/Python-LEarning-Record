from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(default=18)
class Department(models.Model):
    title = models.CharField(max_length=16)


#新建数据
Department.objects.create(title='研发部')

UserInfo.objects.create(name='mkk',password='2003815',age=21)
