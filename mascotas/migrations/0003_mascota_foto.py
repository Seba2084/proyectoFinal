# Generated by Django 3.2.15 on 2022-09-21 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0002_auto_20220918_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='foto',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
