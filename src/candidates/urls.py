from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about', views.about, name='about'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^districts', views.districts, name='districts'),
    url(r'^districts-zoomed', views.districts-zoomed, name='districts-zoomed'),
]