from django.shortcuts import render, redirect
from django.http import HttpResponse
from stu1.models import UserInfo

# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    # 如果是POST请求，获取用户提交的信息
    username = request.POST.get('user',)
    password = request.POST.get('pwd',)
    if username == 'admin' and password == '123':
        return HttpResponse('登录成功')
    else:
        return render(request, 'login.html', {'error_msg':'用户名或密码错误'})

def orm(request):
    # 1.新建数据库
    # UserInfo.objects.create(name = 'jhon', password = '123', age = 25)
    # UserInfo.objects.create(name = 'lisa', password = '456', age = 23)
    
    # 2.删除数据
    # UserInfo.objects.filter(id = 3).delete()
    # UserInfo.objects.filter(id = 3).delete()
    # UserInfo.objects.all().delete()
    
    # 3.获取数据
    # data_list = UserInfo.objects.all()
    # for obj in data_list:
    #     print(obj.id, obj.name, obj.password)       
    # data_list_1 = UserInfo.objects.filter(id=3)
    # row_obj = UserInfo.objects.filter(id=3).first()
    # print(data_list_1.id,)
    
    # 更新数据
    # UserInfo.objects.all().update(password = '999')
    # UserInfo.objects.filter(name = 'jhon').update(age = 18)
   
    return HttpResponse('ORM OK')

def info_list(request):
    # 获取所有用户信息
    data_list = UserInfo.objects.all()
    return render(request, 'info_list.html', {'data_list':data_list})

def info_add(request):
    if request.method == 'GET':
        return render(request,'info_add.html')
    
    # 获取用户提交的数据
    name = request.POST.get('user')
    password = request.POST.get('pwd')
    age = request.POST.get('age')
    # 添加到数据库
    UserInfo.objects.create(name = name, password = password, age = age)
    # 自动跳转
    return redirect('/info/list')

def info_delete(request):
    nid = request.GET.get('nid')
    UserInfo.objects.filter(id=nid).delete()
    return redirect('/info/list')