

from django.shortcuts import render
from .models import user_info



# 关于index这个页面返回的设置
def index_list(request):
    # 从数据库获取所有数据（MyModel.objects.all()返回查询集）
    all_data = user_info.objects.all()

    # 将数据传递给模板（第三个参数是上下文，字典格式）  这个index.html的根目录默认是在templates的下面
    return render(request, 'html_files/index.html', {'dataList': all_data})


