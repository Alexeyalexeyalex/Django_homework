from django import forms
from .models import Product



class ProductForm(forms.Form):

    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    price = forms.IntegerField()
    quantity = forms.IntegerField()
    product_registration_date = forms.DateField()
    image = forms.ImageField()




