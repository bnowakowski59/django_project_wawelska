# Generated by Django 3.1.4 on 2021-01-19 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_car_obslugaokresowakm'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='przegladTechniczny',
            field=models.DateField(default='2000-01-01'),
        ),
    ]
