# Generated by Django 2.2.3 on 2019-07-03 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20190702_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentbook',
            name='date_devolution',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='rentbook',
            name='delivery_date_forecast',
            field=models.DateField(),
        ),
    ]
