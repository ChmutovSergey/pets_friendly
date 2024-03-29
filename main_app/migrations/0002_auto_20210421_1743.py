# Generated by Django 3.1.7 on 2021-04-21 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='address',
            field=models.CharField(max_length=500, verbose_name='Адрес отеля'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='description',
            field=models.TextField(verbose_name='Описание отеля'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='mass_transport_route',
            field=models.TextField(blank=True, verbose_name='Как добраться на общественном транспорте'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='metro',
            field=models.ManyToManyField(blank=True, to='main_app.Metro'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='person_car_route',
            field=models.TextField(blank=True, verbose_name='Как добраться на личном автомобиле'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='phone',
            field=models.BigIntegerField(verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название отеля'),
        ),
        migrations.AlterField(
            model_name='metro',
            name='station',
            field=models.CharField(max_length=100, verbose_name='Станция метро'),
        ),
    ]
