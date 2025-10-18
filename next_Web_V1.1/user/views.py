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
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # 注册成功后自动登录
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'账号 {username} 注册成功！')
            return redirect('dashboard')  # 修改：注册后跳转到仪表板
        else:
            messages.error(request, '注册失败，请检查表单错误。')
    else:
        form = UserCreationForm()

    return render(request, 'html_files/register.html', {'form': form})


# 用户登录视图
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'欢迎回来，{username}！')
            # 获取next参数，如果存在则重定向到next指定的页面，否则重定向到仪表板
            next_url = request.GET.get('next', 'dashboard')  # 修改：默认跳转到仪表板
            return redirect(next_url)
        else:
            messages.error(request, '用户名或密码错误！')

    return render(request, 'html_files/login.html')


# 用户登出视图
def logout_view(request):
    logout(request)
    messages.success(request, '您已成功退出登录！')
    return redirect('login')


# 仪表板页面 - 登录后的主页面
@login_required(login_url='/accounts/login/')
def dashboard_view(request):
    return render(request, 'html_files/dashboard.html', {
        'username': request.user.username
    })


# 显示所有用户信息 - 原有的功能，添加登录要求
@login_required(login_url='/accounts/login/')
def show_user_information_view(request):
    # 获取数据库中的所有数据信息
    userData = show_user_informations.objects.all()
    # 往html模板传递参数
    return render(request, 'html_files/show_user_informations.html', {
        'dataList': userData,
        'username': request.user.username  # 传递当前用户名到模板
    })


# 添加新用户 - 添加登录要求
@login_required(login_url='/accounts/login/')
def add_user_view(request):
    if request.method == 'POST':
        # 获取表单数据
        name = request.POST.get('name')
        age = request.POST.get('age')
        sex = request.POST.get('sex')

        # 创建新用户
        user_info = show_user_informations.objects.create(
            name=name,
            age=age,
            sex=sex,
            created_by=request.user  # 关联当前登录用户
        )
        messages.success(request, f'用户 {name} 添加成功！')
        # 重定向到用户列表页面
        return redirect('dataList')

    # 如果是GET请求，显示添加表单
    return render(request, 'html_files/user_form.html', {'form_type': 'add'})


# 编辑用户信息 - 添加登录要求
@login_required(login_url='/accounts/login/')
def edit_user_view(request, user_id):
    # 获取要编辑的用户对象，如果不存在则返回404
    user = get_object_or_404(show_user_informations, id=user_id)

    if request.method == 'POST':
        # 更新用户信息
        user.name = request.POST.get('name')
        user.age = request.POST.get('age')
        user.sex = request.POST.get('sex')
        user.save()

        messages.success(request, f'用户 {user.name} 信息更新成功！')
        # 重定向到用户列表页面
        return redirect('dataList')

    # 如果是GET请求，显示编辑表单
    return render(request, 'html_files/user_form.html', {
        'form_type': 'edit',
        'user': user
    })


# 删除用户 - 添加登录要求
@login_required(login_url='/accounts/login/')
def delete_user_view(request, user_id):
    if request.method == 'POST':
        # 获取并删除用户
        user = get_object_or_404(show_user_informations, id=user_id)
        user_name = user.name
        user.delete()

        messages.success(request, f'用户 {user_name} 删除成功！')
        # 重定向到用户列表页面
        return redirect('dataList')

    # 如果是GET请求，显示确认删除页面
    user = get_object_or_404(show_user_informations, id=user_id)
    return render(request, 'html_files/delete_confirm.html', {'user': user})