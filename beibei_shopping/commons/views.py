from django.shortcuts import render




def index(request):
    '''首页'''
    return render(request,"index.html",{"msg":"首页"})



def code(request):

    pass

