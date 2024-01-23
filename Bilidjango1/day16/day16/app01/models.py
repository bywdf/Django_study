from django.db import models

# Create your models here.
class Department(models.Model):
    '''部门表'''
    # id = models.BigAutoField(verbose_name='ID', primary_key=True) # 自己写的主键，不写的话Django自己生产
    # id = models.AutoField(verbose_name='ID', primary_key=True) 
    title = models.CharField(verbose_name='标题', max_length=32)
    def __str__(self):    # 引入外键时，返回名称
        return self.title
    
    
    
class UserInfo(models.Model):
    '''员工表'''
    name = models.CharField(verbose_name='姓名', max_length = 32)
    password = models.CharField(verbose_name='密码', max_length = 64)
    age = models.IntegerField(verbose_name='年龄')
    account = models.DecimalField(verbose_name='账户余额', max_digits=10, decimal_places=2, default=0) # 固定字段十进制精度数 (总位数，小数位数）
    # creat_time = models.DateTimeField(verbose_name='入职时间')
    creat_time = models.DateField(verbose_name='入职时间')
    # depart_id = models.BigIntegerField(verbose_name='部门ID') 无约束
    
    # 有约束 
    # 1. -to,与哪张表关联
    #    -to_field，与表中哪一列相关联
    # 2. django自动，写的depart，自动生产depart_id
    # 3. 部门表被删除,级联删除,删除相关用户
    depart = models.ForeignKey(verbose_name='部门', to='Department', to_field='id', on_delete=models.CASCADE)
    # 4. 置空
    # depart = models.ForeignKey(to='Depatrment', to_field='id', null=True, blank=True, on_delete=models.SET_NULL)
    gender_choices = (
        (1,'男'),
        (2,'女'),
    )
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices)

    
class PrettyNum(models.Model):
    '''靓号表'''
    mobile = models.CharField(verbose_name='', max_length=11)
    price = models.IntegerField(verbose_name='价格')
    level_choices = (
        (1, '等级1'),
        (2, '等级2'),
        (3, '等级3'),
        (4, '等级4'),
    )
    level = models.SmallIntegerField(verbose_name='等级', choices = level_choices, default=1)
    status_choices=(
        (1, '已售'),
        (2, '未售'),
    )
    status = models.SmallIntegerField(verbose_name='状态', choices= status_choices, default=2)

