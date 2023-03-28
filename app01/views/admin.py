
from django.shortcuts import render, redirect

from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.form import Admin_Edit,AdminModelFrom,rest

"""管理员列表"""


def admin_list(req):
    #检查用户是否已经登陆，若未登录则跳转回登陆界面
    #获取cookie中的随机字符串，看看session里有没有，若有则

    data_dict = {}
    search_data = req.GET.get('q', "")
    if search_data:
        data_dict = {"mobile__contains": search_data}

    queryset = models.admin.objects.filter(**data_dict);

    page_object = Pagination(req, queryset)
    context = {
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }
    return render(req, 'admin_list.html', context)


def admin_add(req):
    title = "新建广利源"
    if req.method == "GET":
        form = AdminModelFrom()
        return render(req, "admin_add.html", {"form": form, "title": title})
    form = AdminModelFrom(data=req.POST)
    if form.is_valid():
        form.save()
        return redirect("/admin/list/")

    return render(req, "admin_add.html", {"form": form, "title": title})


def admin_edit(req, nid):
    row_obj = models.admin.objects.filter(id=nid).first()
    if not row_obj:
        return redirect('/admin/lsit/')

    title = "编辑管理员"
    if req.method == "GET":
        form = Admin_Edit(instance=row_obj)
        return render(req, 'admin_edit.html', {'form': form, 'title': title})
    form = Admin_Edit(data=req.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect("/admin/list/")
    return render(req, 'admin_edit.html', {'form': form, 'title': title})


def admin_delete(req, nid):
    models.admin.objects.filter(id=nid).delete()
    return redirect("/admin/list")





def admin_reset(req, nid):
    """重置密码"""
    row_obj = models.admin.objects.filter(id=nid).first()
    if not row_obj:
        return redirect('/admin/lsit/')
    title = "重置密码 -{}".format(row_obj.name)
    if req.method == "GET":
        form = rest()
        return render(req, 'admin_reset.html', {'form': form, 'title': title})
    form = rest(data=req.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect('/admin/list')
    return render(req, 'admin_reset.html', {'form': form, 'title': title})
