
from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})


def base(request):
    return render(request, 'base.html', {})

def projects(request):
    return render(request, 'projects.html', {})

def about(request):
    return render(request, 'about.html', {})

def uhoh(request):
    return render(request, 'uhoh.html', {})

def github(request):
    return render(request, 'www.github.com/murphycf', {})