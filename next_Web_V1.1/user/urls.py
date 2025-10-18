
from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_user_information_view, name='dataList'),  # 函数视图
]
