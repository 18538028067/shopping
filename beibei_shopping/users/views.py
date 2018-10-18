from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

from . import models



def user_login(request):
    '''用户登录'''
    if request.method == "GET":
        return render(request, "users/login.html", {})
    elif request.method == "POST":
        username = request.POST["username"].strip()
        password = request.POST["password"].strip()

        # 验证码
        code = request.POST["code"].strip()

        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                # 将验证通过的用户信息保存在request
                login(request,user)
            else:
                return render(request, "users/login.html", {"msg": "您的账号已经被锁定，请联系管理员"})
        else:
            return render(request, "users/login.html", {"msg": "账号或者密码有误"})


def user_register(request):
    '''用户注册'''
    if request.method == "GET":
        return render(request,"users/register.html",{})
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        nickname = request.POST["nickname"]
        confirmpwd = request.POST["confirmpwd"]

        # 验证码
        code = request.POST["code"]

        # 数据验证
        if password == confirmpwd:
            if username(len) < 1:
                return render(request,"users/register.html",{"msg":"用户名不能为空！"})

            elif User.objects.get(username=username):
                return render(request,"users/register.html",{"msg":"用户名重复！"})

            elif models.UserInfo.objects.get(nickname=nickname):
                return render(request,"users/register.html",{"msg":"用户昵称重复！"})

            else:
                # 保存用户信息
                user = User.objects.create_user(username=username,password=password)
                user_info = models.UserInfo(nickname=nickname,user=user)

                user.save()
                user_info.save()

                return render(request,"users/login.html",{"msg":"恭喜您，用户注册成功！"})

        else:
            return render(request, "users/register.html", {"msg": "两次密码不一致！"})


def user_logout(request):
    '''注销用户'''
    logout(request)



