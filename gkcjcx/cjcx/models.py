from django.db import models

# Create your models here.
class Course(models.Model):
    '''学科'''
    name = models.CharField(verbose_name='学科名称', max_length=32)

    
class Student(models.Model):
    '''学生'''
    zhunkaozheng = models.CharField(verbose_name='学生准考证号', max_length=32)
    xingming = models.CharField(verbose_name='学生姓名', max_length=32)
    banji = models.IntegerField(verbose_name='班级')
    
class Chengji(models.Model):
    '''成绩查询'''
    sno = models.ForeignKey()
    cno = models.ForeignKey()
    chengji = models.IntegerField(verbose_name='成绩')
    weici = models.IntegerField(verbose_name='位次')
    