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

    # 用户信息管理URL
    # 用户列表显示
    #     URL 路径: user-management/
    #     视图函数: views.show_user_information_view
    #     名称: dataList
    #     作用: 显示所有用户信息的列表页面
    path('user-management/', views.show_user_information_view, name='dataList'),
    # 添加用户
    #     URL 路径: user-management/add/
    #     视图函数: views.add_user_view
    #     名称: add_user
    #     作用: 处理添加新用户的表单和请求
    path('user-management/add/', views.add_user_view, name='add_user'),

    #####################
    # 首先在这里将一下关于URL路径的参数
    # <int:user_id> 语法说明
    #     < >: 表示这是一个路径参数
    #     int: 路径转换器，确保匹配的是整数
    #     user_id: 参数名称，会传递给视图函数

    # 还有一些其它的路径转换器件如下:
    # # 字符串（默认）
    # path('user/<str:username>/', ...)  # 匹配任何非空字符串
    # # 整数
    # path('post/<int:post_id>/', ...)   # 匹配正整数
    # # Slug（字母、数字、连字符、下划线）
    # path('article/<slug:slug>/', ...)  # 匹配如 "hello-world"
    # # UUID
    # path('file/<uuid:file_id>/', ...)  # 匹配 UUID 字符串
    # # 路径（包含斜杠）
    # path('docs/<path:doc_path>/', ...) # 匹配包含斜杠的路径
    #####################


    # 编辑用户（带参数）
    #     URL 路径: user-management/edit/<int:user_id>/
    #     路径参数: <int:user_id> - 捕获 URL 中的整数作为用户 ID
    #     视图函数: views.edit_user_view
    #     名称: edit_user
    #     作用: 编辑指定 ID 的用户信息
    #     示例:
    #         user-management/edit/1/ → user_id=1
    #         user-management/edit/25/ → user_id=25
    path('user-management/edit/<int:user_id>/', views.edit_user_view, name='edit_user'),
    # 删除用户（带参数）
    #     URL 路径: user-management/delete/<int:user_id>/
    #     路径参数: <int:user_id> - 用户 ID
    #     视图函数: views.delete_user_view
    #     名称: delete_user
    #     作用: 删除指定 ID 的用户
    path('user-management/delete/<int:user_id>/', views.delete_user_view, name='delete_user'),
]