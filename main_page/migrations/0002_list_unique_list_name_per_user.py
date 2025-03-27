# Generated by Django 5.1.4 on 2025-03-09 10:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='list',
            constraint=models.UniqueConstraint(fields=('name', 'its_User'), name='unique_list_name_per_user'),
        ),
    ]
