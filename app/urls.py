from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^members$', views.members, name='members'),
    url(r'^rep$', views.rep, name='rep'),
    url(r'^events$', views.events, name='events'),
    url(r'^gallery$', views.gallery, name='gallery'),
    url(r'^contact$', views.contact, name='contact'),
]

