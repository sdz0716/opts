from django.db import models
import UnixTimestampField
import datetime
# Create your models here.

class serverList(models.Model):
    instance = models.CharField(max_length=255)
    hostname = models.CharField(max_length=255)
    ip = models.CharField(max_length=100, unique=True)
    hostcomputer = models.CharField(max_length=255)
    cpucore = models.CharField(max_length=255)
    memory = models.CharField(max_length=255)
    system = models.CharField(max_length=255)
    systemdisk = models.CharField(max_length=255)
    datadisk = models.CharField(max_length=255, blank=True, null=True)
    user = models.CharField(max_length=100)
    use = models.CharField(max_length=255)
    remark = models.CharField(max_length=255, blank=True, null=True)
    alter_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return u'%s' % self.ip