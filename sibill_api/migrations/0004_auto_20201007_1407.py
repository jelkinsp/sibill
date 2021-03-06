# Generated by Django 3.1.2 on 2020-10-07 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sibill_api', '0003_auto_20201007_1253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='products',
        ),
        migrations.AddField(
            model_name='invoice',
            name='products',
            field=models.ManyToManyField(to='sibill_api.Product'),
        ),
        migrations.RemoveField(
            model_name='user',
            name='invoices',
        ),
        migrations.AddField(
            model_name='user',
            name='invoices',
            field=models.ManyToManyField(to='sibill_api.Invoice'),
        ),
    ]
