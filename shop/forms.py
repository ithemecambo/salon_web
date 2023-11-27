from django import forms
from shop.models import *


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'category_name',
            'font_awesome',
            'logo_url',
            'status'
        ]

    # def clean_category_name(self):
    #     category_name = self.cleaned_data.get('category_name')
    #     if not category_name:
    #         raise forms.ValidationError('This field is required.')
    #     for category in Category.objects.all():
    #         if category.category_name == category_name:
    #             raise forms.ValidationError(category_name + ' is already created')
    #     return category_name


class CategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'category_name',
            'font_awesome',
            'logo_url',
            'status'
        ]


class ShopCreateForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = [
            'user_id',
            'category_id',
            'shop_name',
            'website',
            'tel',
            'fax',
            'email',
            'twitter',
            'facebook',
            'linkedin',
            'instagram',
            'address',
            'latitude',
            'longitude',
            'banner_url',
            'logo_url',
            'about',
            'status'
        ]


class BusinessHourCreateForm(forms.ModelForm):
    class Meta:
        model = BusinessHour
        fields = ['day', 'hour']


class ShopServiceCreateForm(forms.ModelForm):
    class Meta:
        model = ShopService
        fields = ['service_id']


class GalleryCreateForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['photo_url']


class StaffCreateForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['first_name', 'last_name', 'nickname', 'tel', 'email', 'ssn', 'photo_url']

