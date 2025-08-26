from django import forms
from django.core.validators import RegexValidator
from app01 import models
from app01.utils.bootstrap import BootStrapModelForm
# Create your views here.

#########################-----  ModelForm   ----#####################################
class UserModelForm(BootStrapModelForm):
    name = forms.CharField(min_length=3,label="姓名",widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = models.UserInfo
        fields = ['name','password','age','account','create_time','gender','depart']

#########################-----  ModelForm   ----#####################################
class PrettyModelForm(BootStrapModelForm):

    # 验证:方式1
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$','请输入以1开头、第二位为3-9的11位手机号')],
        # disabled=True,不可修改
    )
    class Meta:
        model = models.PrettyNumber
        fields = ['mobile','price','level','status']
        # 所有字段    __all__
        # fields = "__all__"
        # 屏蔽某一个字段
        # exclude = ['mobile']


    # 验证:方式2
    # 钩子方法
    # 方法名必须是clean_ < 字段名 >，参数只有self
    # 从self.cleaned_data里取字段值
    # 校验失败就抛 forms.ValidationError
    # 最后return 清洗后的值，供后续流程使用
    def clean_mobile(self):
        txt_mobile = self.cleaned_data['mobile']

        # 排除当前正在编辑的这条记录
        qs = models.PrettyNumber.objects.filter(mobile=txt_mobile)
        if self.instance.pk:  # 编辑时 instance.pk 有值
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise forms.ValidationError('手机号已存在')

        return txt_mobile





