from django.shortcuts import render, redirect
from app01 import models
from app01.views import PrettyModelForm


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

    from app01.utils.pagination import Pagination

    pretty_mobile_queryset = models.PrettyNumber.objects.filter(**data_dict).order_by('id')

    page_object = Pagination(request, pretty_mobile_queryset)


    context = {
        'search_data': search_data,

        'pretty_mobile_queryset':page_object.page_queryset,#分完页的数据

        'page_string':page_object.html()#生成的页码
    }

    return render(request,'pretty_mobile_list.html',context)

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
    return render(request, 'pretty_mobile_edit.html', {'form': form})

def pretty_mobile_delete(nid):
    """删除靓号"""
    models.PrettyNumber.objects.filter(id=nid).delete()
    return redirect('/pretty_mobile/list')
