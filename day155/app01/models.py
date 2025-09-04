from ssl import cert_time_to_seconds

from django.db import models

# Create your models here.

class Admin(models.Model):
    objects = models.Manager()
    username = models.CharField(max_length=32,verbose_name="管理员账号")
    password = models.CharField(verbose_name="密码", max_length=64)

    def __str__(self):
        return self.username


class Department(models.Model):
    """部门表"""
    # id = models.BigAutoField(primary_key=True,verbose_name="ID")
    title = models.CharField(max_length=32,verbose_name="标题")
    def __str__(self):
        return self.title

    objects = models.Manager()


class UserInfo(models.Model):
    """员工表"""
    name = models.CharField(verbose_name="姓名",max_length=16)
    password = models.CharField(verbose_name="密码",max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="账户余额",max_digits=10,decimal_places=2,default=0)
    create_time = models.DateField(verbose_name="入职时间")


    #无约束
    # depart_id = models.BigAutoField(verbose="部门ID")

    #1.有约束
    # --to 与那个表进行关联
    # --to_field 与哪一列做关联
    #2.django自动
    # -- 写的depart
    # --生成数据列 depart_id
    # 3. 部门被删除
    # --1.级联删除
    depart = models.ForeignKey(to=Department, to_field="id", on_delete=models.CASCADE,verbose_name="部门")
    # --2.设置成空的
    #    depart = models.ForeignKey(to=Department,to_field="id",null=True,blank=True,on_delete=models.SET_NULL)
    #
    #django中的约束
    gender_choice = (
        (1,'男'),
        (2,'女')
    )


    gender = models.SmallIntegerField(verbose_name="性别",choices=gender_choice)
    objects = models.Manager()


class PrettyNumber(models.Model):
    """靓号表"""
    mobile = models.CharField(verbose_name="靓号",max_length=11)
    #想要允许为空，可以设置，    null=True,blank = True
    price = models.IntegerField(verbose_name="价格")
    level_choices = (
        (1,'D'),
        (2,'C'),
        (3,'B'),
        (4,'A'),
        (5,'S')
    )
    level = models.SmallIntegerField(verbose_name="级别",choices=level_choices)
    status_choices = (
        (0,'未占用'),
        (1,'已占用')
    )
    status = models.SmallIntegerField(verbose_name="状态",choices=status_choices,default=0)
    objects = models.Manager()


class Task(models.Model):
    """任务"""
    level_choices = (
        (1,"S"),
        (2,"A"),
        (3,"B"),
    )
    level = models.SmallIntegerField(verbose_name="级别",choices=level_choices)
    title = models.CharField(verbose_name="标题",max_length=64)
    detail = models.TextField(verbose_name="详细信息")
    user = models.ForeignKey(verbose_name="负责人",to="Admin",to_field="id",on_delete=models.CASCADE)


class Order(models.Model):
    """工单"""
    oid = models.CharField(verbose_name="订单号",max_length=64)
    title = models.CharField(verbose_name="名称",max_length=32)
    price = models.CharField(verbose_name="价格",max_length=32)
    status_choices = (
        (0,"未支付"),
        (1,"已支付"),
    )

    status = models.CharField(verbose_name="状态",max_length=32,choices=status_choices)
    admin = models.ForeignKey(verbose_name="管理员",to="Admin",on_delete=models.CASCADE)