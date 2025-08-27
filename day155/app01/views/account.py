from django.shortcuts import render,redirect,HttpResponse
from django import forms

from app01 import models
from app01.utils.bootstrap import BootStrapForm
from app01.utils.encrypt import md5

class LoginForm(BootStrapForm):
    username = forms.CharField(
        widget=forms.TextInput,
        label="用户名",
        required=True
    )

    password = forms.CharField(
        widget=forms.PasswordInput,#PasswordInput(render_value=True)需要保留原来输入的密码的话
        label="密码",
        required=True
    )
    def clean_password(self):
        password = self.cleaned_data.get('password')
        return md5(password)


def login(request):
    """登陆页面"""
    if request.method == "GET":
        form = LoginForm()
        return render(request,'login.html',{'form':form})
    form = LoginForm(data=request.POST)
    if form.is_valid():
        #验证成功

        #数据库校验用户名和密码是否正确，获取用户对象
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            #用户名和密码错误
            form.add_error("password", "用户名和密码错误")
            return render(request,'login.html',{'form':form})

        # 用户名和密码正确
        # 网站生成随机字符串     写入浏览器的cookie和session
        request.session['info'] = {"id":admin_object.id ,"name":admin_object.username}
        #sessionid = fj449evj6tlvk8ly03e1je58bg4z2rgf



        return redirect("/admin/list/")
    return render(request,'login.html',{'form':form})