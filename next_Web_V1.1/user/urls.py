from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    # 将根路径重定向到仪表板
    path('', RedirectView.as_view(pattern_name='dashboard', permanent=False)),

    # 认证相关URL
    path('accounts/register/', views.register_view, name='register'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),

    # 仪表板页面 - 登录后的主页面
    path('dashboard/', views.dashboard_view, name='dashboard'),

    # 用户信息管理URL
    path('user-management/', views.show_user_information_view, name='dataList'),
    path('user-management/add/', views.add_user_view, name='add_user'),
    path('user-management/edit/<int:user_id>/', views.edit_user_view, name='edit_user'),
    path('user-management/delete/<int:user_id>/', views.delete_user_view, name='delete_user'),
]