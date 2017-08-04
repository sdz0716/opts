from django.db import models
import UnixTimestampField
import datetime
# Create your models here.

class serverList(models.Model):
    instance = models.CharField(max_length=255)
    hostname = models.CharField(max_length=255)
    ip = models.CharField(max_length=100, unique=True)
    hostcomputer = models.CharField(max_length=255)
    cpucore = models.IntegerField()
    memory = models.IntegerField()
    system = models.CharField(max_length=255)
    systemdisk = models.IntegerField()
    datadisk = models.IntegerField(null=True, blank=True)
    user = models.CharField(max_length=100)
    use = models.CharField(max_length=255)
    remark = models.CharField(max_length=255, blank=True)
    alter_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u'%s' % self.ip