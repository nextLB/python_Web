

from django.db import models

class user_info(models.Model):
    # 定义字段（根据需求添加）
    name = models.CharField(max_length=100, verbose_name="姓名")  # 字符串类型，最长100字符
    age = models.IntegerField(verbose_name="年龄")  # 整数类型

    # 定义Meta类，指定自定义表名
    class Meta:
        db_table = "user_info"  # 自定义数据表名称
        verbose_name = "user_info"  # 后台显示的名称（可选）
        verbose_name_plural = verbose_name  # 复数形式（可选）

    # 可选：定义对象的字符串表示（方便调试）
    def __str__(self):
        return self.name
