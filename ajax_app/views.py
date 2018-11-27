import time
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def handle_ajax(request):
    """
    接受ajax请求，并给以响应
    :param request:
    :return:
    """
    time.sleep(10)
    name = request.POST.get("name")
    age = request.POST.get("age")
    print(name,age)
    #......业务处理
    #响应一段字符 即可
    return HttpResponse("你好，这是给你的响应")

def handle_username(request):
    """
    验证用户名是否重复
    :param request:
    :return:
    """
    time.sleep(3)
    username = request.POST.get("username")
    #验证逻辑  XXX.objects.get(username=username)
    if username == "wanglulu":
        return HttpResponse("error")
    return HttpResponse("ok")

def test(request):
    pass
