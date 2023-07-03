from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    name = forms.CharField(label="Имя")
    class Meta:
        model = Products
        fields = ['name']


class StuffForm(forms.ModelForm):
    name = forms.CharField(label="Имя")
    status = forms.BooleanField(label='Активный')
    class Meta:
        model = Stuff
        fields = '__all__'