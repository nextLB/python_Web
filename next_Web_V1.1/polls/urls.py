
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_list, name='dataList'),  # 函数视图
]








