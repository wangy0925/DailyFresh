import time
import os
from django.db import models
from db.base_model import BaseModel
from django.conf import settings
from DjangoUeditor.models import UEditorField


def goods_type_upload_path(instance, filename):
    name = 'goods/type/%s_%s' % (int(time.time()), filename)
    if os.path.exists(os.path.join(settings.MEDIA_ROOT, name)):
        os.remove(os.path.join(settings.MEDIA_ROOT, name))
    return name


def goods_sku_upload_path(instance, filename):
    name = 'goods/sku/%s_%s' % (int(time.time()), filename)
    if os.path.exists(os.path.join(settings.MEDIA_ROOT, name)):
        os.remove(os.path.join(settings.MEDIA_ROOT, name))
    return name


def banner_upload_path(instance, filename):
    name = 'goods/banner/%s_%s' % (int(time.time()), filename)
    if os.path.exists(os.path.join(settings.MEDIA_ROOT, name)):
        os.remove(os.path.join(settings.MEDIA_ROOT, name))
    return name

def promotion_upload_path(instance, filename):
    name = 'goods/promotion/%s_%s' % (int(time.time()), filename)
    if os.path.exists(os.path.join(settings.MEDIA_ROOT, name)):
        os.remove(os.path.join(settings.MEDIA_ROOT, name))
    return name


GOODS_SKU_STATUS_CHOICE = (
    (0, '下线'),
    (1, '上线'),
)


# Create your models here.
class GoodsType(BaseModel):
    """
    商品类型模型类
    """
    name = models.CharField(max_length=20, verbose_name='种类名称')
    logo = models.CharField(max_length=20, verbose_name='标识')
    image = models.ImageField(upload_to=goods_type_upload_path, verbose_name='商品类型图片')
    
    class Meta:
        db_table = 'db_goods_type'
        verbose_name = '商品种类'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return '<商品分类-%s>' % self.name
    

class GoodsSKU(BaseModel):
    """
    商品SKU模型类
    """
    type = models.ForeignKey('GoodsType', verbose_name='商品种类', on_delete=models.CASCADE)
    goods = models.ForeignKey('Goods', verbose_name='商品SPU', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name='商品名称')
    desc = models.CharField(max_length=256, verbose_name='商品简介')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品价格')
    unite = models.CharField(max_length=20, verbose_name='商品单位')
    image = models.ImageField(upload_to=goods_sku_upload_path, verbose_name='商品图片')
    stock = models.IntegerField(default=1, verbose_name='商品库存')
    sales = models.IntegerField(default=0, verbose_name='商品销量')
    status = models.SmallIntegerField(default=1, choices=GOODS_SKU_STATUS_CHOICE, verbose_name='状态')
    
    class Meta:
        db_table = 'db_goods_sku'
        verbose_name = '商品sku'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return '<商品SKU模型--%s>' % self.name
    

GOODS_DETAIL_PATH = 'goods/detail/%(basename)s_%(datetime)s.%(extname)s',

class Goods(BaseModel):
    """
    商品SPU模型类
    """
    name = models.CharField(max_length=20, verbose_name='商品SPU名称')
    detail = UEditorField(verbose_name='详细介绍', width='90%', height=500, imagePath=GOODS_DETAIL_PATH,
                          upload_settings={'imageMaxSize': 1024000}, toolbars='full')
    
    class Meta:
        db_table = 'df_goods'
        verbose_name = '商品spu'
        verbose_name_plural = verbose_name
        
    def __str__(self):
        return '<商品SPU---%s>' % self.name


class IndexGoodsBanner(BaseModel):
    """
    首页轮播图展示模型类
    """
    sku = models.ForeignKey('GoodsSKU', verbose_name='商品', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=banner_upload_path, verbose_name='图片')
    index = models.SmallIntegerField(default=0, verbose_name='展示顺序')
    
    class Meta:
        db_table = 'db_index_banner'
        verbose_name = '首页展示轮播图'
        verbose_name_plural = verbose_name
        

class IndexTypeGoodBanner(BaseModel):
    """
    首页分类商品展示模型类
    """
    DISPLAY_TYPE_CHOICE = (
        ('0', '标题'),
        ('1', '图片'),
    )
    
    type = models.ForeignKey('GoodsType', verbose_name='商品类型', on_delete=models.CASCADE)
    sku = models.ForeignKey('GoodsSKU', verbose_name='商品SKU', on_delete=models.CASCADE)
    display_type = models.SmallIntegerField(default=1, choices=DISPLAY_TYPE_CHOICE)
    index = models.SmallIntegerField(default=0, verbose_name='展示顺序')
    
    class Meta:
        db_table = 'db_index_type_goods'
        verbose_name = '主页分类展示商品'
        verbose_name_plural = verbose_name


class IndexPromotionBanner(BaseModel):
    """
    首页促销活动模型类
    """
    name = models.CharField(max_length=20, verbose_name='活动名称')
    url = models.URLField(verbose_name='活动链接')
    image = models.ImageField(upload_to=promotion_upload_path, verbose_name='活动图片')
    index = models.SmallIntegerField(default=0, verbose_name='展示顺序')
    
    class Meta:
        db_table = 'db_index_promotion'
        verbose_name = '主页促销活动'
        verbose_name_plural = verbose_name
        