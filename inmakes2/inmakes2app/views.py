from django.http import HttpResponse
from django.shortcuts import render
from . models import games
# Create your views here.
# def demo(request):
#    return HttpResponse('Hello World')
def index(request):
    obj=games.objects.all()
    return render(request,'index.html',{'result':obj})

# def about(request):
#     return render(request,'about.html')