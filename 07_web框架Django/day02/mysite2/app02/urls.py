from django.urls import path, re_path, register_converter, include
from app02 import views
from app02 import converters

# 自定义匹配路由
# 限制四位的0~9整数匹配规则
register_converter(converters.FourDigitYearConverter, "yyyy")

urlpatterns = [
    path("articles/2003/", views.special_case_2003),
    # path("articles/<yyyy:year>/", views.year_archive),
    path("articles/<int:year>/", views.year_archive),
    path("articles/<int:year>/<int:month>/", views.month_archive),
    path("articles/<int:year>/<int:month>/<slug:slug>/", views.article_detail),
    
    # 正则匹配
    # path("articles/2003/", views.special_case_2003),
    # re_path(r"^articles/(?P<year>[0-9]{4})/$", views.year_archive),
    # re_path(r"^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$", views.month_archive),
    # re_path(r"^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$", views.article_detail)
]