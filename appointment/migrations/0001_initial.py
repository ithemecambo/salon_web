# Generated by Django 4.2.7 on 2023-11-27 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("shop", "0001_initial"),
        ("service", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Appointment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("status", models.BooleanField(default=True)),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                (
                    "booking_day",
                    models.CharField(max_length=10, verbose_name="Booking Day"),
                ),
                (
                    "booking_hour",
                    models.CharField(max_length=10, verbose_name="Booking Hour"),
                ),
                ("amount", models.FloatField(default=0, verbose_name="Amount")),
                (
                    "shop_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shop.shop",
                        verbose_name="Shop",
                    ),
                ),
            ],
            options={"verbose_name_plural": "Appointments",},
        ),
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("status", models.BooleanField(default=True)),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                (
                    "appointment_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="appointment.appointment",
                        verbose_name="Appointment",
                    ),
                ),
                (
                    "service_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="service.service",
                        verbose_name="Service",
                    ),
                ),
            ],
            options={"verbose_name_plural": "Bookings",},
        ),
    ]
