from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

@login_required()
def home(request):
    return render(request, 'home/home.html')