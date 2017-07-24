from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.devops.models import serverList
from django.db.models import Count, Sum
from django.core.paginator import Paginator
import json
import datetime

@login_required()
def tables(request):
    return render(request, 'devops/tables.html')

@login_required()
def serverInfo(request):
    if request.method == 'GET':
        print(request.GET)
        print(request.POST.getlist('btSelectItem')) #获取checkbox信息
        limit = request.GET.get('limit')
        offset = request.GET.get('offset')  # how many items in total in the DB
        search = request.GET.get('search')
        sort_column = request.GET.get('sort')
        order = request.GET.get('order')
        if search:
            all_records = serverList.objects.filter(instance=search, hostname=search, ip=search, hostcomputer=search, cpucore=search, memory=search, system=search, systemdisk=search, datadisk=search, user=search, use=search, remark=search)
        else:
            all_records = serverList.objects.all()

        if sort_column:
            if sort_column in ['instance', 'hostname', 'ip', 'hostcomputer', 'cpucore', 'memory', 'system', 'systemdisk', 'datadisk', 'user', 'use', 'remark', 'alter_time']:
                if order == 'desc':
                    sort_column = '-%s' % sort_column
                all_records = serverList.objects.all().order_by(sort_column)

        all_records_count = all_records.count()
        if not offset:
            offset = 0
        if not limit:
            limit = 10
        pageinator = Paginator(all_records, limit)
        page = int(int(offset) / int(limit) + 1)
        response_data = {'total': all_records_count, 'rows': []}
        for ser in pageinator.page(page):
            response_data['rows'].append({
                'instance': ser.instance if ser.instance else '',
                'hostname': ser.hostname if ser.hostname else '',
                'ip': ser.ip if ser.ip else '',
                'hostcomputer': ser.hostcomputer if ser.hostcomputer else '',
                'cpucore': ser.cpucore if ser.cpucore else '',
                'memory': ser.memory if ser.memory else '',
                'system': ser.system if ser.system else '',
                'systemdisk': ser.systemdisk if ser.systemdisk else '',
                'datadisk': ser.datadisk if ser.datadisk else '',
                'user': ser.user if ser.user else '',
                'use': ser.use if ser.use else '',
                'remark': ser.remark if ser.remark else '',
                'alter_time': ser.alter_time.strftime('%Y-%m-%d %H:%M') if ser.alter_time else '',
            })
    # return HttpResponse(json.dumps(response_data))
    return JsonResponse(response_data)

@login_required()
def addServerInfo(request):
    print(request.POST)
    if request.method == 'POST':
        pass
    return HttpResponseRedirect('/devops/')