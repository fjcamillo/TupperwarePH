from django.db import models

# Create your models here.


class account_info(models.Model):
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
