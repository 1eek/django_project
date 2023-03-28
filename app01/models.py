from django.db import models


# Create your models here.
class Department(models.Model):
    """部门表"""
    title = models.CharField(verbose_name="标题", max_length=32)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """员工表"""
    name = models.CharField(verbose_name="姓名", max_length=16)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="账户余额", max_digits=10, decimal_places=2, default=0)
    create_time = models.DateField(verbose_name="入职时间")
    # 将两个表关联
    # -to 与哪张表关联
    # -to_filed表中哪一列
    # django自动生成 depart_id
    # 级联删除，删除部门的话就删除该部门下的用户 on_delete=models.CASCADE
    # 置空SET_NULL()
    depart = models.ForeignKey(verbose_name="部门", to="Department", to_field="id", on_delete=models.CASCADE)
    gender_choice = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choice)


class PrettyNum(models.Model):
    mobile = models.CharField(verbose_name="手机号", max_length=11)
    price = models.IntegerField(verbose_name="价格", default=0)
    level_choice = (
        (1, "一级"),
        (2, "二级"),
        (3, "三级"),
        (4, "四级"),
    )
    level = models.SmallIntegerField(verbose_name="等级", choices=level_choice, default=1)
    status_choices = (
        (1, "已使用"),
        (2, "未使用"),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices, default=2)


class admin(models.Model):
    name = models.CharField(verbose_name="用户名", max_length=32)
    pwd = models.CharField(verbose_name="密码", max_length=64)


class Order(models.Model):
    """工单"""
    num = models.CharField(verbose_name="订单号", max_length=64)
    name = models.CharField(verbose_name="商品名称", max_length=32)
    price = models.IntegerField(verbose_name="价格")
    status_choice = (
        (1, "已支付"),
        (2, "未支付"),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choice)
    admin = models.ForeignKey(verbose_name="管理员",to=admin,on_delete=models.CASCADE )