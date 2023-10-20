from django.db import models

# Create your models here.

class Account(models.Model):
    """帐户表
    """
    username = models.CharField(verbose_name='用户名', max_length=64, unique=True)
    password = models.CharField(verbose_name='密码', max_length=255)
    email = models.EmailField(verbose_name='邮箱', max_length=64, unique=True)
    register_date = models.DateTimeField(verbose_name='注册时间', auto_now_add=True)
    signature = models.CharField(verbose_name='签名', max_length=255, null=True)


class Article(models.Model):
    """文章表
    """
    title = models.CharField(verbose_name='标题', max_length=255, unique=True)
    content = models.TextField(verbose_name='内容')
    account = models.ForeignKey(verbose_name='作者', to='Account', on_delete=models.CASCADE) # 当用户删除时，他的文章放在哪
    tags = models.ManyToManyField(verbose_name='标签', to='Tag', related_name='articles', null=True) # 文章和标签是多对多的关系
    pub_date = models.DateTimeField(verbose_name='发布时间', auto_now_add=True)

class Tag(models.Model):
    """标签表
    """
    name = models.CharField(verbose_name='标签名', max_length=64, unique=True)
    date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
