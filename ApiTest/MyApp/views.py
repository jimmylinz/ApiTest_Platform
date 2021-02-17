from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from MyApp.models import *
# Create your views here.
@login_required
def welcome(request):
    print("进来了")
    return render(request,'welcome.html')

def case_list(requset):
    print("用例库")
    return render(requset,'case_list.html')

#进入主页
@login_required
def home(request):
    print("home")
    return render(request,'welcome.html',{"whichHTML":"home.html","ord":""})

#返回子页面
def child(request,eid,ord):
    print("child")
    return render(request,eid)

def login(request):
    print("login")
    return render(request,'login.html')

def login_action(request):
    u_name = request.GET['username']
    p_word = request.GET['password']

    from django.contrib import auth
    user = auth.authenticate(username=u_name,password=p_word)
    if user is not None:
        auth.login(request,user)
        request.session['user'] = u_name
        return HttpResponse('成功')
    else:
        return HttpResponse('失败')

def register_action(request):
    u_name = request.GET['username']
    p_word = request.GET['password']
    #开始联通django用户表
    from django.contrib.auth.models import User
    try:
        user = User.objects.create_user(username=u_name,password=p_word)
        user.save()
        return HttpResponse("注册成功！")
    except:
        return HttpResponse("改用户名已存在，请更换用户名重试~")

def logout(request):
    print("退出")
    from django.contrib import auth
    auth.logout(request)
    return HttpResponseRedirect('/login/')

#吐槽函数
def pei(request):
    print("吐槽")
    tucao_text = request.GET['tucao_text']
    DB_tucao.objects.create(user=request.user.username,text=tucao_text)
    return HttpResponse("写入成功")

def api_help(request):
    print("帮助")
    return render(request,'welcome.html',{"whichHTML":"help.html","old":""})