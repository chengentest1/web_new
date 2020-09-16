from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.

def hello(request):
    return HttpResponse("hello world")

def user(request):
    res={
        "code":"200",
        "msc":"成功",
        "data":[]

    }
    return JsonResponse(res)

def login(request):
    return render(request,'login.html',{"year":"2020","month":"09"})

def archive(request,year,month):
    res={
        "code":"200",
        "msg":"成功success",
        "data":[
            {
                "year":year,
                "month":month
            }
        ]
    }
    return JsonResponse(res)