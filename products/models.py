from django.db import models

# Create your models here.


class specific_products(models.Model):
    product_name = models.CharField(max_length=50)
    product_description = models.TextField()
    product_image = models.FileField(null=True, blank=True)
    product_category = models.CharField(max_length=30, null=True, blank=True)
    product_price = models.FloatField(max_length=10, null=True, blank=True)
    product_promo = models.FloatField(max_length=10, null=True, blank=True)
    product_stock = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.product_name