# Generated by Django 4.1 on 2022-08-30 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos_app', '0003_albumvideos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='categorias',
            field=models.ManyToManyField(related_name='álbumdefotos', to='recursos_app.albumfotos'),
        ),
    ]
