# Generated by Django 3.1.4 on 2020-12-07 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20201207_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='obraz',
            field=models.ImageField(blank=True, null=True, upload_to='zjdecia'),
        ),
        migrations.AddField(
            model_name='car',
            name='opis',
            field=models.TextField(default=''),
        ),
    ]
