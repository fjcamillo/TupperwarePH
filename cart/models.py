from django.db import models

# Create your models here.


class onClickCart(models.Model):
    product_cart_title = models.CharField(max_length=150, default='ProductName')
    product_cart_image = models.FileField(null=True, blank=True)
    product_cart_price = models.FloatField(null=True, blank=True)


    def __str__(self):
        return self.product_cart_title


