


from django.shortcuts import render
from .models import show_user_informations


# Create your views here.

def show_user_information_view(request):

    # 获取其数据库中的所有数据信息
    userData = show_user_informations.objects.all()


    # 往html模板传递参数
    return render(request, 'html_files/show_user_informations.html', {'dataList': userData})



