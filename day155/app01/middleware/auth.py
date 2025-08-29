'django.middleware.common.CommonMiddleware'
from contextlib import redirect_stderr

from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

class AuthMiddleware(MiddlewareMixin):
    """中间件"""
    def process_request(self, request):
        #  0排除不需要登录的
        if request.path_info in ['/login/','/image/code/','/task/ajax/']:
            return None


        #如果没有返回值，返回None，继续向后走
        #如果有返回值,不再继续。直接返回给用户
        #  1读取用户session信息
        info_dict =  request.session.get('info')
        if info_dict:
            return
        #  2没有登陆
        return redirect('/login/')



# class M2(MiddlewareMixin):
#     def process_request(self, request):
#         print('process_request2')
#
#     def process_response(self, request, response):
#         print('process_response2')
#         return response
