from django.urls import path
from . import views

urlpatterns = [
    # 认证相关URL
    path('accounts/register/', views.register_view, name='register'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),

    # 用户信息管理URL
    path('', views.show_user_information_view, name='dataList'),  # 显示所有用户
    path('add/', views.add_user_view, name='add_user'),  # 添加用户
    path('edit/<int:user_id>/', views.edit_user_view, name='edit_user'),  # 编辑用户
    path('delete/<int:user_id>/', views.delete_user_view, name='delete_user'),  # 删除用户
]