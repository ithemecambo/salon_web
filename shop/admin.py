from django.contrib import admin

from shop.forms import *
from shop.models import *


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryCreateForm
    model = Category
    list_display = [
        'id',
        'category_logo',
        'category_name',
        'status'
    ]

    list_display_links = [
        'category_logo',
        'category_name',
    ]

    list_filter = [
        'created_date',
        'status'
    ]

    search_fields = [
        'category_name',
    ]

    ordering = ['id']

    list_per_page = 10


class BusinessHourLevelInlineAdmin(admin.TabularInline):
    form = BusinessHourCreateForm
    model = BusinessHour
    extra = 0


class GalleryLevelInlineAdmin(admin.TabularInline):
    form = GalleryCreateForm
    model = Gallery
    extra = 0


class ShopServiceLevelInlineAdmin(admin.TabularInline):
    form = ShopServiceCreateForm
    model = ShopService
    extra = 0


class StaffLevelInlineAdmin(admin.StackedInline):
    form = StaffCreateForm
    model = Staff
    extra = 0


class ShopAdmin(admin.ModelAdmin):
    form = ShopCreateForm
    model = Shop
    list_display = [
        'shop_logo_photo',
        'shop_name',
        'tel',
        'email',
        'website',
    ]

    list_display_links = [
        'shop_logo_photo',
        'shop_name',
        'tel',
        'email',
    ]

    list_filter = [
        'created_date',
        'status'
    ]

    search_fields = [
        'shop_name',
        'tel',
        'email',
        'website',
        'address'
    ]

    inlines = [
        StaffLevelInlineAdmin,
        BusinessHourLevelInlineAdmin,
        ShopServiceLevelInlineAdmin,
        GalleryLevelInlineAdmin
    ]

    ordering = ['shop_name']
    list_per_page = 10


admin.site.register(Category, CategoryAdmin)
admin.site.register(Shop, ShopAdmin)
