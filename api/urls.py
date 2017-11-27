from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^app/', views.app, name='app'),
    url(r'^user/', views.user, name='user'),
    url(r'^data/', views.data, name='data'),
]
