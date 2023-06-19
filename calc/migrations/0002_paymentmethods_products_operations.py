# Generated by Django 4.2.2 on 2023-06-19 14:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'payment_methods',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Operations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('deb_cred', models.BooleanField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('amount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('total', models.DecimalField(decimal_places=2, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('notice', models.TextField(null=True)),
                ('name_of_product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='calc.products')),
                ('payment_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='calc.paymentmethods')),
                ('stuff_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='calc.stuff')),
            ],
            options={
                'db_table': 'Operations',
            },
        ),
    ]
