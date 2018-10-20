from django.db import models


from store.models import Store



class GoodType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,unique=True,verbose_name="商品类型名称")
    cover = models.ImageField(upload_to="static/images/goods",default="static/images/goods/default.png",verbose_name="商品类型图片")
    intro = models.TextField(verbose_name="商品类别描述")
    parent = models.ForeignKey("self",null=True,blank=True,verbose_name="父级类型",on_delete=models.CASCADE)



class Goods(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,verbose_name="商品名称")
    # max_digits：有效位数  decimal_places:保留小数位
    # price = models.DecimalField(max_digits=8,decimal_places=2)
    price = models.FloatField(verbose_name="商品单价")
    count = models.IntegerField(default=0,verbose_name="商品销量")
    creat_time = models.DateTimeField(auto_now_add=True,verbose_name="上架时间")
    intro = models.TextField()
    stores = models.ForeignKey(Store,on_delete=models.CASCADE,verbose_name="商品所属店铺")
    goodstype = models.ForeignKey(GoodType,on_delete=models.CASCADE,verbose_name="商品类型")





class GoodsImage(models.Model):
    id = models.AutoField(primary_key=True)
    path = models.ImageField(upload_to="static/images/goods",default="static/images/goods/default.png",verbose_name="商品名称")
    status = models.BooleanField(default=False,verbose_name="是否显示该图片")
    intro = models.TextField(verbose_name="商品描述",null=True,blank=True)
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE,verbose_name="所属商品")
