from django import forms
from service.models import *


class ServiceCreateForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'photo_url', 'status']


class PackageCreateForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['name', 'price', 'symbol', 'photo_url', 'status', 'description']
