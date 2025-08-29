import json
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def task_list(request):
    """任务管理"""
    return render(request,'task_list.html')


@csrf_exempt
def task_ajax(request):
    print(request.GET)     # 浏览器直接访问时能看到
    print(request.POST)
    data = {"status": True, "data": [1, 2, 3, 4]}
    return JsonResponse({'status': True, 'data': list(request.POST.items())})