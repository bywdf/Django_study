from django.shortcuts import render
from django.http import HttpResponse
from stu1.models import UserInfo

# Create your views here.

def user_list(request):
    name = '小刘'
    hobby = ['篮球','足球','游泳']
    xinxi = {'adress':'linyi', 'age':20, 'sex':'男'}
    return render(request, 'user_list.html',{'name':name, 'hobby':hobby, 'xinxi':xinxi})

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
    # 新建数据库
    UserInfo.objects.create(name = 'jhon', password = '123', age = 25)
    UserInfo.objects.create(name = 'lisa', password = '456', age = 23)
    return HttpResponse('ORM OK')

# def info_list(request):
#     data_list = UserInfo.objects.all()
#     return render(request, 'info_list.html', {'data_list':data_list})