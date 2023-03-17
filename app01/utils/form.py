from app01 import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django import forms
from app01.utils.bootstrap import BootStrapModelForm

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



