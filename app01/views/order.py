import random
from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from app01 import models
from app01.utils.bootstrap import BootStrapModelForm
from app01.utils.pagination import Pagination


class OrderModelForm(BootStrapModelForm):
    class Meta:
        model = models.Order
        exclude = ["num", "admin"]


def order_list(req):
    form = OrderModelForm()
    queryset = models.Order.objects.all()
    page_object = Pagination(req, queryset)

    context = {
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html(),  # 生成页码
        "form": form
    }
    return render(req, 'order_list.html', context)


@csrf_exempt
def order_add(req):
    """新建订单"""
    form = OrderModelForm(data=req.POST)
    if form.is_valid():
        # 添加订单号
        form.instance.num = datetime.now().strftime("%Y%M%D%H%M%S") + str(random.randint(1000, 9999))
        # 管理员id 为当前登录管理员的id
        form.instance.admin_id = req.session["info"]["id"]
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, "error": form.errors})


@csrf_exempt
def order_delete(req):
    # 获取id
    uid = req.GET.get('uid')
    # 判断数据是否存在
    exists = models.Order.objects.filter(id=uid).exists()
    # 若不存在返回错误信息
    if not exists:
        return JsonResponse({"status": False, 'error': "数据不存在"})
    # 存在则删除
    models.Order.objects.filter(id=uid).delete()
    return JsonResponse({'status': True})


@csrf_exempt
def order_detail(req):
    # 获取id
    uid = req.GET.get('uid')
    obj = models.Order.objects.filter(id =uid).values("name","price",'status').first()
    if not obj:
        return JsonResponse({'status':False,'error':"数据不存在"})
    result={
        "status":True,
        "data":obj,
    }
    return JsonResponse(result)

@csrf_exempt
def order_edit(req):
    uid = req.GET.get("uid")
    obj = models.Order.objects.filter(id=uid).first()
    if not obj:
        return JsonResponse({"status":False,'tips':"数据不存在,请刷新重试"})

    form = OrderModelForm(data=req.POST,instance=obj)
    if form.is_valid():
        form.save()
        return JsonResponse({"status":True})
    return JsonResponse({"status":False,'error':form.errors})



