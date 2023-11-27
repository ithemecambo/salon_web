# Generated by Django 4.2.7 on 2023-11-27 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Account",
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
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        max_length=30, null=True, verbose_name="First Name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        max_length=30, null=True, verbose_name="Last Name"
                    ),
                ),
                (
                    "sex",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female")],
                        default="Male",
                        max_length=10,
                        verbose_name="Sex",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="Email"
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="Password")),
                ("phone", models.CharField(max_length=15, verbose_name="Phone")),
                (
                    "fax",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="Fax"
                    ),
                ),
                (
                    "photo_url",
                    models.ImageField(
                        blank=True,
                        help_text="Allowed size is 100MB",
                        null=True,
                        upload_to="avatars/%Y-%m-%d/",
                        verbose_name="Photo",
                    ),
                ),
                ("address", models.CharField(max_length=250, verbose_name="Address")),
                (
                    "date_joined",
                    models.DateTimeField(auto_now_add=True, verbose_name="Date Joined"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Created Date"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="Updated Date"
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={"verbose_name": "Account", "verbose_name_plural": "Accounts",},
        ),
    ]
