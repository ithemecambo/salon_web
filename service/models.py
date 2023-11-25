from django.db import models
from django.utils.safestring import mark_safe

from shop.models import *


# TODO: Create service provide to shop
class Service(BaseModel):
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Name')
    photo_url = models.ImageField(upload_to='services//%Y-%m-%d/', verbose_name='Photo URL',
                                  help_text='Allows size is 20MB', blank=False, null=False)


    class Meta:
        verbose_name_plural = 'Services'


    def __str__(self):
        return f'{self.name}'

    def photo(self):
        if self.photo_url:
            return mark_safe('<img src="%s" style="width: auto; height:55px;" />' % self.photo_url.url)
        else:
            return '__'
        photo.short_description = 'Photo'

