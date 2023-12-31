# Generated by Django 4.2.2 on 2023-06-20 13:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0006_rename_name_of_product_id_operations_name_of_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operations',
            name='date',
        ),
        migrations.RemoveField(
            model_name='operations',
            name='name_of_product',
        ),
        migrations.RemoveField(
            model_name='operations',
            name='notice',
        ),
        migrations.RemoveField(
            model_name='operations',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='operations',
            name='stuff',
        ),
        migrations.RemoveField(
            model_name='operations',
            name='total',
        ),
        migrations.AddField(
            model_name='operations',
            name='fk_name_of_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='calc.products'),
        ),
        migrations.AlterModelTable(
            name='operations',
            table='operations',
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sell_id', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('notice', models.TextField(null=True)),
                ('fk_payment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='calc.paymentmethods')),
                ('fk_stuff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='calc.stuff')),
            ],
            options={
                'db_table': 'sales',
            },
        ),
    ]
