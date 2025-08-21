from django.shortcuts import render,redirect
from app01 import models
# Create your views here.
# --部门--
def depart_list(request):
    """部门列表"""
    #去数据库中获取信息列表
    queryset = models.Department.objects.all()



    return render(request,'depart_list.html',{'queryset':queryset})

def depart_add(request):
    """添加部门"""
    if request.method == "GET":
        return render(request,'depart_add.html')
    #获取用户post的数据(输入为空)
    title = request.POST.get('title')

    #保存到数据库
    models.Department.objects.create(title=title)

    #重定向回部门列表
    return redirect('/depart/list')

def depart_delete(request):
    """删除功能"""
    #获取ID
    #http://127.0.0.1:8000/depart/delete/?nid=1
    nid = request.GET.get('nid')
    #删除
    models.Department.objects.filter(id=nid).delete()
    #跳转回部门列表
    return redirect('/depart/list')

def depart_edit(request,nid):
    """修改部门"""
    if request.method == "GET":
        #根据nid获取数据
        row_object = models.Department.objects.filter(id=nid).first()
        return render(request, 'depart_edit.html', {'row_object':row_object})

    #获取用户输入的标题
    title = request.POST.get('title')
    #根据ID找到数据库中的数据并且进行更新
    models.Department.objects.filter(id=nid).update(title=title)
    #跳转回部门列表
    return redirect('/depart/list')

# --员工--
def user_list(request):
    """员工列表"""

    return render(request,'user_list.html')