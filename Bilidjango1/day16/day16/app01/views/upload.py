from django.shortcuts import render, HttpResponse


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