from django.shortcuts import render
from django.http import HttpResponse
from zhkh import models

# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    id = int(request.POST.get('id'))
    pwd = request.POST.get('pwd')
    
    username = models.Teacher.objects.filter(id=id).first().id
    password = models.Teacher.objects.filter(id=id).first().password
    
    if password == pwd:
        return HttpResponse('123')
    else:
        return render(request, 'login.html', {'error_msg':'用户名或密码错误'})
# def teacher_score_list(request):
    
#     return render(request, 'teacher_score_list.html')