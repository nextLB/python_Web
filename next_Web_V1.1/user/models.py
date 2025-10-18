

from django.db import models

# Create your models here.

# 关于用户信息显示的页面
class show_user_informations(models.Model):

    # 定义字段
    name = models.CharField(max_length=100, verbose_name="姓名")  # 字符串类型，最长100字符
    age = models.IntegerField(verbose_name="年龄")  # 整数类型
    sex = models.CharField(max_length=4, verbose_name="性别")

    # 定义Meta类，制定表名
    class Meta:
        db_table = "user_informations"  # 数据表名称
        verbose_name = "user_informations"  # 后台显示的名称

    # 定义对象的字符串表示
    def __str__(self):
        return f"{self.name}（{self.age}岁，{self.sex}）"





