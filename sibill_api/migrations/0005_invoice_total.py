# Generated by Django 3.1.2 on 2020-10-07 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sibill_api', '0004_auto_20201007_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
