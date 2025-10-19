from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import user_informations_data_table




# 用户注册的视图
def register_view(request):
    """
    处理用户注册请求的视图函数
    支持GET（显示注册表单）和POST（处理注册数据）两种请求方法
    """
    # 检查请求方法是否为POST（用户提交表单）
    if request.method == 'POST':
        # 使用Django内置的用户创建表单，传入POST数据
        form = UserCreationForm(request.POST)

        # 验证表单数据是否有效（用户名是否唯一、密码是否符合要求等）
        if form.is_valid():
            # 表单验证通过，将用户数据保存到数据库
            form.save()

            # 注册成功后自动登录
            # 从清理后的表单数据中获取用户名
            user_account = form.cleaned_data.get('username')
            # 从清理后的表单数据中获取密码
            user_password = form.cleaned_data.get('password1')
            # 使用Django的authenticate函数验证用户凭证
            user = authenticate(username=user_account, password=user_password)
            # 使用Django的login函数登录用户，建立会话
            login(request, user)

            # 往自定义数据库中写入用户信息
            user_info = user_informations_data_table.objects.create(
                user_account=user_account,
                user_password=user_password,
                created_by=request.user  # 关联当前登录用户，记录是谁创建的这个用户
            )

            # 显示成功消息（会在模板中显示）
            messages.success(request, f'账号 {user_account} 注册成功！')

            # 重定向到仪表板页面
            return redirect('dashboard')

        else:
            # 表单验证失败，显示错误消息
            messages.error(request, '注册失败，请检查表单错误。')

    else:
        # 请求方法不是POST（通常是GET请求），创建一个空表单显示给用户
        form = UserCreationForm()

    # 渲染注册模板，传入表单对象
    return render(request, 'html_files/register.html', {'form': form})


# 用户登录视图
def login_view(request):
    """
    处理用户登录请求的视图函数
    支持GET（显示登录表单）和POST（处理登录数据）两种请求方法
    """

    # 检查请求方法是否为POST（用户提交登录表单）
    if request.method == 'POST':
        # 从POST数据中获取用户名
        user_account = request.POST.get('username')
        # 从POST数据中获取密码
        user_password = request.POST.get('password')

        # 使用Django的authenticate函数验证用户凭证
        user = authenticate(request, username=user_account, password=user_password)

        # 检查用户认证是否成功（user不为None表示认证成功）
        if user is not None:
            # 认证成功，使用login函数建立用户会话
            login(request, user)
            # 显示登录成功消息
            messages.success(request, f'欢迎回来，{user_account}！')

            # 获取next参数，如果存在则重定向到next指定的页面，否则重定向到仪表板
            next_url = request.GET.get('next', 'dashboard')  # 修改：默认跳转到仪表板
            # 重定向到目标页面
            return redirect(next_url)
        else:
            # 认证失败，显示错误消息
            messages.error(request, '用户名或密码错误！')

    # 渲染登录模板
    # 如果是GET请求，直接显示登录页面
    # 如果是POST请求但认证失败，重新显示登录页面并显示错误消息
    return render(request, 'html_files/login.html')





# 用户登出视图
def logout_view(request):
    """
    处理用户退出登录的视图函数
    """
    # 使用Django的logout函数清除用户会话
    logout(request)
    # 显示退出成功消息
    messages.success(request, '您已成功退出登录！')
    # 重定向到登录页面
    return redirect('login')


# 仪表板页面 - 登录后的主页面
@login_required(login_url='/accounts/login/')
# @login_required 的作用
# @login_required 是 Django 提供的一个视图装饰器，用于保护需要登录才能访问的页面。
def dashboard_view(request):
    """
    显示用户仪表板的视图函数
    只有登录用户才能访问
    """
    return render(request, 'html_files/dashboard.html', {
        'username': request.user.username
    })
