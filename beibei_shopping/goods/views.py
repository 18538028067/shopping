from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse

from . import models


def add(request):
    '''增加商品'''
    if request.method == "GET":
        return render(request,"goods/add.html")
    else:
        pass
