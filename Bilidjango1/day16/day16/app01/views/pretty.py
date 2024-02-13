from django.shortcuts import render, redirect
from app01 import models

from app01.utils.pagination import Pagination
from app01.utils.form import PrettyModelForm, PrettyEditModelForm

# Create your views here.

# '''数据库查询'''
# models.PrettyNum.objects.filter(mobile='18553976921', id=2)
# # 空字典等于查询所有
# data_dict = {'mobile':'18553976921', 'id':2}
# models.PrettyNum.objects.filter(**data_dict)

# # 针对数字
# models.PrettyNum.objects.filter(id=2)          # 等于2
# models.PrettyNum.objects.filter(id__gt=2)      # 大于2
# models.PrettyNum.objects.filter(id__gte=2)     # 大于等于2
# models.PrettyNum.objects.filter(id__lt=2)     # 小于2
# models.PrettyNum.objects.filter(id__lte=2)     # 小于等于2
# # 针对字符串
# models.PrettyNum.objects.filter(mobile__startswith='135')  # 以135开头
# models.PrettyNum.objects.filter(mobile__endswith='666')  # 以135结尾
# models.PrettyNum.objects.filter(mobile__contains='6')  # 包含6筛选出来


def pretty_list(request):
    '''靓号列表'''
    
    # for i in range(300):
    #     models.PrettyNum.objects.create(mobile = '18152641135',
    #                                    price = 10,
    #                                    level = 1,
    #                                    status = 1
    #                                    )
    
    # models.PrettyNum.objects.filter(id__gte=320).delete()
    data_dict = {}
    search_data = request.GET.get('q','')
    if search_data:
        data_dict ['mobile__contains']= search_data 
    # models.PrettyNum.objects.filter(**data_dict)
    
    queryset = models.PrettyNum.objects.filter(**data_dict).order_by('-level')

    page_object = Pagination(request, queryset)

    context = {
        'search_data':search_data,
        'queryset':page_object.page_queryset,     # 分页数据
        'page_string': page_object.html()         # 页码
    }
    
    return render(request, 'pretty_list.html', context)


def pretty_add(request):
    '''靓号添加'''
    
    if request.method == "GET":
        form = PrettyModelForm()
        return render(request, 'pretty_add.html', {'form': form})  
     
    form = PrettyModelForm(data=request.POST)
    
    if form.is_valid():
        form.save()
        return redirect('/pretty/list/')
    return render(request, 'pretty_add.html', {'form': form}) 
    
            
def pretty_edit(request, nid):
    '''编辑靓号，（继承原来的也可以，重写字段）
    只允许用户写价格、级别、状态的话需要另写一个只有这三个字段的modelform'''
    row_object = models.PrettyNum.objects.filter(id=nid).first()
    
    if request.method =='GET':
        form = PrettyEditModelForm(instance=row_object)
        return render(request, 'pretty_edit.html', {'form': form})
    
    form = PrettyModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/pretty/list/')
    return render(request, 'pretty_edit.html', {'form': form})
        
    
def pretty_delete(request, nid):
    '''删除靓号'''
    models.PrettyNum.objects.filter(id=nid).delete()
    return redirect('/pretty/list/')



