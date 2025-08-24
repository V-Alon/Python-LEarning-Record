from os.path import exists
from django.core.validators import RegexValidator
from django.shortcuts import render,redirect
from app01 import models
from django import forms
# Create your views here.
# -----------------部门---------------------
def depart_list(request):
    """部门列表"""
    #去数据库中获取信息列表
    depart_queryset = models.Department.objects.all()

    return render(request,'depart_list.html',{'depart_queryset':depart_queryset})

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

#########################-----  ModelForm   ----#####################################
class UserModelForm(forms.ModelForm):
    name = forms.CharField(min_length=3,label="姓名")

    class Meta:
        model = models.UserInfo
        fields = ['name','password','age','account','create_time','gender','depart']


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        #循环找到所有的插件，添加了class = "form-control"
        for name,field in self.fields.items():
            #如果不想要全部都是一个样式，判断一下
            # if name =="password":
            #     continue
            field.widget.attrs={'class':'form-control'}
#########################-----  ModelForm   ----#####################################

def user_add_model_form(request):
    """添加用户基于ModelForm"""
    if request.method == "GET":
        form = UserModelForm()
        return render(request,'user_add_model_form.html',{'form':form})
    #用户通过post提价数据
    #数据校验！！！
    form = UserModelForm(data=request.POST)
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


        form = UserModelForm(instance=row_object)

        return render(request,'user_edit.html',{'form':form})
    else:

        form = UserModelForm(data=request.POST,instance=row_object)
        if form.is_valid():
            #默认保存的是用户输入的所有数据
            # form.instance.字段名 = 值
            # 比如数据库的修改时间
            # 如果需要用户输入以外再增加值
            form.save()
            return redirect('/user/list')

        return render(request,'user_edit.html',{'form':form})


def user_delete_model_form(request,nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list')


# -------------------靓号-----------------
def pretty_mobile_list(request):
    """靓号列表"""
    """ # q = models.PrettyNumber.objects.filter(**data_dict)
    # data_dict = {mobile="13988888888",id="1"}
    # **     解包
    # q = models.PrettyNumber.objects.filter(mobile="13988888888",id="1")

    # models.PrettyNumber.objects.filter(id = 1)       #等于
    # models.PrettyNumber.objects.filter(id_gt = 1)    #大于
    # models.PrettyNumber.objects.filter(id_gte = 1)   #大于等于
    # models.PrettyNumber.objects.filter(id_lt = 1)    #小于
    # models.PrettyNumber.objects.filter(id_lte = 1)   #小于等于"""
    data_dict = {}
    search_data = request.GET.get('q',"")
    if search_data:
        data_dict["mobile__contains"]=search_data
    #<QuerySet [<PrettyNumber: PrettyNumber object (1)>, <PrettyNumber: PrettyNumber object (2)>]>
    #根据需要访问的页码 计算起始位置  显示不同的界面
    page = int(request.GET.get('page',1))
    page_size =10
    start = (page-1)*page_size
    end = page*page_size





    pretty_mobile_queryset = models.PrettyNumber.objects.filter(**data_dict).order_by('id')[start:end]

    return render(request,'pretty_mobile_list.html',{'pretty_mobile_queryset':pretty_mobile_queryset,'search_data':search_data})


class PrettyModelForm(forms.ModelForm):

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


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs={'class':'form-control'}

    # 验证:方式2
    # 钩子方法
    # 方法名必须是clean_ < 字段名 >，参数只有self
    # 从self.cleaned_data里取字段值
    # 校验失败就抛 forms.ValidationError
    # 最后return 清洗后的值，供后续流程使用
    def clean_mobile(self):



        txt_mobile = self.cleaned_data['mobile']

        models.PrettyNumber.objects.filter(mobile=txt_mobile).exists()
        if exists:
            raise forms.ValidationError('手机号已经存在')

        # if len(txt_mobile) != 11:
        #     # 验证不通过，抛出forms.ValidationError
        #     raise forms.ValidationError("格式错误")
        # # 验证通过
        # return txt_mobile


def pretty_mobile_add(request):
    """添加账号基于ModelForm"""
    if request.method == "GET":
        form = PrettyModelForm()
        return render(request,'pretty_mobile_add.html',{'form':form})

    form = PrettyModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/pretty_mobile/list')

    return render(request,'pretty_mobile_add.html',{'form':form})


def pretty_mobile_edit(request,nid):
    """编辑账号"""
    row_object = models.PrettyNumber.objects.filter(id=nid).first()
    if request.method == "GET":
        # 根据ID去数据库获取信息（对象）

        form = PrettyModelForm(instance=row_object)

        return render(request, 'pretty_mobile_edit.html', {'form': form})
    else:

        form = PrettyModelForm(data=request.POST, instance=row_object)

        if form.is_valid():
            form.save()
            return redirect('/pretty_mobile/list')


def pretty_mobile_delete(request,nid):
    """删除靓号"""
    models.PrettyNumber.objects.filter(id=nid).delete()
    return redirect('/pretty_mobile/list')



