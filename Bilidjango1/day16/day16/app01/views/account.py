from django.shortcuts import render, HttpResponse, redirect
from django import forms
from io import BytesIO

from app01 import models
from app01.utils.bootstrap import BootStrapForm
from app01.utils.encrypt import md5
from app01.utils.code import check_code


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
    code = forms.CharField(
        label='验证码',
        widget=forms.TextInput,
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
        # {'username':'wdf', 'password': '123', 'code': 'xxxx'}
        user_input_code = form.cleaned_data.pop('code')  # 剔除掉验证码
        image_code = request.session.get('image_code', '')
        if image_code.lower() != user_input_code.lower():
            form.add_error('code', '验证码错误')  # 主动的在form中添加错误信息
            return render(request, 'login.html', {'form': form})

        # 去数据库校验用户名和密码是否正确,获取用户对象、None
        # admin_object = models.Admin.objects.filter(username='xxx', password='xxx').first()
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error('password', '用户名或密码错误')  # 主动的在form中添加错误信息
            return render(request, 'login.html', {'form': form})

        # 用户名和密码正确
        # 网站生成随机字符串；写到用户浏览器的cookie中；写入到session中；
        request.session['info'] = {'id': admin_object.id, 'name': admin_object.username}
        request.session.set_expiry(60*60*24*3) # 设置session的过期时间为3天
        
        return redirect("/admin/list/")
    return render(request, 'login.html', {'form': form})


def image_code(request):
    '''生成验证码'''

    # 调用pillow函数，生成图片
    img, code_string = check_code()

    # 写入到自己的session中，以便后续获取验证码再进行校验
    request.session['image_code'] = code_string
    # 给Session设置一个60秒超时
    request.session.set_expiry(60)

    stream = BytesIO()
    img.save(stream, 'png')
    return HttpResponse(stream.getvalue())


def logout(request):
    '''注销'''

    request.session.clear()
    return redirect('/login/')
