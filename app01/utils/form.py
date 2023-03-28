from app01 import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django import forms
from app01.utils.bootstrap import BootStrapModelForm
from app01.utils.encrapt import md5


class UserModelForm(BootStrapModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age", "gender", "depart", "create_time", "account"]



class numform(BootStrapModelForm):
    # mobile = forms.CharField(
    #     label="手机号",
    #     validators=[RegexValidator("/^1[3456789]\d{9}$/","手机号格式错误")]
    # )
    class Meta:
        model = models.PrettyNum
        fields = ["mobile", "price", "level", "status"]


    def clean_mobile(self):
        txt_mobile = self.cleaned_data["mobile"]
        # self.instance.pk 获取当前id
        exists = models.PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
        if (exists):
            raise ValidationError("手机号已存在")
        if len(txt_mobile) != 11:
            raise ValidationError("格式错误")
        return txt_mobile;


class rest(BootStrapModelForm):
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.admin
        fields = ['pwd', 'confirm_password']
        widgets = {
            "pwd": forms.PasswordInput(render_value=True)
        }

    def clean_pwd(self):
        pwd = self.cleaned_data.get("pwd")
        md5_pwd = md5(pwd)

        # 去数据库校验当前密码和新输入的密码是否一致
        exists = models.admin.objects.filter(id=self.instance.pk, pwd=md5_pwd).exists()
        if exists:
            raise ValidationError("不能与以前的密码相同")

        return md5_pwd

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("pwd")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            raise ValidationError("密码不一致")
        # 返回什么，此字段以后保存到数据库就是什么。
        return confirm

class AdminModelFrom(BootStrapModelForm):
    confirm_pwd = forms.CharField(label="确认密码",
                                  widget=forms.PasswordInput)

    class Meta:
        model = models.admin
        fields = ["name", "pwd", "confirm_pwd"]
        widgets = {
            "pwd": forms.PasswordInput
        }

    def clean_pwd(self):
        pwd = self.cleaned_data.get("pwd")
        return md5(pwd)

    def clean_confirm_pwd(self):
        pwd = self.cleaned_data.get("pwd")
        confirm = md5(self.cleaned_data.get("confirm_pwd"))
        if confirm != pwd:
            raise ValidationError("密码不一致")
        return confirm


class Admin_Edit(BootStrapModelForm):
    class Meta:
        model = models.admin
        fields = ["name"]