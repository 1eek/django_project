# Generated by Django 4.1.7 on 2023-03-18 07:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app01", "0003_prettynum"),
    ]

    operations = [
        migrations.CreateModel(
            name="admin",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=32, verbose_name="用户名")),
                ("pwd", models.CharField(max_length=64, verbose_name="密码")),
            ],
        ),
    ]
