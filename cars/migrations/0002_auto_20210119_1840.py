# Generated by Django 3.1.4 on 2021-01-19 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='obslugaOkresowaData',
        ),
        migrations.RemoveField(
            model_name='car',
            name='obslugaOkresowaKM',
        ),
        migrations.RemoveField(
            model_name='car',
            name='przegladTechniczny',
        ),
        migrations.RemoveField(
            model_name='car',
            name='rocznikOponLetnich',
        ),
        migrations.RemoveField(
            model_name='car',
            name='rocznikOponZimowych',
        ),
        migrations.RemoveField(
            model_name='car',
            name='rozmiarOpon',
        ),
    ]