from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about', views.about, name='about'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^districts', views.districts, name='districts'),
    url(r'^map', views.map, name='map'),
    url(r'^zoomed', views.zoomed, name='zoomed'),
]