import json
from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from app01 import models
from app01.utils.bootstrap import BootStrapModelForm

class OrderModelForm(BootStrapModelForm):
    class Meta:
        model = models.Order
        exclude = ['oid']



def order_list(request):
    form = OrderModelForm()
    context = {
        'form': form,
    }
    return render(request,'order_list.html',context)


@csrf_exempt
def order_add(request):
    """创建订单Ajax请求"""
    form = OrderModelForm(data= request.POST)
    if form.is_valid():
        form.save()
        # return HttpResponse(json.dumps({'status': True}))
        return JsonResponse({'status':True})

    return JsonResponse({'status': False,"error": form.errors})