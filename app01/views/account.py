from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect

from app01 import models
from app01.utils.bootstrap import BootStrapForm
from app01.utils.code import check_code
from app01.utils.encrapt import md5


class loginForm(BootStrapForm):
    name = forms.CharField(label="用户名",
                           widget=forms.TextInput
                           )
    pwd = forms.CharField(label="密码",
                          widget=forms.PasswordInput)

    code = forms.CharField(label="验证码",
                           widget=forms.PasswordInput)

    def clean_password(self):
        pwd = self.cleaned_data.get('pwd')
        return md5(pwd)


def login(req):
    if req.method == "GET":
        form = loginForm()
        return render(req, "login.html", {'form': form})
    form = loginForm(data=req.POST)
    if form.is_valid():
        # 获取验证码
        user_inputcode = form.cleaned_data.pop('code')
        # 验证码的叫校验
        Code = req.session.get('image_code', "")
        if Code.upper() != user_inputcode.upper():
            form.add_error("code", '验证码错误')  # 错误信息提示
            return render(req, 'login.html', {'form': form})

        obj = models.admin.objects.filter(**form.cleaned_data).first()
        if not obj:
            form.add_error("pwd", '用户名或者密码错误')  # 错误信息提示
            return render(req, 'login.html', {'form': form})

        # 用户名和密码正确
        # 写到用户浏览器的cookie中,再写入session中
        req.session["info"] = {'id': obj.id, 'name': obj.name}
        #session保存7天
        req.session.set_expiry(60*60*24*7)
        return redirect('/user/list/')
    return render(req, "login.html", {'form': form})


from io import BytesIO


def image_code(req):
    """生成验证码图片"""
    img, code_string = check_code()
    # 写入session 便于后续校验
    req.session["image_code"] = code_string
    # 设置60s失效
    req.session.set_expiry(60)

    stream = BytesIO()
    img.save(stream, 'png')
    return HttpResponse(stream.getvalue())


def logout(req):
    """注销"""
    # 清除掉当前登录用户的session
    req.session.clear()
    return redirect('/login/')
