from django.shortcuts import render, redirect
from django import forms
from django.core.exceptions import ValidationError

from app01 import models

from app01.utils.pagination import Pagination
from app01.utils.bootstrap import BootStrapModelForm
from app01.utils.encrypt import md5


def admin_list(request):
    '''管理员列表'''
    
    # info_dict = request.session['info'] 获取登录信息
    # info_dict[id]
    
    # 构造搜索
    data_dict = {}
    search_data = request.GET.get('q','')
    if search_data:
        data_dict['username__contains']= search_data 
    
    # 根据搜索条件去数据库获取
    queryset = models.Admin.objects.filter(**data_dict)
    
    # 分页
    page_object = Pagination(request, queryset)
    context = {
        'search_data': search_data,
        'queryset': page_object.page_queryset,     # 分页数据
        'page_string': page_object.html(),         # 生成页码
    }

    return render(request, 'admin_list.html', context)


class AdminModelForm(BootStrapModelForm):
    
    confirm_password = forms.CharField(
        label='确认密码',
        widget=forms.PasswordInput(render_value=True),
        )
    
    class Meta:
        model = models.Admin
        fields = ['username', 'password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }
        
    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)
    
    def clean_confirm_password(self):
        pwd = self.cleaned_data.get('password')
        confirm = md5(self.cleaned_data.get('confirm_password'))
        if confirm != pwd:
            raise ValidationError("两次输入的密码不一致")
        return confirm  # 返回什么。此字段就保存此数据库
             

def admin_add(request):
    '''添加管理员'''
    
    title = '新建管理员'
    if request.method == 'GET':
        form = AdminModelForm()
        return render(request, 'change.html', {'form': form, 'title': title})
    
    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    
    return render(request, 'change.html', {'form': form, 'title': title})


class AdminEditModelForm(BootStrapModelForm):
    class Meta:
        model = models.Admin
        fields = ['username']


def admin_edit(request, nid):
    '''编辑管理员'''
    # 对象 / None
    title = '编辑管理员'
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return render(request,'error.html', {"msg":"数据不存在"})

    # 要是单独只能修改某几个字段，单独写一个form类
    if request.method == 'GET':
        form = AdminEditModelForm(instance=row_object) 
        return render(request, 'change.html', {'form':form, 'title': title})
    form = AdminEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, 'change.html', {'form': form, 'title': title})


def admin_delete(request, nid):
    '''删除管理员'''
    models.Admin.objects.filter(id=nid).delete()
    return redirect('/admin/list')


class AdminRestModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label='确认密码',
        widget=forms.PasswordInput(render_value=True),
        )
    
    class Meta:
        model = models.Admin
        fields = ['password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }  
        
    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        md5_pwd = md5(pwd)
        
        # 去数据库校验新输入的密码和之前的密码是否是一样的
        exists = models.Admin.objects.filter(id=self.instance.pk, password=md5_pwd).exists()
        if exists:
            raise ValidationError('密码不能与之前的相同')
        return md5(pwd)
    
    def clean_confirm_password(self):
        pwd = self.cleaned_data.get('password')
        confirm = md5(self.cleaned_data.get('confirm_password'))
        if confirm != pwd and pwd!=None:
            raise ValidationError("两次输入的密码不一致")
        return confirm  # 返回什么。此字段就保存此数据库
               
        
def admin_reset(request, nid):
    '''重置密码'''
   
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return render(request,'error.html', {"msg":"数据不存在"})
    
    title = '重置密码 - {}'.format(row_object.username)
    if request.method == 'GET':
        form =  AdminRestModelForm()
        return render(request, 'change.html', {'form': form, 'title': title})
    
    form =  AdminRestModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/list')
    return render(request, 'change.html', {'form': form, 'title': title})