from django.shortcuts import render
from django.http import JsonResponse

def chart_list(request):
    ''' 数据统计页面 '''
    return render(request, 'chart_list.html')


def chart_bar(request):
    '''构造柱状图的数据'''
    # 数据可以到数据库中获取
    legend = ['张三','李四'] 
    x_axis = ['1月', '2月', '3月', '4月', '5月', '6月']
    series_list= [
        {
            'name': '张三',
            'type': 'bar',
            'data': [5, 20, 36, 10, 10, 20]
        },
        {
        'name': '李四',
        'type': 'bar',
        'data': [25, 10, 16, 40, 20, 80]
        }
    ]
    
    result = {
        'status': True,
        'data':{
            'legend': legend,
            'series_list': series_list,
            'x_axis': x_axis,
        }
    }
    return JsonResponse(result)
    