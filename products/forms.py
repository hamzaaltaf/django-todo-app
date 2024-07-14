from .models import Products
from django import forms

class ProductForm(forms.Form):
    title = forms.CharField(required = True)
    price = forms.DecimalField(required = True)
    summary = forms.CharField()
