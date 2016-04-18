from django.contrib import admin
from .models import account_info
# Register your models here.


class display_account(admin.ModelAdmin):
    list_display = ['name', 'address', 'email', 'id', 'contact']

    class Meta:
        model = account_info



admin.site.register(account_info, display_account)