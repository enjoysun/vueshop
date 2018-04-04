from datetime import datetime
from django.db import models

# Create your models here.


class BaseModel(models.Model):
    ctime = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        abstract = True


class GoodCategory(BaseModel):
    """
    商品类别
    """
    CATEGORY_TYPE = (
        (1, '一级类目'),
        (2, '二级类目'),
        (3, '三级类目'),
    )

    name = models.CharField(default='', max_length=32, help_text='类别名', verbose_name='名称')
    code = models.CharField(default='', max_length=32, help_text='类别code', verbose_name='编码')
    descripition = models.TextField(default='', help_text='类别描述', verbose_name='描述')
    category_type = models.CharField(max_length=64, choices=CATEGORY_TYPE, verbose_name='类别', help_text='类别级别')
    fid = models.ForeignKey('self', null=True, blank=True, verbose_name='父类别', help_text='父类别', related_name='sub_cat', on_delete=models.CASCADE)
    is_tab = models.BooleanField(default=False, verbose_name='是否显示在tab', help_text='是否显示在导航')

    class Meta:
        verbose_name = '商品类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodGateBrand(BaseModel):
    """
    品牌
    """
    name = models.CharField(default='', max_length=32, verbose_name='品牌名称', help_text='名称')
    description = models.TextField(default='', verbose_name='品牌描述', help_text='品牌描述')
    img_url = models.CharField(default='', max_length=128, verbose_name='品牌img地址', help_text='品牌img地址')

    class Meta:
        verbose_name = '品牌'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(BaseModel):
    """
    商品
    """
    category = models.ForeignKey(GoodCategory, null=True, blank=True, verbose_name='类别', help_text='类别', on_delete=models.CASCADE)
    goods_sn = models.CharField(max_length=64, default='', verbose_name='唯一编号', help_text='唯一编号')
    name = models.CharField(max_length=128, verbose_name='商品名', help_text='商品名')
    click_num = models.IntegerField(default=0, verbose_name='点击数', help_text='点击数')
    sold_num = models.IntegerField(default=0, verbose_name='销售量', help_text='销售量')
    fav_num = models.IntegerField(default=0, verbose_name='收藏数', help_text='收藏数')
    goods_num = models.IntegerField(default=0, verbose_name='库存数', help_text='库存数')
    market_price = models.FloatField(default=0, verbose_name='市场价格', help_text='市场价格')
    shop_price = models.FloatField(default=0, verbose_name='本地价格', help_text='本地价格')
    goods_brief = models.CharField(max_length=128, verbose_name='简短描述', help_text='简短描述')

    # 缺少ueditor
    ship_free = models.BooleanField(default=True, verbose_name='是否承担运费', help_text='是否承担运费')
    goods_header_img = models.CharField(max_length=128, verbose_name='展示图片地址', help_text='展示图片地址')
    is_new = models.BooleanField(default=False, verbose_name='是否是新品', help_text='是否是新品')
    is_hot = models.BooleanField(default=False, verbose_name='是否是热销', help_text='是否是热销')

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsImage(BaseModel):
    """
    商品图片
    """
    goods = models.ForeignKey(Goods, related_name='images', verbose_name='商品', help_text='商品', on_delete=models.CASCADE)
    image_url = models.CharField(max_length=128, verbose_name='商品详细图片地址', help_text='商品详细图片地址')

    class Meta:
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class Banner(BaseModel):
    """
    商品轮播图
    """
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    img_url = models.CharField(max_length=128, verbose_name="轮播图地址")
    img_index = models.IntegerField(default=0, verbose_name="轮播图顺序")

    class Meta:
        verbose_name = '商品轮播图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name




