# Generated by Django 4.2.7 on 2023-11-27 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Service",
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
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                (
                    "photo_url",
                    models.ImageField(
                        blank=True,
                        help_text="Allows size is 20MB",
                        null=True,
                        upload_to="services/%Y-%m-%d/",
                        verbose_name="Photo URL",
                    ),
                ),
            ],
            options={"verbose_name_plural": "Services",},
        ),
        migrations.CreateModel(
            name="Package",
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
                ("name", models.CharField(max_length=250, verbose_name="Name")),
                ("price", models.FloatField(verbose_name="Unit Price")),
                (
                    "symbol",
                    models.CharField(
                        blank=True, max_length=2, null=True, verbose_name="Symbol"
                    ),
                ),
                (
                    "photo_url",
                    models.ImageField(
                        blank=True,
                        help_text="Allow size is 20MB",
                        null=True,
                        upload_to="services/packages/%Y-%m-%d/",
                        verbose_name="Photo URL",
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
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
            options={"verbose_name_plural": "Packages",},
        ),
    ]
