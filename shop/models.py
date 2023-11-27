from django.db import models
from django.utils.safestring import mark_safe

from account.models import Account
from service.models import Service


class BaseModel(models.Model):
    status = models.BooleanField(default=True, blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    category_name = models.CharField(max_length=100, blank=False, null=False, verbose_name='Category Name')
    font_awesome = models.CharField(max_length=50, blank=True, null=True, verbose_name='Font Awesome')
    logo_url = models.ImageField(upload_to='categories/', blank=True, null=True, verbose_name='Icon',
                                 help_text='Allowed size is 5MB')

    class Meta:
        verbose_name_plural = 'Categories'
        # ordering = ('id',)

    def __str__(self):
        return f'{self.category_name}'

    def category_logo(self):
        if self.logo_url:
            return mark_safe('<img src="%s" style="width: 25px; height: 25px;"/>' % self.logo_url.url)
        else:
            return '__'
    category_logo.short_description = 'Logo'


class Shop(BaseModel):
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE,
                                verbose_name='User')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE,
                                verbose_name='Category')
    shop_name = models.CharField(max_length=100, blank=False, null=False, verbose_name='Shop Name')
    tel = models.CharField(max_length=20, blank=False, null=False, verbose_name='Tel')
    fax = models.CharField(max_length=20, blank=False, null=False, verbose_name='Fax')
    email = models.EmailField(max_length=100, blank=False, null=False, verbose_name='Email')
    website = models.CharField(max_length=100, blank=True, null=True, verbose_name='Website')
    twitter = models.CharField(max_length=120, blank=True, null=True, verbose_name='Twitter')
    facebook = models.CharField(max_length=120, blank=True, null=True, verbose_name='Facebook')
    linkedin = models.CharField(max_length=120, blank=True, null=True, verbose_name='LinkedIn')
    instagram = models.CharField(max_length=120, blank=True, null=True, verbose_name='Instagram')
    address = models.CharField(max_length=250, blank=False, null=False, verbose_name='Address')
    latitude = models.FloatField(blank=False, null=False, verbose_name='Latitude', default=0)
    longitude = models.FloatField(blank=False, null=False, verbose_name='Longitude', default=0)
    banner_url = models.ImageField(upload_to='shops/banners/%Y-%m-%d/', verbose_name='Banner URL',
                                   blank=True, null=True, help_text='Allow size is 10MB')
    logo_url = models.ImageField(upload_to='shops/logos/%Y-%m-%d/', verbose_name='Logo URL',
                                 blank=True, null=True, help_text='Allow size is 5MB')
    about = models.TextField(blank=True, null=True, verbose_name='About')

    class Meta:
        verbose_name_plural = 'Shops'

    def __str__(self):
        return f'{self.shop_name}'

    def shop_banner_photo(self):
        if self.banner_url:
            return mark_safe('<img src="%s" style="width: auto; height: 55px;" />' % self.banner_url.url)
        else:
            return '__'
    shop_banner_photo.short_description = 'Banner'

    def shop_logo_photo(self):
        if self.logo_url:
            return mark_safe('<img src="%s" style="width: auto; height: 55px;" />' % self.logo_url.url)
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
        return f'{self.shop_id} ~ {self.service_id}'


class Gallery(BaseModel):
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE, verbose_name='Shop')
    photo_url = models.ImageField(upload_to='shops/galleries/%Y-%m-%d/', verbose_name='Photo',
                                  blank=True, null=True, help_text='Allow size is 20MB')

    class Meta:
        verbose_name_plural = 'Galleries'

    def __str__(self):
        return f'{self.shop_id}'

    def gallery_photo(self):
        if self.photo_url:
            return mark_safe('<img src="%s" style="width: auto; height: 55px;" />' % self.photo_url.url)
        else:
            return '__'
    gallery_photo.short_description = 'Album'


class BusinessHour(BaseModel):
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE, verbose_name='Shop')
    day = models.CharField(max_length=25, blank=False, null=False, verbose_name='Day')
    hour = models.CharField(max_length=25, blank=False, null=False, verbose_name='Hour')

    class Meta:
        verbose_name_plural = 'BusinessHours'

    def __str__(self):
        return f'{self.shop_id}'


class Staff(BaseModel):
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE, verbose_name='Shop')
    first_name = models.CharField(max_length=25, blank=True, null=True, verbose_name='First Name')
    last_name = models.CharField(max_length=25, blank=True, null=True, verbose_name='Last Name')
    nickname = models.CharField(max_length=25, blank=False, null=False, verbose_name='Nickname', default='')
    tel = models.CharField(max_length=20, blank=True, null=True, verbose_name='Tel')
    email = models.EmailField(max_length=100, blank=True, null=True, verbose_name='Email')
    ssn = models.CharField(max_length=15, blank=False, null=False, verbose_name='Social Security Number')
    photo_url = models.ImageField(upload_to='avatars/staffs/%Y-%m-%d/', verbose_name='Photo URL',
                                  blank=True, null=True, help_text='Allow size is 10MB')

    class Meta:
        verbose_name_plural = 'Staffs'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def profile(self):
        if self.photo_url:
            return mark_safe('<img src="%s" style="width: auto; height: 55px;" />' % self.photo_url.url)
        else:
            return '__'
    profile.short_description = 'Profile'

