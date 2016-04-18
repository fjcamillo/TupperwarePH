from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'aboutus/aboutus.html')

def reseller(request):
    return render(request, 'aboutus/reseller.html', {'reseller': ['name', 'contact']})

