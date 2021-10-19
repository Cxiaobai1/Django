from django.db import models


# Create your models here.
class Pub_name(models.Model):
    pubname = models.CharField(max_length=255, verbose_name='出版社', unique=True)

    def __str__(self):
        return '出版社：%s' % self.pubname


class Author(models.Model):
    name = models.CharField(max_length=30, verbose_name='姓名')
    email = models.EmailField(verbose_name='邮箱')

    # books = models.ManyToManyField(to='BOOk')

    def __str__(self):
        return '作者:%s' % self.name


class BOOk(models.Model):
    title = models.CharField(max_length=30, unique=True, verbose_name='书名')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='定价')

    # def default_price(self):
    #     return '$30'
    default_price = '$30'
    retail_price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='零售价', default=default_price)
    pub = models.ForeignKey(to=Pub_name, on_delete=models.CASCADE, null=True)
    author = models.ManyToManyField(to='Author')

    def __str__(self):
        # return "title:%s,pub:%s,price:%s" % (self.title, self.pub, self.price)
        return "%s %s %s %s" % (self.title, self.price, self.retail_price, self.pub)


class UserInfo(models.Model):
    email = models.EmailField(max_length=24, verbose_name='用户邮箱', default=1)
    username = models.CharField(max_length=24, verbose_name='用户昵称')
    password = models.CharField(max_length=100, verbose_name='密码')

    def __str__(self):
        return "%s" % (self.username)


class MfBook(models.Model):
    num = models.IntegerField(verbose_name='排名', null=True)
    title = models.CharField(max_length=255, verbose_name='书籍名称', unique=True, db_index=True,
                             primary_key=True)
    author = models.CharField(max_length=255, verbose_name='作者', null=True)
    description = models.CharField(max_length=255, verbose_name='简介', default='无描述', null=True)
    img_ul = models.CharField(max_length=255, verbose_name='图片路径', default='无路径', null=True)


class CxBook(models.Model):
    num = models.IntegerField(verbose_name='排名', null=True)
    title = models.CharField(max_length=255, verbose_name='书籍名称', unique=True, db_index=True,
                             primary_key=True)
    author = models.CharField(max_length=255, verbose_name='作者', null=True)
    description = models.CharField(max_length=255, verbose_name='简介', default='无描述', null=True)
    img_ul = models.CharField(max_length=255, verbose_name='图片路径', default='无路径', null=True)


class DyBook(models.Model):
    num = models.IntegerField(verbose_name='排名', null=True)
    title = models.CharField(max_length=255, verbose_name='书籍名称', unique=True, db_index=True,
                             primary_key=True)
    author = models.CharField(max_length=255, verbose_name='作者', null=True)
    description = models.CharField(max_length=255, verbose_name='简介', default='无描述', null=True)
    img_ul = models.CharField(max_length=255, verbose_name='图片路径', default='无路径', null=True)


class DjBook(models.Model):
    num = models.IntegerField(verbose_name='排名', null=True)
    title = models.CharField(max_length=255, verbose_name='书籍名称', unique=True, db_index=True,
                             primary_key=True)
    author = models.CharField(max_length=255, verbose_name='作者', null=True)
    description = models.CharField(max_length=255, verbose_name='简介', default='无描述', null=True)
    img_ul = models.CharField(max_length=255, verbose_name='图片路径', default='无路径', null=True)


class XsBook(models.Model):
    num = models.IntegerField(verbose_name='排名', null=True)
    title = models.CharField(max_length=255, verbose_name='书籍名称', unique=True, db_index=True,
                             primary_key=True)
    author = models.CharField(max_length=255, verbose_name='作者', null=True)
    description = models.CharField(max_length=255, verbose_name='简介', default='无描述', null=True)
    img_ul = models.CharField(max_length=255, verbose_name='图片路径', default='无路径', null=True)


class AllBook(models.Model):
    title = models.CharField(max_length=255, verbose_name='书籍名称', unique=True, db_index=True,
                             primary_key=True)
    author = models.CharField(max_length=255, verbose_name='作者', null=True)
    description = models.CharField(max_length=255, verbose_name='简介', default='无描述', null=True)
    img_ul = models.CharField(max_length=255, verbose_name='图片路径', default='无路径', null=True)
