from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET

from . import models

@login_required
def add(request):
    '''增加店铺'''
    if request.method == "GET":
        return render(request,"store/add.html",{})
    else:
        name = request.POST["name"].strip()
        intro = request.POST["intro"].strip()
        try:
            cover = request.FILES["cover"]
            store = models.Store(name=name,intro=intro,cover=cover,user=request.user)
            store.save()
        except:
            store = models.Store(name=name,intro=intro,user=request.user)
        store.save()
        # return redirect(reverse("store:detail",kwargs={"s_id":store.id}))
        return redirect(reverse("store:detail", kwargs={"s_id": store.id}))


@require_GET
@login_required
def list(request):
    '''店铺列表'''
    stores = models.Store.objects.filter(user=request.user,status__in=[0,1])
    return render(request,"store/list.html",{"stores":stores})


@login_required
def update(request,s_id):
    '''修改店铺'''
    if request.method == "GET":
        store = models.Store.objects.get(pk=s_id)
        return render(request,"store/update.html",{"store":store})
    else:
        name = request.POST["name"].strip()
        intro = request.POST["intro"].strip()

        store = models.Store.objects.get(pk=s_id)
        store.name = name
        store.intro = intro
        try:
            cover = request.FILES["cover"]
            store.cover = cover
        except:
            pass
        store.save()

        return redirect(reverse("store:detail",kwargs={"s_id":store.id}))



@require_GET
@login_required
def detail(request,s_id):
    '''店铺详情'''
    store = models.Store.objects.get(pk=s_id)
    return render(request,"store/detail.html",{"store":store})


@require_GET
@login_required
def change(request,s_id,status):
    '''修改店铺状态'''
    store = models.Store.objects.get(id=s_id)
    store.status = int(status)
    store.save()
    if store.status == 2:
        return redirect(reverse("store:list"))
    else:
        return render(request, "store/detail.html", {"store": store})







