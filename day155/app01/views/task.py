import json
from django import forms
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from app01.utils.bootstrap import BootStrapModelForm
from app01 import models
from app01.utils.pagination import Pagination          # ★1. 引入分页器

class TaskModelForm(BootStrapModelForm):               # 顺手把 From 改成 Form
    class Meta:
        model = models.Task
        fields = "__all__"
        widgets = {
            "detail": forms.TextInput()
        }


def task_list(request):
    """任务列表"""
    queryset = models.Task.objects.all().order_by('-id')

    # ★2. 用分页器包装 queryset
    page_obj = Pagination(request, queryset, page_size=10)  # 每页 10 条，可按需改
    page_queryset = page_obj.page_queryset                   # 已切片的数据

    form = TaskModelForm()
    context = {
        'queryset': page_queryset,   # ★3. 把切片后的数据给模板
        'form': form,
        'pager': page_obj,           # ★4. 把分页 html 给模板
    }
    return render(request, 'task_list.html', context)


@csrf_exempt
def task_ajax(request):
    print(request.GET)
    print(request.POST)
    return JsonResponse({'status': True, 'data': list(request.POST.items())})


@csrf_exempt
def task_add(request):
    form = TaskModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, 'error': form.errors}, json_dumps_params={'ensure_ascii': False})