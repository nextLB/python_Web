from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    # 将根路径重定向到仪表板
    # 关于重定向的解释：重定向是指当用户访问某个URL时，服务器会返回一个特殊的响应告诉浏览器"请去访问另一个 URL"，然后浏览器会自动跳转到新的地址。
    # 完整工作流程
    #     1、用户访问 http://yoursite.com/
    #     2、Django 匹配到空路径 ''
    #     3、RedirectView 处理请求
    #     4、服务器返回 302 状态码和 Location 头：/dashboard/
    #     5、浏览器自动跳转到 http://yoursite.com/dashboard/
    path('', RedirectView.as_view(pattern_name='dashboard', permanent=False)),

    # 认证相关URL
    # 用户注册
    #   URL路径：accounts/register/
    #   视图函数：views.register_view
    #   名称：register
    #   作用：处理用户注册请求，访问地址如 http://yoursite.com/accounts/register/
    path('accounts/register/', views.register_view, name='register'),
    # 用户登录
    #   URL路径： accounts/login/
    #   视图函数：views.login_view
    #   名称：login
    #   作用：处理用户登录请求
    path('accounts/login/', views.login_view, name='login'),
    # 用户退出
    #     URL 路径: accounts/logout/
    #     视图函数: views.logout_view
    #     名称: logout
    #     作用: 处理用户退出登录请求
    path('accounts/logout/', views.logout_view, name='logout'),

    # 仪表板页面 - 登录后的主页面
    #     URL 路径: dashboard/
    #     视图函数: views.dashboard_view
    #     名称: dashboard
    #     作用: 显示用户登录后的主控制面板
    path('dashboard/', views.dashboard_view, name='dashboard'),

]
