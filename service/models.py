from django.utils.safestring import mark_safe

from account.models import *
from shop.models import *


# TODO: Create service provide to shop
class Service(BaseModel):
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Name')
    photo_url = models.ImageField(upload_to='services/%Y-%m-%d/', verbose_name='Photo URL',
                                  help_text='Allows size is 20MB', blank=False, null=False)

    class Meta:
        verbose_name_plural = 'Services'

    def __str__(self):
        return f'{self.name}'

    def service_photo(self):
        if self.photo_url:
            return mark_safe('<img src="%s" style="width: auto; height:55px;" />' % self.photo_url.url)
        else:
            return '__'
        service_photo.short_description = 'Photo'


class Package(BaseModel):
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service',
                                   verbose_name='Service')
    name = models.CharField(max_length=250, blank=True, null=True, verbose_name='Name')
    price = models.FloatField(blank=True, null=True, verbose_name='Unit Price')
    symbol = models.CharField(max_length=2, blank=False, null=False, verbose_name='Symbol')
    photo_url = models.ImageField(upload_to='services/packages/%Y-%m-%d/', verbose_name='Photo URL',
                                  blank=False, null=False, help_text='Allow size is 20MB')
    description = models.TextField(blank=False, null=False, verbose_name='Description')

    class Meta:
        verbose_name_plural = 'Packages'

    def __str__(self):
        return f'{self.name}'
    def package_photo(self):
        if self.photo_url:
            return mark_safe('<img src"%s style="width: auto; height:55px; />' % self.photo_url)
        else:
            return '__'
    package_photo.short_description = 'Photo'


class Shop(BaseModel):
    user_id = models.ForeignKey(Account, related_name='user', on_delete=models.CASCADE,
                                verbose_name='User')
    category_id = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE,
                                verbose_name='Category')
    shop_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Shop Name')
    website = models.CharField(max_length=100, blank=False, null=False, verbose_name='Website')
    tel = models.CharField(max_length=20, blank=True, null=True, verbose_name='Tel')
    fax = models.CharField(max_length=20, blank=False, null=False, verbose_name='Fax')
    email = models.CharField(max_length=100, blank=True, null=True, verbose_name='Email')
    twitter = models.CharField(max_length=120, blank=True, null=True, verbose_name='Twitter')
    facebook = models.CharField(max_length=120, blank=True, null=True, verbose_name='Facebook')
    linkedin = models.CharField(max_length=120, blank=True, null=True, verbose_name='LinkedIn')
    instagram = models.CharField(max_length=120, blank=True, null=True, verbose_name='Instagram')
    address = models.CharField(max_length=250, blank=True, null=True, verbose_name='Address')
    latitude = models.FloatField(blank=True, null=True, verbose_name='Latitude')
    longitude = models.FloatField(blank=True, null=True, verbose_name='Longitude')
    banner_url = models.ImageField(upload_to='shops/banners/%Y-%m-%d/', verbose_name='Banner URL',
                                   blank=False, null=False, help_text='Allow size is 10MB')
    logo_url = models.ImageField(upload_to='shops/logos/%Y-%m-%d/', verbose_name='Logo URL',
                                 blank=False, null=False, help_text='Allow size is 5MB')
    about = models.TextField(blank=False, null=False, verbose_name='About')

    class Meta:
        verbose_name_plural = 'Shops'

    def __str__(self):
        return f'{self.shop_name}'

    def shop_banner_photo(self):
        if self.banner_url:
            return mark_safe('<img src"%s" style="width: auto; height: 55px;" />' % self.banner_url)
        else:
            return '__'
    shop_banner_photo.short_description = 'Banner'

    def shop_logo_photo(self):
        if self.logo_url:
            return mark_safe('<img src"%s" style="width: auto; height: 55px;" />' % self.logo_url)
        else:
            return '__'
    shop_logo_photo.short_description = 'Logo'


class ShopService(BaseModel):
    shop_id = models.ForeignKey(Shop, related_name='shop', on_delete=models.CASCADE,
                                verbose_name='Shop')
    service_id = models.ManyToManyField(Service, related_name='service', verbose_name='Service')

    class Meta:
        verbose_name_plural = 'ShopServices'

    def __str__(self):
        return f'{self.shop_id.name} ~ {self.service_id.name}'


class Gallery(BaseModel):
    shop_id = models.ForeignKey(Shop, related_name='shop', on_delete=models.CASCADE, verbose_name='Shop')
    photo_url = models.ImageField(upload_to='services/galleries/%Y-%m-%d/', verbose_name='Photo',
                                  blank=False, null=False, help_text='Allow size is 20MB')

    class Meta:
        verbose_name_plural = 'Galleries'

    def __str__(self):
        return f'{self.shop_id.name}'

    def gallery_photo(self):
        if self.photo_url:
            return mark_safe('<img src="%s" style="width: auto; height: 55px;" />' % self.photo_url)
        else:
            return '__'
    gallery_photo.short_description = 'Album'


