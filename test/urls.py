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
from django.urls import path

from app01.views import depart, user, pretty, admin, account,order,chart

urlpatterns = [
    # path("admin/", admin.site.urls),

    # 部门
    path("depart/list/", depart.depart_list),
    path("depart/add/", depart.depart_add),
    path("depart/delete/", depart.depart_delete),
    path("depart/<int:nid>/edit/", depart.depart_edit),
    path("depart/multi/", depart.depart_multi),

    # 用户
    path("user/list/", user.user_list),
    path("user/add/", user.user_add),
    path("user/model/form/add/", user.user_formadd),
    path("user/<int:nid>/edit/", user.user_edit),
    path("user/<int:nid>/delete/", user.user_delete),

    # 靓号
    path("num/list/", pretty.num_list),
    path("num/add/", pretty.num_add),
    path("num/<int:nid>/edit", pretty.num_edit),
    path("num/<int:nid>/delete", pretty.num_delete),

    # 管理员
    path("admin/list/", admin.admin_list),
    path("admin/add/", admin.admin_add),
    path("admin/<int:nid>/edit/", admin.admin_edit),
    path("admin/<int:nid>/delete", admin.admin_delete),
    path("admin/<int:nid>/reset", admin.admin_reset),

    #登陆界面
    path("login/", account.login),
    path("logout/", account.logout),
    path("image/code/", account.image_code),

    #订单管理
    path("order/list/",order.order_list),
    path("order/add/", order.order_add),
    path("order/delete/", order.order_delete),
    path("order/detail/", order.order_detail),
    path("order/edit/",order.order_edit),

    path('chart/list/', chart.chart_list),
    path('chart/bar/', chart.chart_bar),
    path('chart/pie/', chart.chart_pie),
    path('chart/line/', chart.chart_line),
    path('chart/highcharts/', chart.highcharts),
]
