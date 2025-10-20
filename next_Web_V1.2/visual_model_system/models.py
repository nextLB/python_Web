
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# 用户信息的数据表
class user_informations_data_table(models.Model):
    # 定义字段
    user_account = models.CharField(max_length=100, verbose_name="账号")      # 字符串类型，最长100字符
    user_password = models.CharField(max_length=100, verbose_name="密码")     # 同上

    # 添加创建者字段
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    # 定义Meta类，制定表名
    class Meta:
        db_table = "user_informations_table"  # 数据表名称
        verbose_name = "user_informations_table"  # 后台显示的名称


    # 定义对象的字符串表示
    def __str__(self):
        # 这个返回到后端超级管理员查看的那里的
        return f"用户账号_{self.user_account}  用户密码_{self.user_password}"





