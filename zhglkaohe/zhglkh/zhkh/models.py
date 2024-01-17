from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=32)
    phone = models.CharField(verbose_name='手机号码', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=32)
    course = models.CharField(verbose_name='课程', max_length=32)
    class_hours = models.IntegerField(verbose_name='课时量',null=True, blank=True)
    duty_hours = models.FloatField(verbose_name='值班折算节数',null=True, blank=True)
    extra_hours = models.FloatField(verbose_name='额外工作折算节数',null=True, blank=True)
    total_hours = models.FloatField(verbose_name='额总工作量节数',null=True, blank=True)
    work_score = models.FloatField(verbose_name='额总工作量节数',null=True, blank=True)
    personal_score = models.FloatField(verbose_name='教师个人成绩',null=True, blank=True)
    class_score = models.FloatField(verbose_name='班级量化成绩',null=True, blank=True)
    group_score = models.FloatField(verbose_name='教研组量化成绩',null=True, blank=True)
    total_score = models.FloatField(verbose_name='总成绩',null=True, blank=True)
    note = models.CharField(verbose_name='备注', max_length=120, null=True, blank=True)
    ranking = models.IntegerField(verbose_name='名次',null=True, blank=True)
    
    def __str__(self):
        return self.name