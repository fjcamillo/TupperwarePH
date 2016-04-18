__author__ = 'Francisc'

from django import forms
from .models import account_info


class PostForm(forms.ModelForm):


    class Meta:
        model = account_info
        fields = [
        ]