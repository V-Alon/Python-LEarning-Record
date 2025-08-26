"""
URL configuration for day155 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path

from app01.views import depart, user, pretty, admin

urlpatterns = [
       # path('admin/', admin.site.urls),
    #部门管理
    path('depart/list/', depart.depart_list),
    path('depart/add/', depart.depart_add),
    path('depart/delete/', depart.depart_delete),
    path('depart/<int:nid>/edit/', depart.depart_edit),



    #员工管理
    path('user/list/', user.user_list),
    path('user/add/', user.user_add),
    path('user/add/model/form/', user.user_add_model_form),
    path('user/<int:nid>/edit/', user.user_edit_model_form),
    path('user/<int:nid>/delete/', user.user_delete_model_form),


    #靓号管理
    path('pretty_mobile/list/', pretty.pretty_mobile_list),
    path('pretty_mobile/add/', pretty.pretty_mobile_add),
    path('pretty_mobile/<int:nid>/edit/', pretty.pretty_mobile_edit),
    path('pretty_mobile/<int:nid>/delete/', pretty.pretty_mobile_delete),


    #管理员
    path('admin/list/',admin.admin_list),
    path('admin/add/',admin.admin_add),



]
