# Generated by Django 4.2.2 on 2023-06-20 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0004_operations_notice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operations',
            name='notice',
        ),
    ]
