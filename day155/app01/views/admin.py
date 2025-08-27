from django.shortcuts import render,redirect
from app01 import models
from app01.utils.pagination import Pagination


def admin_list(request):
    """管理员列表"""
    queryset = models.Admin.objects.all()

    page_object = Pagination(request, queryset)

    context = {
        'queryset': queryset,
        'page_string': page_object.html(),
    }

    return render(request,'admin_list.html',context)


from app01.utils.bootstrap import BootStrapModelForm
from django import forms
from django.core.exceptions import ValidationError
from app01.utils.encrypt import md5

class AdminModeForm(BootStrapModelForm):

    confirm_password = forms.CharField(label="确认密码",widget=forms.PasswordInput)

    class Meta:
        model = models.Admin
        fields = ["username", "password", "confirm_password"]
        widgets = {"password": forms.PasswordInput}
        #可以在PasswordInput后夹砂管加上render_value=True
        #密码校验错误后原来输入的可以保留

    def clean_password(self):
        password = self.cleaned_data.get('password')





        return md5(password)

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = md5(self.cleaned_data.get('confirm_password'))
        if password != confirm_password:
            raise ValidationError("密码不一致")
        #返回什么，保存到数据库就是什么
        return confirm_password


class AdminEditModelForm(BootStrapModelForm):
    class Meta:
        model = models.Admin
        fields = ["username"]

class AdminResetModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(label="确认密码", widget=forms.PasswordInput)
    class Meta:
        model = models.Admin
        fields = ["password", "confirm_password"]
        widgets = {"password": forms.PasswordInput}

    def clean_password(self):
        password = self.cleaned_data.get('password')
        md5_password = md5(password)

        #去数据库校验和新输入的密码是否相同
        exists = models.Admin.objects.filter(id = self.instance.pk,password=md5_password).exists()
        if exists:
            error = "密码不可以和之前一样"
            raise ValidationError(error)
        return md5(password)

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = md5(self.cleaned_data.get('confirm_password'))
        if password != confirm_password:
            raise ValidationError("密码不一致")
        #返回什么，保存到数据库就是什么
        return confirm_password

def admin_add(request):
    """添加管理员"""
    title = "添加管理员"
    if request.method == "GET":
        form = AdminModeForm()
        return render(request, 'change.html', {"title": title, "form": form})

    form = AdminModeForm(data = request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')\

    return render(request, 'change.html', {"title": title, "form": form})

def admin_edit(request,nid):
    """编辑管理员"""
    #对象或者None
    row_obj = models.Admin.objects.filter(id=nid).first()
    if row_obj is None:
        error = "!!!ERROR!!!"
        # return render(request, 'error.html',{"error":error})
        return redirect('/admin/list/')

    title = "编辑管理员"

    if request.method == "GET":
        form = AdminEditModelForm(instance=row_obj)
        return render(request, 'change.html', {"title": title, "form": form})

    form = AdminEditModelForm(data = request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, 'change.html', {"title": title, "form": form})

def admin_delete(request,nid):
    """删除管理员"""
    models.Admin.objects.filter(id=nid).delete()
    return redirect('/admin/list/')

def admin_reset(request,nid):
    """重置密码"""
    # 对象或者None
    row_obj = models.Admin.objects.filter(id=nid).first()
    if row_obj is None:
        return redirect('/admin/list/')
    title = "重置密码 - {}".format(row_obj.username)

    if request.method == "GET":
        form = AdminResetModelForm()
        return render(request, 'change.html', {"title": title, "form": form})

    form = AdminResetModelForm(data = request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, 'change.html', {"title": title, "form": form})
