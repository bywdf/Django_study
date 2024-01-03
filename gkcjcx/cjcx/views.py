from django.shortcuts import render

# Create your views here.
def chaxun(request):
    return render(request, 'chaxun.html')

def jieguo(request):
    return render(request, 'jieguo.html')