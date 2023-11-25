# Generated by Django 4.2.7 on 2023-11-25 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                    "category_name",
                    models.CharField(max_length=100, verbose_name="Category Name"),
                ),
                (
                    "font_awesome",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Font Awesome",
                    ),
                ),
                (
                    "logo_url",
                    models.ImageField(
                        blank=True,
                        help_text="Allowed size is 5MB",
                        null=True,
                        upload_to="categories/",
                        verbose_name="Icon",
                    ),
                ),
            ],
            options={"verbose_name_plural": "Categories",},
        ),
    ]
