from django.contrib import admin
from products.models import specific_products
# Register your models here.


class SpecificProductModel(admin.ModelAdmin):
    list_display = ['product_name', 'product_category', 'id', 'product_price', 'product_image']
    list_filter = ['product_category', 'product_price']
    search_fields = ['product_name', 'product_category', 'product_price', 'id']

    class Meta:
        model = specific_products





admin.site.register(specific_products, SpecificProductModel)
