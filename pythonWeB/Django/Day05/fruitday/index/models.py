from django.db import models

# Create your models here.
# 用户实体
class Users(models.Model):
    # 电话号码 - CharField()
    uphone = models.CharField(max_length=11)
    # 密码 - CharField()
    upwd = models.CharField(max_length=30)
    # 电子邮件 - EmailField()
    uemail = models.EmailField()
    # 用户名 - CharField()
    uname = models.CharField(max_length=20)
    # 启用/禁用 - BooleanField(),默认值为True
    isActive = models.BooleanField(default=True)

# 商品类型 Models

class GoodsType(models.Model):
    title = models.CharField(max_length=40)
    picture = models.ImageField(upload_to='static/upload/goodstype')
    desc = models.TextField()

# 商品 Models
class Goods(models.Model):
    title = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    spec = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='static/upload/goods')
    isActive = models.BooleanField(default=True)