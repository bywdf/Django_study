from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from app01 import models
from app01.utils.bootstrap import BootStrapModelForm


class OrderModelForm(BootStrapModelForm):
    class Meta:
        model = models.Order
        # fields = '__all__'
        # fields = ['']
        exclude = ['oid']
        
        
def order_list(request):
    form = OrderModelForm()
    return render(request, 'order_list.html', {'form': form})


@csrf_exempt
def order_add(request):
    '''新建订单（Ajax请求）'''
    form = OrderModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse
