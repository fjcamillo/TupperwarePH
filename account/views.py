from django.shortcuts import render
from .forms import PostForm
# Create your views here.



def index(request):
    form = PostForm()

    context = {

    }
    return render(request, 'account/account.html', context)