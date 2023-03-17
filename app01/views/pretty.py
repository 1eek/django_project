
from django.shortcuts import render, redirect
from app01.utils.form import UserModelForm,numform
from app01 import models
from app01.utils.pagination import Pagination


# Create your views here.






def num_list(req):

    data_dict = {}
    search_data = req.GET.get('q', "")
    if search_data:
        data_dict = {"mobile__contains": search_data}
    #获取数据库中的数据
    queryset = models.PrettyNum.objects.filter(**data_dict).order_by("-level")
    page_object = Pagination(req, queryset)

    context = {
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }
    return render(req, 'num_list.html', context)



def num_add(req):
    if (req.method == "GET"):
        form = numform()
        return render(req, "num_add.html", {"form": form})
    # return redirect("/user/list")
    form = numform(data=req.POST)
    if form.is_valid():
        # 如果数据合法，保存到数据库
        form.save()
        return redirect("/num/list")
    else:
        return render(req, "num_add.html", {"form": form})


def num_edit(req, nid):
    row_obj = models.PrettyNum.objects.filter(id=nid).first()
    if (req.method == "GET"):
        form = numform(instance=row_obj)
        return render(req, "num_edit.html", {'form': form})
    form = numform(data=req.POST, instance=row_obj)
    if (form.is_valid()):
        form.save()
        return redirect("/num/list/")
    return render(req, "num_edit.html", {'form': form})


def num_delete(req, nid):
    models.PrettyNum.objects.filter(id=nid).delete()
    return redirect("/num/list/")