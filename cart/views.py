from django.shortcuts import render, get_object_or_404
from .models import onClickCart
# Create your views here.


def index(request):
    inside_cart = onClickCart.objects.all()
    va = 0
    context = {
        'object_list': inside_cart,
        'va': va

    }
    return render(request, 'cart/cart.html', context)


def sample_test(request):
    inside_cart = onClickCart.objects.all()
    va = 0
    context = {
        'object_list': inside_cart,
        'va': va
    }
    return render(request, 'cart/sample_cart.html', context)


