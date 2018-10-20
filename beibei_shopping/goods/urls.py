from django.conf.urls import url

from . import views

app_name = "goods"


urlpatterns = [
    url(r'^add/$',views.add,name="add")
    # url(r'')
]

