from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=255,unique=True,verbose_name="用户昵称")
    age = models.IntegerField(default=18,verbose_name="用户年龄")
    gender = models.CharField(max_length=10,default="男",verbose_name="用户性别")
    header = models.ImageField(upload_to="static/images/headers",default="static/images/headers/beibei.png",verbose_name="用户头像")
    phone = models.IntegerField(max_length=50,default=123456,verbose_name="用户手机号码")


    # 和系统内置的用户管理建立一对一的关系
    user = models.OneToOneField(User,on_delete=models.CASCADE)

