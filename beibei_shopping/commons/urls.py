from django.conf.urls import url

from . import views


app_name = "commons"

urlpatterns = [
    url(r"^$",views.index,name="index"),
    url(r"^code/$",views.code,name="code"),

]