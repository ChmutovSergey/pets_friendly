from django.db import models


class Contact(models.Model):
    address = models.CharField(max_length=500, null=False, verbose_name='Адрес')
    phone = models.BigIntegerField(null=False, verbose_name='Номер телефона')
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=False, verbose_name='Долготоа')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=False, verbose_name='Широта')

    def __str__(self):
        return self.address


class Hotel(models.Model):
    title = models.CharField(max_length=200, null=False, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    contact = models.ForeignKey('main_app.Contact', on_delete=models.CASCADE, verbose_name='Контакты')

    def __str__(self):
        return self.title


class Room(models.Model):
    title = models.CharField(max_length=200, null=False, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    area = models.FloatField(null=False, verbose_name='Площадь')
    hotel = models.ForeignKey('main_app.Hotel', on_delete=models.PROTECT, verbose_name='Отель')
    room_detail = models.ForeignKey('main_app.RoomDetail', on_delete=models.PROTECT, verbose_name='Номер')

    def __str__(self):
        return self.title


class RoomDetail(models.Model):
    title = models.CharField(max_length=200, null=False, verbose_name='Наименование')
    seats = models.IntegerField(null=False, verbose_name='Количество мест')
    rate = models.FloatField(null=False, verbose_name='Цена')

    def __str__(self):
        return self.title


class PetsType(models.Model):
    pets_type = models.CharField(max_length=500, primary_key=True, null=False, verbose_name='Вид животного')

    def __str__(self):
        return self.pets_type
