from django.db import models
from django.utils.safestring import mark_safe

from shop.models import *

DEVICE_CHOICES = (
    ('All', 'All'),
    ('Web', 'Web'),
    ('iOS', 'iOS'),
    ('Android', 'Android')
)


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
# class Notification(BaseModel):
#     platform_id = models.ForeignKey(Platform, on_delete=models.CASCADE, verbose_name='Platform')
#     title = models.CharField(max_length=100, verbose_name='Title')
#     subtitle = models.CharField(max_length=250, verbose_name='Sub Title')
#     photo_url = models.ImageField(upload_to='notifications/%Y-%m-%d/', verbose_name='Photo URL',
#                                   help_text='Allowed size is 20MB', blank=False, null=False)
#     message = models.TextField(verbose_name='Message')
#
#     class Meta:
#         verbose_name_plural = 'Notifications'
#
#     def __str__(self):
#         return f'{self.title}'
#
#     def profile(self):
#         if self.photo_url:
#             return mark_safe('<img src="%s" style="width: auto; height:55px;" />' % self.photo_url.url)
#         else:
#             return '__'
#     profile.short_description = 'Profile'

