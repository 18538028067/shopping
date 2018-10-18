from django.conf.urls import url

from . import views

app_name = "beibei_shopping"

urlpatterns = [
    url(r"^login/$",views.user_login,name="user_login"),
    url(r"^register/$",views.user_register,name="user_register"),
    url(r"^logout/$",views.user_logout,name="user_logout"),

]
