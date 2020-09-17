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



#个人信息
def personinfo(request):
    context={
        "name":"上海悠悠",
        "n_name":"悠悠",
        "age":"20",
        "fancy":["python","request","pytest"],
        "blog":{
            "url":"http://www.cnblogs.com/youyouketang/",
            "img":"http://pic.cnblogs.com/avatar/1070438/20161126151035.png"
        }
     }

    class Myblog():
        def __init__(self):
            self.guanzhu=1000
            self.fensi=10
        def guanzhu(self):
            return self.guanzhu

        def fensi(self):
            return self.fensi
    myblog=Myblog() #实例对象
    context["myblog"]=myblog
    return render(request,'personinfo.html',context)



def daohang(request):
    context={"name_list":[
         {"type": "科普读物","value": ["宇宙知识", "百科知识", "科学世界", "生物世界"]}
        ,{"type": "计算机/网络","value": ["Java", "Python", "C语言"]}
        ,{"type": "建筑","value": ["标准/规范", "室内设计", "建筑科学", "建筑文化"]}
             ]}
    return render(request,"daohang.html",context)





















