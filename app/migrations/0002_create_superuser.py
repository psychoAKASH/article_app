# Generated by Django 5.1.7 on 2025-04-09 05:33
from django.utils import timezone

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0001_initial'),
    ]

    def create_superuser(apps, schema_editor):
        from django.contrib.auth import get_user_model
        User = get_user_model()
        if User.objects.exists():
            return
        superuser = User.objects.create_superuser(
            username="admin",  # should be fetched from env file
            email="admin@abc.com",
            password="admin@123",
            last_login=timezone.now()
        )
        superuser.save()

    operations = [
        migrations.RunPython(create_superuser)
    ]
