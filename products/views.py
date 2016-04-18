from django.shortcuts import render, get_object_or_404
from .models import specific_products
from cart.models import onClickCart
from .forms import PostForm
# Create your views here.


def index(request):
    # filtered_category = specific_products.objects.filter(specific_products.product_category)
    context_index = {

    }
    return render(request, 'v4/Deals.html', context_index)


def bags(request):
    queryset = specific_products.product_category
    category_names = get_object_or_404(specific_products, product_category='Bag')
    return render(request, '')


def specificproductview(request, id):
    product_name_to_create = get_object_or_404(specific_products, id=id)
    ohyeah = PostForm()
    if request.method == "POST":
        onClickCart.objects.create()
    context_svp = {
        'name': product_name_to_create.product_name,
        'category': product_name_to_create.product_category,
        'price': product_name_to_create.product_price,
        'image': product_name_to_create.product_image,
        'description': product_name_to_create.product_description,
        'id': product_name_to_create.id,
        'promo': product_name_to_create.product_promo,
        'stock': product_name_to_create.product_stock,
    }
    return render(request, 'specific-products/specific_product.html', context_svp)


def men(request):
    return render(request, 'v4/Mens.html')


def women(request):
    return render(request, 'v4/Womens.html')


def kids(request):
    forshowcase = specific_products.objects.get(id=17)
    form_product1 = PostForm()
    form_product2 = PostForm()
    form_product3 = PostForm()
    form_product4 = PostForm()
    form_product5 = PostForm()
    form_product6 = PostForm()
    form_product7 = PostForm()
    form_product8 = PostForm()
    form_product9 = PostForm()
    form_product10 = PostForm()
    form_product11 = PostForm()
    form_product12 = PostForm()

    if request.method=="POST" and "product_one" in request.POST:
        onClickCart.objects.create(product_cart_title="Baby Care Plus Blue Baby Bath", product_cart_price=280, product_cart_image="")
    if request.method=="POST" and "product_two" in request.POST:
        onClickCart.objects.create(product_cart_title="Baby Care Plus Blue Baby Cologne", product_cart_price=280, product_cart_image="")
    if request.method=="POST" and "product_three" in request.POST:
        onClickCart.objects.create(product_cart_title="Baby Care Plus Blue Baby Lotion", product_cart_price=369, product_cart_image="")
    if request.method=="POST" and "product_four" in request.POST:
        onClickCart.objects.create(product_cart_title="Baby Care Plus Blue Baby Powder", product_cart_price=229, product_cart_image="")
    if request.method=="POST" and "product_five" in request.POST:
        onClickCart.objects.create(product_cart_title="Baby Care Plus Blue Baby Shampoo", product_cart_price=240, product_cart_image="")
    if request.method=="POST" and "product_six" in request.POST:
        onClickCart.objects.create(product_cart_title="Baby Care Plus Blue Baby Soap", product_cart_price=175, product_cart_image="")
    if request.method=="POST" and "product_seven" in request.POST:
        onClickCart.objects.create(product_cart_title="Baby Care Plus Calming Baby Bath", product_cart_price=240, product_cart_image="")
    if request.method=="POST" and "product_eight" in request.POST:
        onClickCart.objects.create(product_cart_title="Baby Care Plus Calming Baby Lotion", product_cart_price=250, product_cart_image="")
    if request.method=="POST" and "product_nine" in request.POST:
        onClickCart.objects.create(product_cart_title="Baby Care Plus Calming Baby Powder", product_cart_price=229, product_cart_image="")
    if request.method=="POST" and "product_ten" in request.POST:
        onClickCart.objects.create(product_cart_title="Baby Care Plus Milk Baby Lotion", product_cart_price=369, product_cart_image="")
    if request.method=="POST" and "product_eleven" in request.POST:
        onClickCart.objects.create(product_cart_title="Baby Care Plus Milk Baby Powder", product_cart_price=229, product_cart_image="")
    if request.method=="POST" and "product_twelve" in request.POST:
        onClickCart.objects.create(product_cart_title="Baby Care Plus Milk Baby Soap", product_cart_price=185, product_cart_image="")

    context = {
        'form1': form_product1,
        'form2': form_product2,
        'form3': form_product3,
        'form4': form_product4,
        'form5': form_product5,
        'form6': form_product6,
        'form7': form_product7,
        'form8': form_product8,
        'form9': form_product9,
        'form10': form_product10,
        'form11': form_product11,
        'form12': form_product12,
    }
    return render(request, 'v4/Kids.html', context)


def tupperware(request):
    return render(request, 'v4/Tupperware.html')



#---> Sub categories
#-------> Kids

def kidone(request):
    return render(request, 'v4/Kids/Pages/Kids1.html')


def kidtwo(request):
    return render(request, 'v4/Kids/Pages/Kids2.html')


def kidThree(request):
    return render(request, 'v4/Kids/Pages/Kids3.html')


def kidFour(request):
    return render(request, 'v4/Kids/Pages/Kids4.html')


def kidFive(request):
    return render(request, 'v4/Kids/Pages/Kids5.html')


#------> Mens Pages


def menone(request):
    return render(request, 'v4/Mens/Pages/Mens1.html')


def mentwo(request):
    return render(request, 'v4/Mens/Pages/Mens2.html')


def menthree(request):
    return render(request, 'v4/Mens/Pages/Mens3.html')


def menfour(request):
    return render(request, 'v4/Mens/Pages/Mens4.html')


#------> Mens subPages


def menbodyone(request):
    return render(request, 'v4/Mens/Subs/Mens_Body1.html')


def menbodytwo(request):
    return render(request, 'v4/Mens/Subs/Mens_Body2.html')


def menbodythree(request):
    return render(request, 'v4/Mens/Subs/Mens_Body3.html')


def mendeoone(request):
    return render(request, 'v4/Mens/Subs/Mens_Deo1.html')


def mendeotwo(request):
    return render(request, 'v4/Mens/Subs/Mens_Deo2.html')


#--------------------> tupperware


def tupperwareone(request):
    return render(request, 'v4/Tupperware/Pages/Tupperware1.html')


def tupperwaretwo(request):
    return render(request, 'v4/Tupperware/Pages/Tupperware2.html')


def tupperwarethree(request):
    return render(request, 'v4/Tupperware/Pages/Tupperware3.html')


#------------------------> women


def womenone(request):
    return render(request, 'v4/Womens/Pages/Womens1.html')


def womentwo(request):
    return render(request, 'v4/Womens/Pages/Womens2.html')


def womenthree(request):
    return render(request, 'v4/Womens/Pages/Womens3.html')


def womenfour(request):
    return render(request, 'v4/Womens/Pages/Womens4.html')


def womenfive(request):
    return render(request, 'v4/Womens/Pages/Womens5.html')


def womensix(request):
    return render(request, 'v4/Womens/Pages/Womens6.html')


def womenseven(request):
    return render(request, 'v4/Womens/Pages/Womens7.html')


def womeneight(request):
    return render(request, 'v4/Womens/Pages/Womens8.html')


def womennine(request):
    return render(request, 'v4/Womens/Pages/Womens9.html')


def womenten(request):
    return render(request, 'v4/Womens/Pages/Womens10.html')


def womeneleven(request):
    return render(request, 'v4/Womens/Pages/Womens11.html')

def womentwelve(request):
    return render(request, 'v4/Womens/Pages/Womens12.html')


#--------------------------------------> Women Subs


def womendeoone(request):
    return render(request, 'v4/Womens/Subs/Womens_Deo1.html')


def womendeotwo(request):
    return render(request, 'v4/Womens/Subs/Womens_Deo2.html')


def womendeothree(request):
    return render(request, 'v4/Womens/Subs/Womens_Deo3.html')


def womenfragranceone(request):
    return render(request, 'v4/Womens/Subs/Womens_Fragrance1.html')


def womenfragrancetwo(request):
    return render(request, 'v4/Womens/Subs/Womens_Fragrance2.html')


def womenfragrancethree(request):
    return render(request, 'v4/Womens/Subs/Womens_Fragrance3.html')


def womenfragrancefour(request):
    return render(request, 'v4/Womens/Subs/Womens_Fragrance4.html')


def womenfragrancefive(request):
    return render(request, 'v4/Womens/Subs/Womens_Fragrance5.html')


def womenlotionone(request):
    return render(request, 'v4/Womens/Subs/Womens_Lotion1.html')


def womenlotiontwo(request):
    return render(request, 'v4/Womens/Subs/Womens_Lotion2.html')


def womenlotionthree(request):
    return render(request, 'v4/Womens/Subs/Womens_Lotion3.html')


def womenlotionfour(request):
    return render(request, 'v4/Womens/Subs/Womens_Lotion4.html')


def womenlotionfive(request):
    return render(request, 'v4/Womens/Subs/Womens_Lotion5.html')