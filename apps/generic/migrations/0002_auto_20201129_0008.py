# Generated by Django 3.1.3 on 2020-11-29 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priceusd',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creado el'),
        ),
    ]
