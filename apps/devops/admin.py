from django.contrib import admin

# Register your models here.

from apps.devops.models import serverList

admin.site.register(serverList)