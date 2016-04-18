from django.shortcuts import render
# from django.http import HttpResponse


def index(request):
    return render(request, 'home/home.html')


def sample(request):
    return render(request, 'home/sam.html')


def shella(request):
    return render(request, 'home/FINAL.html')

