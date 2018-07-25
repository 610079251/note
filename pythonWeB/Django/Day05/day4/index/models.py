from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    website = models.URLField()


class Author(models.Model):
    # name - 姓名,字符串
    name = models.CharField(max_length=30)
    # age - 年龄,整数
    age = models.IntegerField()
    # email - 邮箱,字符串,允许为空
    email = models.EmailField(null=True)
    # gender - 性别,BooleanField
    # gender = models.BooleanField(default=True)


class Book(models.Model):
    title = models.CharField(max_length=50)
    publicate_date = models.DateField()
