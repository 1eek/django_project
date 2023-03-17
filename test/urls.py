"""test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app01.views import depart,user,pretty
from app01 import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("depart/list/", depart.depart_list),
    path("depart/add/", depart.depart_add),
    path("depart/delete/", depart.depart_delete),
    path("depart/<int:nid>/edit/", depart.depart_edit),
    path("user/list/", user.user_list),
    path("user/add/", user.user_add),
    path("user/model/form/add/", user.user_formadd),
    path("user/<int:nid>/edit/", user.user_edit),
    path("user/<int:nid>/delete/", user.user_delete),
    path("num/list/", pretty.num_list),
    path("num/add/", pretty.num_add),
    path("num/<int:nid>/edit",pretty.num_edit),
    path("num/<int:nid>/delete",pretty.num_delete),

]
