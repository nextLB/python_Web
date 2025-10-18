from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import show_user_informations


# 用户注册视图
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
            username = form.cleaned_data.get('username')
            # 从清理后的表单数据中获取密码（password1是第一个密码字段）
            password = form.cleaned_data.get('password1')
            # 使用Django的authenticate函数验证用户凭证
            user = authenticate(username=username, password=password)
            # 使用Django的login函数登录用户，建立会话
            login(request, user)

            # 显示成功消息（会在模板中显示）
            messages.success(request, f'账号 {username} 注册成功！')

            # 重定向到仪表板页面
            return redirect('dashboard')  # 修改：注册后跳转到仪表板

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
        username = request.POST.get('username')
        # 从POST数据中获取密码
        password = request.POST.get('password')

        # 使用Django的authenticate函数验证用户凭证
        user = authenticate(request, username=username, password=password)

        # 检查用户认证是否成功（user不为None表示认证成功）
        if user is not None:
            # 认证成功，使用login函数建立用户会话
            login(request, user)
            # 显示登录成功消息
            messages.success(request, f'欢迎回来，{username}！')

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


# 显示所有用户信息 - 原有的功能，添加登录要求
@login_required(login_url='/accounts/login/')
def show_user_information_view(request):
    """
    显示所有用户信息的视图函数
    只有登录用户才能访问
    """
    # 获取数据库中的所有数据信息
    # 使用ORM的all()方法获取show_user_informations表中的所有记录
    userData = show_user_informations.objects.all()

    # 往html模板传递参数，渲染用户信息展示页面
    return render(request, 'html_files/show_user_informations.html', {
        'dataList': userData,  # 用户数据列表，传递给模板显示
        'username': request.user.username  # 传递当前用户名到模板，用于显示登录用户信息
    })


# 添加新用户 - 添加登录要求
@login_required(login_url='/accounts/login/')
def add_user_view(request):
    """
    处理添加新用户的视图函数
    支持GET（显示添加表单）和POST（处理表单提交）
    """
    # 检查请求方法是否为POST（用户提交了添加表单）
    if request.method == 'POST':
        # 从POST数据中获取表单字段值
        name = request.POST.get('name')  # 获取姓名
        age = request.POST.get('age')  # 获取年龄
        sex = request.POST.get('sex')  # 获取性别

        # 创建新用户记录并保存到数据库
        user_info = show_user_informations.objects.create(
            name=name,  # 设置姓名
            age=age,  # 设置年龄
            sex=sex,  # 设置性别
            created_by=request.user  # 关联当前登录用户，记录是谁创建的这个用户
        )

        # 显示添加成功的消息
        messages.success(request, f'用户 {name} 添加成功！')

        # 重定向到用户列表页面（名称为'dataList'的URL）
        return redirect('dataList')

    # 如果是GET请求，显示添加用户表单
    return render(request, 'html_files/user_form.html', {
        'form_type': 'add'  # 告诉模板这是添加表单，不是编辑表单
    })


# 编辑用户信息 - 添加登录要求
@login_required(login_url='/accounts/login/')
def edit_user_view(request, user_id):
    """
    编辑现有用户信息的视图函数
    接收user_id参数指定要编辑的用户
    """
    # 获取要编辑的用户对象，如果不存在则返回404错误页面
    # get_object_or_404会尝试根据id查找用户，找不到则自动返回404
    user = get_object_or_404(show_user_informations, id=user_id)

    # 检查请求方法是否为POST（用户提交了编辑表单）
    if request.method == 'POST':
        # 使用POST数据更新用户信息
        user.name = request.POST.get('name')  # 更新姓名
        user.age = request.POST.get('age')  # 更新年龄
        user.sex = request.POST.get('sex')  # 更新性别
        user.save()  # 将修改保存到数据库

        # 显示更新成功的消息
        messages.success(request, f'用户 {user.name} 信息更新成功！')

        # 重定向到用户列表页面
        return redirect('dataList')

    # 如果是GET请求，显示编辑表单并预填现有数据
    return render(request, 'html_files/user_form.html', {
        'form_type': 'edit',  # 告诉模板这是编辑表单
        'user': user  # 传递要编辑的用户对象到模板
    })


# 删除用户 - 添加登录要求
@login_required(login_url='/accounts/login/')
def delete_user_view(request, user_id):
    """
    删除用户的视图函数
    通常使用POST方法进行删除操作（更安全）
    """
    # 检查请求方法是否为POST（确认删除）
    if request.method == 'POST':
        # 获取要删除的用户对象，如果不存在则返回404
        user = get_object_or_404(show_user_informations, id=user_id)
        user_name = user.name  # 保存用户名用于显示消息

        # 从数据库中删除用户
        user.delete()

        # 显示删除成功的消息
        messages.success(request, f'用户 {user_name} 删除成功！')

        # 重定向到用户列表页面
        return redirect('dataList')

    # 如果是GET请求，显示确认删除页面
    # 这是一种安全措施，防止通过简单链接直接删除
    user = get_object_or_404(show_user_informations, id=user_id)
    return render(request, 'html_files/confirm_delete.html', {
        'user': user  # 传递要删除的用户对象到确认页面
    })