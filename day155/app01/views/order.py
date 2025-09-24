import json
import random
from datetime import datetime
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from app01 import models
from app01.utils.bootstrap import BootStrapModelForm
from app01.utils.pagination import Pagination


class OrderModelForm(BootStrapModelForm):
    class Meta:
        model = models.Order
        exclude = ['oid', 'admin']


def order_list(request):
    queryset = models.Order.objects.all().order_by('-id')
    page_obj = Pagination(request, queryset)
    form = OrderModelForm()
    context = {
        'form': form,
        'page_string': page_obj.html(),
        'queryset': queryset,
    }
    return render(request, 'order_list.html', context)


@csrf_exempt
def order_add(request):
    """创建订单Ajax请求"""
    form = OrderModelForm(data=request.POST)
    if form.is_valid():
        form.instance.oid = datetime.now().strftime('%Y%m%d%H%M%S') + str(random.randint(1000, 9999))
        # 设置固定管理员ID
        # form.instance.admin_id = 固定的管理员ID   session中获取
        form.instance.admin_id = request.session["info"]["id"]
        # 保存到数据库
        form.save()
        return JsonResponse({'status': True})

    return JsonResponse({'status': False, 'error': form.errors.get_json_data()})


def order_delete(request):
    """删除订单"""
    uid = request.GET.get('uid')
    if not uid:
        return JsonResponse({'status': False, 'error': "缺少订单ID"})

    exists = models.Order.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({'status': False, 'error': "数据不存在"})

    models.Order.objects.filter(id=uid).delete()

    return JsonResponse({'status': True})


def order_detail(request):
    """方式一"""
    """uid = request.GET.get('uid')
    row_object = models.Order.objects.filter(id=uid).first()
    if not row_object:
        return JsonResponse({'status': False, 'error': "数据不存在"})
    result = {
        "status": True,
        "data": {
            'title': row_object.title,
            'price': row_object.price,
            'status': row_object.status,
        }
    }
    return JsonResponse({"status": True, "data": result})"""
    """方式二  """
    uid = request.GET.get('uid')
    row_dict = models.Order.objects.filter(id=uid).values('title','price','status').first()
    if not row_dict:
        return JsonResponse({'status': False, 'error': "数据不存在"})
    result = {
        "status": True,
        "data": row_dict
    }
    return JsonResponse({"status": True, "data": result})

@csrf_exempt
def order_edit(request):
    uid = request.GET.get('uid')
    row_project =  models.Order.objects.filter(id=uid).first()
    if not row_project:
        return JsonResponse({'status':False,'summary':'error!!!'})