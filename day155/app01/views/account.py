from django.shortcuts import render,redirect,HttpResponse
from django import forms
from io import BytesIO


from app01 import models
from app01.utils.bootstrap import BootStrapForm
from app01.utils.encrypt import md5
from app01.utils.code import check_code

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
    code = forms.CharField(
        widget=forms.TextInput,
        label="验证码",
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
        user_input_code = form.cleaned_data.pop('code')
        code = request.session.get('image_code',"")
        if code.upper()!=user_input_code.upper():
            form.add_error("code", "验证码错误")
            return render(request,'login.html',{'form':form})

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
        request.session.set_expiry(60*60*24*3)
        #三天免登录，session保存三天


        return redirect("/admin/list/")
    return render(request,'login.html',{'form':form})


def image_code(request):
    """生成图片验证码"""
    img,code_string= check_code()

    # 写入到session中保存起来
    request.session['image_code'] = code_string
    # 给session设置60S超时
    request.session.set_expiry(60)

    stream = BytesIO()
    img.save(stream, 'png')
    stream.getvalue()
    return HttpResponse(stream.getvalue())


def logout(request):
    """注销"""

    request.session.clear()

    return redirect("/login/")


