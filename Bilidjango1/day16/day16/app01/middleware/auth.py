from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect, HttpResponse


class AuthMiddleware(MiddlewareMixin):
    '''中间件'''
    
    def process_request(self, request):
        
        # 0.排除哪些不需要登录就能访问的页面
        # request.path_info 获取当前用户请的url
        if request.path_info == '/login/':
            return
        
        # 1.读取当前访问用户的session信息，如果能读到，说明已登陆过，就可以继续往后走
        info_dict = request.session.get('info')
        if info_dict:
            return
       
        # 2.如果没有登录信息，重新回到登录页面
        return redirect('/login/')
       
        # 如果方法中没有返回值（返回None），继续往后走
        # 如果有返回值，直接从此处返回HttpResponse、render、redirect