# Generated by Django 5.1.4 on 2025-03-12 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_task_unique_list_name_per_list'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='task',
            name='unique_list_name_per_list',
        ),
        migrations.AddConstraint(
            model_name='task',
            constraint=models.UniqueConstraint(fields=('name', 'its_List', 'is_checked', 'created_at'), name='unique_task_name_per_list'),
        ),
    ]
