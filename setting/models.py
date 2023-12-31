from django.db import models
from django.utils.safestring import mark_safe

from service.models import Service
from shop.models import Shop

DEVICE_CHOICES = (
    ('All', 'All'),
    ('Web', 'Web'),
    ('iOS', 'iOS'),
    ('Android', 'Android')
)


class BaseModel(models.Model):
    status = models.BooleanField(default=True, blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


# TODO: Auto register when application is started open in the first installation
class Platform(BaseModel):
    platform_name = models.CharField(choices=DEVICE_CHOICES, max_length=15, default='All',
                                     verbose_name='Platform Name')
    ip = models.CharField(max_length=20, blank=False, null=False, verbose_name='IP Address')
    device = models.CharField(max_length=20, blank=False, null=False, verbose_name='Device')
    uuid = models.CharField(max_length=250, blank=False, null=False, verbose_name='UUID')

    class Meta:
        verbose_name_plural = 'Platforms'

    def __str__(self):
        return f'{self.platform_name}'


# # TODO: Send broadcast ads specific our customers
class Notification(BaseModel):
    platform_id = models.ForeignKey(Platform, on_delete=models.CASCADE, verbose_name='Platform')
    title = models.CharField(max_length=100, verbose_name='Title')
    subtitle = models.CharField(max_length=250, verbose_name='Sub Title')
    photo_url = models.ImageField(upload_to='notifications/%Y-%m-%d/', verbose_name='Photo URL',
                                  help_text='Allowed size is 20MB', blank=False, null=False)
    message = models.TextField(blank=True, null=True, verbose_name='Message')

    class Meta:
        verbose_name_plural = 'Notifications'

    def __str__(self):
        return f'{self.title}'

    def banner_notification_photo(self):
        if self.photo_url:
            return mark_safe('<img src="%s" style="width: auto; height:55px;" />' % self.photo_url.url)
        else:
            return '__'
    banner_notification_photo.short_description = 'Banner'


class Promotion(BaseModel):
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE, verbose_name='Shop')
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Service')
    title = models.CharField(max_length=100, blank=False, null=False, verbose_name='Title')
    subtitle = models.CharField(max_length=250, blank=False, null=False, verbose_name='SubTitle')
    color = models.CharField(max_length=10, blank=False, null=False, verbose_name='Color', 
                             help_text='Hex Color [Ex: #C3C3C3]', default='#')
    photo_url = models.ImageField(upload_to='settings/promotions/%Y-%m-%d/', verbose_name='Photo URL',
                                  blank=False, null=False, help_text='Allow size is 10MB')
    description = models.TextField(blank=True, null=True, verbose_name='Description')

    class Meta:
        verbose_name_plural = 'Promotions'

    def __str__(self):
        return f'{self.title}'

    def banner_promotion_photo(self):
        if self.photo_url:
            return mark_safe('<img src="%s" style="width: auto; height: 55px;" />' % self.photo_url.url)
        else:
            return '__'
    banner_promotion_photo.short_description = 'Banner'


