__author__ = 'Francisc'

from django import forms
from cart.models import onClickCart


class PostForm(forms.ModelForm):


    class Meta:
        model = onClickCart
        fields = [
        ]