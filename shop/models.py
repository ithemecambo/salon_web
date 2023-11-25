from django.db import models

class BaseModel(models.Model):
    status = models.BooleanField(default=True, blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    category_name = models.CharField(max_length=100, verbose_name='Category Name')
    font_awesome = models.CharField(max_length=50, blank=True, null=True, verbose_name='Font Awesome')
    logo_url = models.ImageField(upload_to='categories/', blank=True, null=True, verbose_name='Icon',
                                 help_text='Allowed size is 5MB')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.category_name}'

