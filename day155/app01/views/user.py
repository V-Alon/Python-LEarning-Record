from django.shortcuts import render, redirect
from app01 import models
from app01.views import UserModelForm

# -------------------员工-----------------
def user_list(request):
    """员工列表"""
    # 去数据库中获取信息列表
    user_queryset = models.UserInfo .objects.all()
    return render(request,'user_list.html',{'user_queryset':user_queryset})

def user_add(request):
    """添加用户"""

    if request.method == "GET":
        content = {
            'gender_choices':models.UserInfo.gender_choice,
            'depart_choices':models.Department.objects.all(),
        }

        return render(request,'user_add.html',content)
    #POST获取用户输入的数据
    username = request.POST.get('username')
    password  =request.POST.get('password')
    age = request.POST.get('age')
    account = request.POST.get('account')
    create_time = request.POST.get('create_time')
    gender = request.POST.get('gender')
    depart_id = request.POST.get('depart')

    #添加到数据库中
    models.UserInfo.objects.create(name=username,password=password,age=age,account=account,
                                   create_time=create_time,gender=gender,depart_id=depart_id)

    #返回到用户列表页面
    return redirect('/user/list')

def user_add_model_form(request):
    """添加用户基于ModelForm"""
    if request.method == "GET":
        form = UserModelForm()
        return render(request,'user_add_model_form.html',{'form':form})
    #用户通过post提价数据
    #数据校验！！！
    form = UserModelForm(data=request.POST,)
    if form.is_valid():
        #如果数据合法，保存到数据库
        # models.UserInfo.objects.create(**form.cleaned_data)
        form.save()
        return redirect('/user/list')

        #如果校验失败，在页面显示错误信息
    return render(request,'user_add_model_form.html',{'form':form})

def user_edit_model_form(request,nid):
    """编辑用户"""
    row_object = models.UserInfo.objects.filter(id=nid).first()
    if request.method == "GET":
    #根据ID去数据库获取信息（对象）


        form = UserModelForm(instance=row_object,)

        return render(request,'user_edit.html',{'form':form})
    else:

        form = UserModelForm(data=request.POST,instance=row_object,)
        if form.is_valid():
            #默认保存的是用户输入的所有数据
            # form.instance.字段名 = 值
            # 比如数据库的修改时间
            # 如果需要用户输入以外再增加值
            form.save()
            return redirect('/user/list')

        return render(request,'user_edit.html',{'form':form})

def user_delete_model_form(nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list')