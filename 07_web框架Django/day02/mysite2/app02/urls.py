from django.urls import path, re_path, register_converter, include
from app02 import views
from app02 import converters

# 自定义匹配路由
# 限制四位的0~9整数匹配规则
register_converter(converters.FourDigitYearConverter, "yyyy")

extra_urls = [
    # path("2003/", views.special_case_2003),
    # path("<yyyy:year>/", views.year_archive),
    # path("<int:year>/", views.year_archive),
    # path("<uuid:uuid>/", views.year_archive_uuid),
    # path("<int:year>/<int:month>/", views.month_archive),
    # path("<int:year>/<int:month>/<slug:slug>/", views.article_detail),
    
    # 正则匹配
    path("2003/", views.special_case_2003),
    # 可以传第二个参数，没有用法没有体现
    re_path(r"^(?P<year>[0-9]{4})/$", views.year_archive, { "version": "v1.0.0"}),
    re_path(r"^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$", views.month_archive),
    re_path(r"^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$", views.article_detail)
]

urlpatterns = [
    path('articles/', include(extra_urls))
]