from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required



def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('../home/')
        else:
            return render(request, 'login/login.html', {'user': user})
    else:
        return render(request, 'login/login.html')
        # raise Http404('wrong')