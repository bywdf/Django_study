from django.shortcuts import render
from django import forms

from app01 import models
from app01.utils.bootstrap import BootStrapForm
from app01.utils.encrypt import md5

class LoginForm(BootStrapForm):
    username = forms.CharField(
        label='用户名',
        widget=forms.TextInput,
        required=True,
        )
    password = forms.CharField(
        label='密码',
        widget=forms.PasswordInput(render_value=True),
        required=True,
        )
    
    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)
    
# class LoginModelForm(forms.ModelForm):
#     class Meta:
#         model = models.Admin
#         fields = ['username', 'password']
    
    
def login(request):
    '''登录'''
    
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    
    form = LoginForm(data=request.POST)
    if form.is_valid():
        # 验证成功，获取到的用户名和密码 form.cleaned_data（是字典）
        
        # 去数据库校验用户名和密码是否正确,获取用户对象、None
        # admin_object = models.Admin.objects.filter(username='xxx', password='xxx').first()
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error('password', '用户名或密码错误')  # 主动的在form中添加错误信息
            return render(request, 'login.html', {'form': form})
        
        # 用户名和密码正确
        # 网站生成随机字符串；写到用户浏览器的cookie中；写入到session中；
        
    return render(request, 'login.html', {'form': form})
