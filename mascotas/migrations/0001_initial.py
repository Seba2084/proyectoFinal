# Generated by Django 3.2.15 on 2022-09-18 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especie', models.CharField(max_length=20)),
                ('raza', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=30)),
                ('sexo', models.CharField(choices=[('M', 'M'), ('H', 'H')], default='H', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='particularidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_mascota', models.CharField(max_length=10)),
                ('señas_particulares', models.CharField(max_length=100)),
                ('edad', models.CharField(choices=[('C', 'C'), ('A', 'A'), ('V', 'V')], default=None, max_length=2)),
            ],
        ),
    ]
