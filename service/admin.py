from django.contrib import admin
from service.forms import *
from service.models import *


class PackageLevelAdmin(admin.StackedInline):
    form = PackageCreateForm
    model = Package
    extra = 0


class ServiceAdmin(admin.ModelAdmin):
    form = ServiceCreateForm
    model = Service
    list_display = ['service_photo', 'name', 'status']
    list_display_links = ['service_photo', 'name']
    list_filter = ['created_date', 'status']
    search_fields = ['name']
    ordering = ['id']
    list_per_page = 10
    inlines = [PackageLevelAdmin]
    save_on_top = True


admin.site.register(Service, ServiceAdmin)
