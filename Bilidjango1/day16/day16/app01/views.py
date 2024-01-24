from django.shortcuts import render, redirect
from app01 import models

from django import forms

from django.core.validators import RegexValidator   # 引入正则
from django.core.exceptions import ValidationError  # 引入报错

# Create your views here.


def depart_list(request):
    '''部门列表'''
    queryset = models.Department.objects.all()
    return render(request, 'depart_list.html', {'queryset': queryset})


def depart_add(request):
    '''添加部门'''
    if request.method == 'GET':
        return render(request, 'depart_add.html')

    title = request.POST.get('title')
    models.Department.objects.create(title=title)
    return redirect('/depart/list/')


def depart_delete(request):
    '''删除部门'''
    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()
    return redirect('/depart/list/')


def depart_edit(request, nid):
    '''修改部门'''
    # 通过nid获取数据，获取到的是一个列表对象，获取第一个
    if request.method == 'GET':
        row_object = models.Department.objects.filter(id=nid).first()
        return render(request, 'depart_edit.html',{'row_object': row_object})
    title = request.POST.get('title')
    models.Department.objects.filter(id=nid).update(title=title)
    return redirect('/depart/list')


def user_list(request):
    '''用户管理'''
    # 获取所有的用户列表
    queryset = models.UserInfo.objects.all()
    # obj.get_gender_display() 自动获取choices内容
    # obj.depart.title() 获取外键对象的title
    return render(request, 'user_list.html', {'queryset':queryset})


def user_add(request):
    '''添加用户'''
    context = {
        'gender_choices': models.UserInfo.gender_choices,
        'depart_list':models.Department.objects.all(),
    }
    return render(request,'user_add.html', context)


# 用modelform，先写一个类
class UserModelForm(forms.ModelForm):
    # 设置最小长度
    name = forms.CharField(min_length=3, label='用户名') 
    class Meta:
        model = models.UserInfo
        # fields = ['name', 'password', 'age', 'account', 'gender','creat_time', 'depart']
        fields = '__all__'  #  直接获取所有字段
        # widgets = {
        #     'name': forms.TextInput(attrs={'class':'form-control'}),
        #     'password': forms.PasswordInput(attrs={'class':'form-control'}),
        # }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环找到所有的插件，添加了class=form-control 的样式
        for name, field in self.fields.items():
            # if name == 'password':
            #     continue
            field.widget.attrs = {'class': 'form-control',
                                  'placeholder': field.label}
            
            
def user_form_add(request):
    '''添加用户,基于modelform版本'''
    if request.method == 'GET':
            form = UserModelForm()
            return render(request, 'user_form_add.html', {'form':form})
    # 用户POST提交，数据校验
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        # print(form.cleaned_data)
        form.save()
        return redirect('/user/list/')
    else:
        # print(form.errors) 在页面上显示错误信息
        return render(request, 'user_form_add.html', {'form':form})
    # 针对数据库的操作用ModesForm。其他的用Form操作，比如登录，


def user_edit(request, nid):
    '''编辑用户'''
    # 根据id去数据库中获取对应的对象
    row_object = models.UserInfo.objects.filter(id=nid).first()

    if request.method == 'GET':
        form = UserModelForm(instance=row_object)
        return render(request, 'user_edit.html', {'form':form})
    
    
    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        # 默认保存用户输入的所有数据
        # form.instance.字段名=值，用户输入以外增加某个值
        form.save()
        return redirect('/user/list/')
    else:
        return render(request, 'user_form_add.html', {'form':form})


def user_delete(request, nid):
    '''删除用户'''
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list/')


# '''数据库查询'''
# models.PrettyNum.objects.filter(mobile='18553976921', id=2)
# # 空字典等于查询所有
# data_dict = {'mobile':'18553976921', 'id':2}
# models.PrettyNum.objects.filter(**data_dict)

# # 针对数字
# models.PrettyNum.objects.filter(id=2)          # 等于2
# models.PrettyNum.objects.filter(id__gt=2)      # 大于2
# models.PrettyNum.objects.filter(id__gte=2)     # 大于等于2
# models.PrettyNum.objects.filter(id__lt=2)     # 小于2
# models.PrettyNum.objects.filter(id__lte=2)     # 小于等于2
# # 针对字符串
# models.PrettyNum.objects.filter(mobile__startswith='135')  # 以135开头
# models.PrettyNum.objects.filter(mobile__endswith='666')  # 以135结尾
# models.PrettyNum.objects.filter(mobile__contains='6')  # 包含6筛选出来

def pretty_list(request):
    '''靓号列表'''
    
    data_dict = {}
    search = request.GET.get('q','')
    if search:
        data_dict ['mobile__contains']= search 
    # models.PrettyNum.objects.filter(**data_dict)
     
    # select * from 表 order by id desc/asc     -id/id
    queryset = models.PrettyNum.objects.filter(**data_dict).order_by('-level')
    return render(request, 'pretty_list.html', {'queryset':queryset, 'search': search})


class PrettyModelForm(forms.ModelForm):
    # 验证方式一：
    mobile = forms.CharField(
        label='手机号',
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误')]
    )
    
    class Meta:
        model = models.PrettyNum
        # exclude = ['level']  这个是排除哪个字段
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {
                'class': 'form-control',
                'placeholder': field.label,
            }
    
    # 验证方式二   clean_mobile 自动生成的字段
    # 钩子方法 比如检验存在不存在，正则表达式都可以
    def clean_mobile(self):
        txt_molile = self.cleaned_data["mobile"]  # 用户输入的字段
        exists = models.PrettyNum.objects.filter(mobile=txt_molile).exists()
        if exists:
            raise ValidationError('手机号已存在')
        else:
            return txt_molile   

def pretty_add(request):
    '''靓号添加'''
    
    if request.method == "GET":
        form = PrettyModelForm()
        return render(request, 'pretty_add.html', {'form': form})  
     
    form = PrettyModelForm(data=request.POST)
    
    if form.is_valid():
        form.save()
        return redirect('/pretty/list/')
    else:
        return render(request, 'pretty_add.html', {'form': form}) 
    
    
class PrettyEditModelForm(forms.ModelForm):
    
    mobile = forms.CharField(
        label='手机号',
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误')]
    )
    
    # mobile = forms.CharField(disabled=True, label='手机号') #不让修改显示
    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price', 'level', 'status']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {
                'class': 'form-control',
                'placeholder': field.label,
            }   
            
    def clean_mobile(self):
        
        # 当前编辑行的id:self.instance.pk 
        
        txt_molile = self.cleaned_data["mobile"]  # 用户输入的字段
        # 排除自己以外的是不是存在
        exists = models.PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=txt_molile).exists()    
        if exists:
            raise ValidationError('手机号已存在')
        else:
            return txt_molile     
              
            
def pretty_edit(request, nid):
    '''编辑靓号，（继承原来的也可以，重写字段）
    只允许用户写价格、级别、状态的话需要另写一个只有这三个字段的modelform'''
    row_object = models.PrettyNum.objects.filter(id=nid).first()
    
    if request.method =='GET':
        form = PrettyEditModelForm(instance=row_object)
        return render(request, 'pretty_edit.html', {'form': form})
    
    form = PrettyModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/pretty/list/')
    else:
        return render(request, 'pretty_edit.html', {'form': form})
        
    
def pretty_delete(request, nid):
    '''删除靓号'''
    models.PrettyNum.objects.filter(id=nid).delete()
    return redirect('/pretty/list/')



