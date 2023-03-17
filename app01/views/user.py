
from django.shortcuts import render, redirect
from app01.utils.form import UserModelForm,numform
from app01 import models
from app01.utils.pagination import Pagination


# Create your views here.




def user_list(req):
    queryset = models.UserInfo.objects.all()
    return render(req, "user_list.html", {'queryset': queryset})


def user_add(req):
    """添加用户"""
    context = {
        "gender_choices": models.UserInfo.gender_choice,
        "depart_list": models.Department.objects.all()
    }
    if (req.method == "GET"):
        return render(req, "user_add.html", context)
    user = req.POST.get("user")
    pwd = req.POST.get("pwd")
    age = req.POST.get("age")
    account = req.POST.get("ac")
    time = req.POST.get("ctime")
    gender = req.POST.get("gd")
    depart = req.POST.get("dp")
    models.UserInfo.objects.create(
        name=user, password=pwd,
        age=age, account=account,
        create_time=time, gender=gender,
        depart_id=depart)
    return redirect("/user/list/")



def user_formadd(req):
    """添加用户"""
    if (req.method == "GET"):
        form = UserModelForm()
        return render(req, "user_model_form_add.html", {"form": form})
    # return redirect("/user/list")
    form = UserModelForm(data=req.POST)
    if form.is_valid():
        # 如果数据合法，保存到数据库
        form.save()
        return redirect("/user/list")
    else:
        return render(req, "user_model_form_add.html", {"form": form})


def user_edit(req, nid):
    row_obj = models.UserInfo.objects.filter(id=nid).first()
    if (req.method == "GET"):
        form = UserModelForm(instance=row_obj)
        return render(req, "user_edit.html", {'form': form})
    form = UserModelForm(data=req.POST, instance=row_obj)
    if (form.is_valid()):
        form.save()
        return redirect("/user/list/")
    return render(req, "user_edit.html", {'form': form})


def user_delete(req, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list/")