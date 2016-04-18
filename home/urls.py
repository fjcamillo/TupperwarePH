from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^sample$', views.index, name='index'),
    url(r'^$', views.shella, name='sample')
]
