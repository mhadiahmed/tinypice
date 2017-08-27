from django.conf.urls import url,include
from .  import views

urlpatterns = [
    url(r'^save/$', views.home,name='home'),
]