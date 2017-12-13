import re
from django.shortcuts import render,HttpResponse
from django.conf import settings
# Create your views here.
def index(request):
    return HttpResponse("主页")


def userinfo(request):
    dict =[
        {"id":1,"name":"xx1"},
        {"id":2,"name":"xx2"},
        {"id":3,"name":"xx3"},
        {"id":4,"name":"xx4"},
    ]

    return render(request,"userinfo.html",{"dict":dict,})


def order(request):

    return render(request,"order.html")


def adduser(request):
    return render(request,"userinfoadd.html")


def edituser(request,nid):
    return HttpResponse("修改用户信息")


def deluser(request,nid):
    return HttpResponse("删除用户信息")
