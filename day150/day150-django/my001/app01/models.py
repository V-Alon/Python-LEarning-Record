from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()



"""
create table app001_userinfo(
    id bigint primary key auto_increment,
    name varchar(32),
    password varchar(64),
    age int
);

"""


