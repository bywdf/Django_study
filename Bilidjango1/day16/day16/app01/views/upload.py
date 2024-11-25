import os
from django.shortcuts import render, HttpResponse
from app01 import models


def upload_list(request):
    if request.method == "GET":
        return render(request, 'upload_list.html')
    # username
    # print(request.POST)   # 请求发过来的数据
    # # <MultiValueDict: {'avatar': [<InMemoryUploadedFile: 小尺寸照片.jpg (image/jpeg)>]}>
    # print(request.FILES)  # 请求发过来的文件 
    
    file_object = request.FILES.get("avatar")
    print(file_object.name) # 读取文件名
    
    f = open(file_object.name, mode ='wb')
    for chunk in file_object:
        f.write(chunk)
    f.close()   
    
    return HttpResponse("....")


from django import forms
from app01.utils.bootstrap import BootStrapForm

class UpForm(BootStrapForm):
    bootstrap_exclude_fields = ['img']   # 去除此字段的form-control样式
    
    name = forms.CharField(label="姓名")
    age = forms.IntegerField(label="年龄")
    img = forms.FileField(label="头像")

def upload_form(request):
    '''form上传'''
    title = "Form上传"
    if request.method == "GET":
        form = UpForm()
        return render(request, 'upload_form.html', {'form': form})    
    
    form = UpForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        # {'name': 'sara', 'age': 11, 'img': <InMemoryUploadedFile: 1.jpg (image/jpeg)>}
        # print(form.cleaned_data)
        # 1.读取图片内容，写入到文件夹中并获取文件的路径。
        image_object = form.cleaned_data.get("img")
        db_file_path = os.path.join('static', 'img', image_object.name)
        file_path = os.path.join('app01', 'static', 'img', image_object.name)
        f = open(file_path, mode='wb')
        for chunk in image_object.chunks():
            f.write(chunk)
        f.close()
       
        # 2.将图片的文件路径写入到数据库
        models.Boss.objects.create(
            name=form.cleaned_data["name"],
            age=form.cleaned_data["age"],
            img=db_file_path,
        )
        
        return HttpResponse("...")
    return render(request, 'upload_form.html', {'form': form})    