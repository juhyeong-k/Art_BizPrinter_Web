from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.shortcuts import render
from django.shortcuts import redirect
from django.template import loader
import datetime

# Create your views here.
def home(request):
    return render(request, 'first.html', {})

def about(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def create(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
