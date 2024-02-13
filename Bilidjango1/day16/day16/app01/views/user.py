from django.shortcuts import render, redirect
from app01 import models

from app01.utils.pagination import Pagination
from app01.utils.form import UserModelForm

# Create your views here.

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
    return render(request, 'user_form_add.html', {'form':form})


def user_delete(request, nid):
    '''删除用户'''
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list/')
