from django.conf.urls import url
from . import views
#from djsngo.urls import path

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/result$', views.result, name='result'),
    url(r'^(?P<question_id>[0-9]+)/votes$', views.votes, name='votes'),



]
