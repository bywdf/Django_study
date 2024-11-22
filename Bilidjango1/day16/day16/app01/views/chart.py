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


def chart_pie(request):
    '''构造饼图'''
    
    db_data_list = [
        {'value': 1048, 'name': 'Search Engine'},
        {'value': 735, 'name': 'Direct'},
        {'value': 580, 'name': 'Email'},
        {'value': 484, 'name': 'Union Ads'},
        {'value': 300, 'name': 'Video Ads'},
    ]
    
    result = {
        'status': True,
        'data': db_data_list,
    }
    return JsonResponse(result)


def chart_line(request):
    '''构造折线图'''
    
    x_axis = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    series_list = [150, 230, 224, 218, 135, 147, 260]    
    
    result = {
        'status': True,
        'data': {
            'x_axis': x_axis,
            'series_list': series_list,
        }
        }
        
    return JsonResponse(result)
        