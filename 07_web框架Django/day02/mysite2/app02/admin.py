from django.contrib import admin
from app02 import models

# Register your models here.

# 定制admin模块
class AccountAdmin(admin.ModelAdmin):
    list_display = ['username', 'password', 'email', 'signature', 'register_date']
    list_filter = ['username', 'email']
    search_fields = ['username', 'email']
    ordering = ['register_date']
    
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'pub_date']
    list_filter = ['title', 'pub_date']
    search_fields = ['title', 'content', 'account_id']
    ordering = ['pub_date']

admin.site.register(models.Account, AccountAdmin)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Tag)