from django.shortcuts import render

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

