from django.shortcuts import render, HttpResponse

# Create your views here.

# URLconf匹配路由
def special_case_2003(request):
    print(dir(request))
    return HttpResponse('articles')

def year_archive(request, year = 2023):
    return HttpResponse('articles %s' %(year))

def year_archive_uuid(request, uuid):
    return HttpResponse('articles %s' %(uuid))

def month_archive(request, year = 2023, month = 1):
    return HttpResponse('articles %s-%s' %(year, month))

def article_detail(request, year = 2023, month = 1, slug = "article_detail"):
    return HttpResponse('articles 动态 %s-%s-%s' %(year, month, slug))
