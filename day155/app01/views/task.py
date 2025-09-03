import json
from django import forms
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from app01.utils.bootstrap import BootStrapModelForm
from app01 import models

class TaskModelFrom(BootStrapModelForm):
    class Meta:
        model = models.Task
        fields ="__all__"
        widgets = {
            "detail" : forms.TextInput()
        }





def task_list(request):
    """任务列表"""
    queryset = models.Task.objects.all().order_by('-id')



    form = TaskModelFrom()
    context = {
        'queryset': queryset,
        'form': form,
    }
    return render(request,'task_list.html',context)


@csrf_exempt
def task_ajax(request):
    print(request.GET)     # 浏览器直接访问时能看到
    print(request.POST)
    data = {"status": True, "data": [1, 2, 3, 4]}
    return JsonResponse({'status': True, 'data': list(request.POST.items())})


@csrf_exempt
def task_add(request):
    # print(request.POST)
    #校验
    form = TaskModelFrom(data=request.POST)
    if form.is_valid():
        form.save()
        data_dict = {"status": True}
        return HttpResponse(json.dumps(data_dict))

    data_dict = {"status": False,'error':form.errors}
    return HttpResponse(json.dumps(data_dict,ensure_ascii=False))

