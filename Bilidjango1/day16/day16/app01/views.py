from django.shortcuts import render, redirect
from app01 import models

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
    return render(request, 'user_list.html',{'queryset':queryset})


def user_add(request):
    '''添加用户'''
    context = {
        'gender_choices': models.UserInfo.gender_choices,
        'depart_list':models.Department.objects.all(),
    }
    return render(request,'user_add.html', context)

from django import forms
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


    