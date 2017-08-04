from django.forms import ModelForm
import apps.devops.models
import UnixTimestampField
import datetime
from django.utils.translation import ugettext_lazy as _
from django.forms import widgets as Fwidgets

class serverInfoForm(ModelForm):
    class Meta:
        model = apps.devops.models.serverList
        fields = '__all__'
        # exclude = ['alter_time']
        # fields = ('instance', 'hostname' )
        labels = {
            'instance': _('实例'),
            'hostname': _('主机名'),
            'ip': _('IP'),
            'hostcomputer': _('宿主机'),
            'cpucore': _('CPU'),
            'memory': _('内存'),
            'system': _('系统'),
            'systemdisk': _('系统盘'),
            'datadisk': _('数据盘'),
            'user': _('使用者'),
            'use': _('用途'),
            'remark': _('备注'),
            # 'alter_time': _('修改时间'),
        }
        widgets = {
            'instance': Fwidgets.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入实例名称'}),
            'hostname': Fwidgets.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入主机名'}),
            'ip': Fwidgets.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入服务器IP'}),
            'hostcomputer': Fwidgets.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入宿主机IP'}),
            'cpucore': Fwidgets.NumberInput(attrs={'class': 'form-control', 'placeholder': '请输入CPU核心数量'}),
            'memory': Fwidgets.NumberInput(attrs={'class': 'form-control', 'placeholder': '请输入内存大小'}),
            'system': Fwidgets.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入系统名称'}),
            'systemdisk': Fwidgets.NumberInput(attrs={'class': 'form-control', 'placeholder': '请输入系统盘容量'}),
            'datadisk': Fwidgets.NumberInput(attrs={'class': 'form-control', 'placeholder': '请输入数据盘容量'}),
            'user': Fwidgets.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入使用者或组别名称'}),
            'use': Fwidgets.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入服务器用途'}),
            'remark': Fwidgets.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入备注信息'}),
            # 'alter_time': Fwidgets.TextInput(attrs={'class': 'form-control'}),
        }
        error_messages = {
        }
        help_texts = {
        }