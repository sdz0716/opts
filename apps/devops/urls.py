from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.tables, name='tables'),
    url(r'^serverinfo', views.serverInfo, name='serverinfo'),
    url(r'^addserverinfo', views.addServerInfo, name='addserverinfo'),
]