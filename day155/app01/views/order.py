import json
import random
from datetime import datetime
from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from app01 import models
from app01.utils.bootstrap import BootStrapModelForm
from app01.utils.pagination import Pagination



class OrderModelForm(BootStrapModelForm):
    class Meta:
        model = models.Order
        exclude = ['oid','admin']



def order_list(request):
    queryset = models.Order.objects.all().order_by('-id')
    page_obj = Pagination(request, queryset)
    form = OrderModelForm()
    context = {
        'form': form,
        'page_string': page_obj.html(),
        'queryset': queryset,
    }
    return render(request,'order_list.html',context)


@csrf_exempt
def order_add(request):
    """创建订单Ajax请求"""
    form = OrderModelForm(data=request.POST)
    if form.is_valid():
        form.instance.oid = datetime.now().strftime('%Y%m%d%H%M%S') + str(random.randint(1000,9999))
        #设置固定管理员ID
        # form.instance.admin_id = 固定的管理员ID   session中获取
        form.instance.admin_id = request.session["info"]["id"]
        #保存到数据库
        form.save()
        return JsonResponse({'status': True})

    return JsonResponse({'status': False, 'error': form.errors.get_json_data()})