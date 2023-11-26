from django.utils.safestring import mark_safe
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



    # # ⭐ ★☆ 💫
    # def rating(self):
    #     if self.rating_num == 1:
    #         return '⭐'
    #     elif self.rating_num == 2:
    #         return '⭐⭐'
    #     elif self.rating_num == 3:
    #         return '⭐⭐⭐'
    #     elif self.rating_num == 4:
    #         return '⭐⭐⭐⭐'
    #     elif self.rating_num == 5:
    #         return '⭐⭐⭐⭐⭐'
    #     else:
    #         return '⭐⭐⭐⭐⭐'


