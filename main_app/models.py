from django.db import models


class Metro(models.Model):
    station = models.CharField(max_length=100, null=False, verbose_name='Станция метро')

    def __str__(self):
        return self.station


class Hotel(models.Model):
    title = models.CharField(max_length=200, null=False, verbose_name='Название отеля')
    description = models.TextField(null=False, verbose_name='Описание отеля')
    address = models.CharField(max_length=500, null=False, verbose_name='Адрес отеля')
    phone = models.BigIntegerField(null=False, verbose_name='Номер телефона')
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=False, verbose_name='Долгота')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=False, verbose_name='Широта')
    opening_time = models.TimeField(null=True, verbose_name='Время открытия')
    closing_time = models.TimeField(null=True, verbose_name='Время закрытия')
    mass_transport_route = models.TextField(null=True, verbose_name='Как добраться на общественном транспорте')
    person_car_route = models.TextField(null=True, verbose_name='Как добраться на личном автомобиле')
    metro = models.ManyToManyField(Metro)

    def __str__(self):
        return self.title


class HotelGallery(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.PROTECT)
    photo_route = models.CharField(max_length=1000, null=False, verbose_name='Путь до фотографии')

    def __str__(self):
        return self.photo_route
