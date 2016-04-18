from django.contrib import admin
from cart.models import onClickCart
# Register your models here.


class cartmodel(admin.ModelAdmin):
    list_display = ['product_cart_title', 'product_cart_image', 'product_cart_price', 'id']

    class Meta:
        model = onClickCart


admin.site.register(onClickCart, cartmodel)