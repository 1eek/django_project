# django_project
1. 新建项目

```
django-admin startproject HelloWorld
```

2. 注册app

```
python manage.py startapp app01;
```


3. 修改数据库的配置

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_test',  # 数据库名字
        'USER': 'root',
        'PASSWORD': '713328911hqh',
        'HOST': '127.0.0.1',  # 那台机器安装了MySQL
        'PORT': 3306,
    }
}
```

4. Django命令生成数据表

```
python manage.py makemigrations
python manage.py migrate
```

