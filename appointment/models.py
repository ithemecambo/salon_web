from shop.models import *


class Appointment(BaseModel):
    shop_id = models.ForeignKey(Shop, related_name='shop', on_delete=models.CASCADE, verbose_name='Shop')
    booking_day = models.CharField(max_length=10, blank=True, null=True, verbose_name='Booking Day')
    booking_hour = models.CharField(max_length=10, blank=True, null=True, verbose_name='Booking Hour')
    amount = models.FloatField(blank=True, null=True, verbose_name='Amount')

    class Meta:
        verbose_name_plural = 'Appointments'

    def __str__(self):
        return f'{self.shop_id.name}'


class Booking(BaseModel):
    appointment_id = models.ForeignKey(Appointment, related_name='appointment', on_delete=models.CASCADE, 
                                       verbose_name='Appointment')
    service_id = models.ForeignKey(Service, related_name='service', on_delete=models.CASCADE, 
                                   verbose_name='Service')
    
    class Meta:
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return f'{self.appointment_id.booking_day}, {self.service_id.name}'
