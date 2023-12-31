from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    age = models.IntegerField()
    # 在已有数据表后面添加列
    # phone = models.IntegerField(default=2)  添加默认值
    # data = models.IntegerField(null = True, blank = True) 允许这个值为空

class Department(models.Model):
    title = models.CharField(max_length = 16)
    
# 数据库新的表添加或删除的话，重新运行下数据库迁移命令