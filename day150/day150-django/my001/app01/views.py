from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("欢迎使用")

def user_list(request):
    #优先去项目的根目录的templates去寻找
    #根据注册表的顺序在每个app的templates目录中去寻找
    #去app01的目录下寻找user_list.html文件
    return render(request,"user_list.html")

def user_add(request):
    return render(request,"user_add.html")

def tpl(request):

    name='韩超'
    roles=['rooter','CEO','keeper']
    user_info={'name':11,'salary':10000,'roles':'CTO'}

    data_list = [
        {'name': '11', 'salary': 10000, 'roles': 'CTO'},
        {'name': '22', 'salary': 9999, 'roles': 'CEO'},
        {'name': '33', 'salary': 8888, 'roles': 'OOO'},
    ]

    return render(
        request,
        'tpl.html',
        {'n1':name,'n2':roles,'n3':user_info,'n4':data_list},
    )

def news(request):
#定义新闻（字典或者列表），或者去数据库   网络请求去获取新闻
    return render(request,"news.html")

def something(request):

    return HttpResponse("返回内容")

from app01.models import Department,UserInfo
def orm(request):
    #测试orm
    Department.objects.create(title='研发部')
    Department.objects.create(title='优化部门')
    Department.objects.create(title='运维部')

    return HttpResponse('success!!!')