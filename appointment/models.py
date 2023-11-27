from django.db import models
from shop.models import *


class BaseModel(models.Model):
    status = models.BooleanField(default=True, blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Appointment(BaseModel):
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE, verbose_name='Shop')
    booking_day = models.CharField(max_length=10, blank=False, null=False, verbose_name='Booking Day')
    booking_hour = models.CharField(max_length=10, blank=False, null=False, verbose_name='Booking Hour')
    amount = models.FloatField(blank=False, null=False, verbose_name='Amount', default=0)

    class Meta:
        verbose_name_plural = 'Appointments'

    def __str__(self):
        return f'{self.shop_id.name}'


class Booking(BaseModel):
    appointment_id = models.ForeignKey(Appointment, on_delete=models.CASCADE,
                                       verbose_name='Appointment')
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE,
                                   verbose_name='Service')
    
    class Meta:
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return f'{self.appointment_id.booking_day}, {self.service_id.name}'
