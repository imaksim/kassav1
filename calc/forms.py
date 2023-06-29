from django import forms
from .models import Products


class ProductForm(forms.ModelForm):
    name = forms.CharField(label="Имя")
    class Meta:
        model = Products
        fields = ['name']
