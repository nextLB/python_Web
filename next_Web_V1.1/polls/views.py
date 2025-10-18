

from django.shortcuts import render
from .models import user_info


def index_list(request):
    # 从数据库获取所有数据（MyModel.objects.all()返回查询集）
    all_data = user_info.objects.all()

    # 将数据传递给模板（第三个参数是上下文，字典格式）
    return render(request, 'html_files/index.html', {'data_list': all_data})
