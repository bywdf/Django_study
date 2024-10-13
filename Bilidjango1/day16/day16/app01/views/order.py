import json
import random
from datetime import datetime
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from app01 import models
from app01.utils.bootstrap import BootStrapModelForm


class OrderModelForm(BootStrapModelForm):
    class Meta:
        model = models.Order
        # fields = '__all__'
        # fields = ['']
        exclude = ['oid', 'admin']
        
        
def order_list(request):
    form = OrderModelForm()
    return render(request, 'order_list.html', {'form': form})


@csrf_exempt
def order_add(request):
    '''新建订单（Ajax请求）'''
    form = OrderModelForm(data=request.POST)
    if form.is_valid():
        
        # oid 订单号：额外增加一些不是用户输入的值（自己计算出来）
        form.instance.oid = datetime.now().strftime('%Y%m%d%H%M%S') + str(random.randint(1000, 9999))

        # 固定管理员ID，去session里面去获取
        # form.instance.admin_id = 当前登录系统的管理员ID
        form.instance.admin_id = request.session['info']['id']
        
        # 保存到数据库
        form.save()
        return JsonResponse({"status":True}) # 等价于下面HttpResponse(json.dumps({'status:true'}))
        # return HttpResponse(json.dumps({'status:true'}))
    return JsonResponse({'status':False, 'error':form.errors})
