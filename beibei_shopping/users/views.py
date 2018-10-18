from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from . import models



def user_login(request):
    '''用户登录'''
    if request.method == "GET":
        return render(request, "users/login.html", {})
    elif request.method == "POST":
        username = request.POST["username"].strip()
        password = request.POST["password"].strip()

        # 验证码
        # code = request.POST["code"].strip()

        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                # 将验证通过的用户信息保存在request
                login(request,user)
                return render(request, "users/userinfo.html", {"user": user})
            else:
                return render(request, "users/login.html", {"msg": "您的账号已经被锁定，请联系管理员"})
        else:
            return render(request, "users/login.html", {"msg": "账号或者密码有误"})


def user_register(request):
    '''用户注册'''
    if request.method == "GET":
        return render(request,"users/register.html",{"msg":"请认真填写如下选项"})
    elif request.method == "POST":
        # 接受参数

        username = request.POST.get("username").strip()
        password = request.POST.get("password").strip()
        confirmpwd = request.POST.get("confirmpwd").strip()
        nickname = request.POST.get("nickname").strip()

        # 数据校验
        if len(username) < 1:
            return render(request,"users/register.html",{"msg":"用户名不能为空！！"})

        if len(password) < 6:
            return render(request,"users/register.html",{"msg":"密码长度不能小于6位！！"})

        if password != confirmpwd:
            return render(request,"users/register.html",{"msg":"两次密码不一致！！"})

        # 用户名是否重复
        try:
            User.objects.get(username=username)
            return render(request,"users/register.html",{"msg":"用户名重复！"})
        except:

            try:
                # 判断昵称是否重复
                models.UserInfo.objects.get(nickname=nickname)
                return render(request,"users/register.html",{"msg":"昵称重复！"})
            except:
                # 保存用户信息
                user = User.objects.create_user(username=username,password=password)
                user_info = models.UserInfo(nickname=nickname,user=user)
                user.save()
                user_info.save()
                return render(request,"users/login.html",{"msg":"用户注册成功"})



@login_required
def user_logout(request):
    '''注销用户'''
    logout(request)
    return render(request, "users/login.html", {"msg": "退出成功！"})


@login_required
def user_info(request):

    pass










