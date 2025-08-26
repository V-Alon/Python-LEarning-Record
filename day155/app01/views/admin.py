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
class AdminModeForm(BootStrapModelForm):

    confirm_password = forms.CharField(label="确认密码",widget=forms.PasswordInput)

    class Meta:
        model = models.Admin
        fields = ["username", "password", "confirm_password"]
        widgets = {"password": forms.PasswordInput}
        #可以在PasswordInput后夹砂管加上render_value=True
        #密码校验错误后原来输入的可以保留
    def clean_password(self):
        






    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
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



