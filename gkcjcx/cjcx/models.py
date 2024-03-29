from django.db import models

# Create your models here.
    
class Chengji(models.Model):
    '''成绩查询'''
    
    zhunkaozheng = models.CharField(verbose_name='学生准考证号', max_length=32)
    xingming = models.CharField(verbose_name='学生姓名', max_length=32)
    banji = models.IntegerField(verbose_name='班级')
    
    yuwen_score = models.IntegerField(verbose_name='语文成绩')
    shuxue_score = models.IntegerField(verbose_name='数学成绩')
    waiyu_score = models.IntegerField(verbose_name='外语成绩')
    
    xuankao_1 = models.CharField(verbose_name='选考科目1名称', max_length=32)
    xuankao_1_score = models.IntegerField(verbose_name='选考1科目成绩')
    xuankao_1_weici = models.IntegerField(verbose_name='选考1科目位次')
    xuankao_2 = models.CharField(verbose_name='选考科目2名称', max_length=32)
    xuankao_2_score = models.IntegerField(verbose_name='选考2科目成绩')
    xuankao_2_weici = models.IntegerField(verbose_name='选考2科目位次')
    xuankao_3 = models.CharField(verbose_name='选考科目3名称', max_length=32)
    xuankao_3_score = models.IntegerField(verbose_name='选考3科目成绩')
    xuankao_3_weici = models.IntegerField(verbose_name='选考3科目位次')
    
    total_score = models.IntegerField(verbose_name='总分')
    total_weici = models.IntegerField(verbose_name='总分位次')