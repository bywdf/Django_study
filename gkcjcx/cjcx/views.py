from django.shortcuts import render
from cjcx import models

from cjcx.utils.pagination import Pagination

# Create your views here.
def list(request):
    '''所有学生'''
    data_dict = {}
    search_data = request.GET.get('q','')
    if search_data:
        data_dict ['zhunkaozheng__contains']= search_data 
    # models.PrettyNum.objects.filter(**data_dict)
    
    queryset = models.Chengji.objects.filter(**data_dict)

    page_object = Pagination(request, queryset)

    context = {
        'search_data':search_data,
        'queryset':page_object.page_queryset,     # 分页数据
        'page_string': page_object.html()         # 页码
    }
    
    return render(request, 'list.html', context)

def jieguo(request, nid):
    queryset = models.Chengji.objects.filter(id=nid)
    return render(request, 'jieguo.html',{'queryset':queryset})