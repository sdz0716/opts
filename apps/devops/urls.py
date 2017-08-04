from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.tables, name='tables'),
    url(r'^tables', views.tables, name='tables'),
    url(r'^serverinfo', views.serverInfo, name='serverinfo'),
    url(r'^addserverinfo', views.addServerInfo, name='addserverinfo'),
    url(r'^modifyserverinfo/(\d+)/$', views.modifyServerInfo, name='modifyserverinfo'),
    url(r'^modifyserverinfo/$', views.modifyServerInfo, name='modifyserverinfoPost'),
]