from django.db import models


class MetroLine(models.Model):
    metro_line = models.CharField(max_length=100, verbose_name='Линия метро')
    img_url = models.TextField(verbose_name='Путь до иконки линии')

    def __str__(self):
        return self.metro_line


class Metro(models.Model):
    station = models.CharField(max_length=100, verbose_name='Станция метро')
    metro_line = models.ManyToManyField(MetroLine)

    def __str__(self):
        return self.station


class Hotel(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название отеля')
    description = models.TextField(verbose_name='Описание отеля')
    short_description = models.TextField(max_length=500, blank=True, verbose_name='Короткое описание отеля')
    address = models.CharField(max_length=500, verbose_name='Адрес отеля')
    phone = models.BigIntegerField(verbose_name='Номер телефона')
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='Долгота')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='Широта')
    opening_time = models.TimeField(verbose_name='Время открытия')
    closing_time = models.TimeField(verbose_name='Время закрытия')
    mass_transport_route = models.TextField(blank=True, verbose_name='Как добраться на общественном транспорте')
    person_car_route = models.TextField(blank=True, verbose_name='Как добраться на личном автомобиле')
    metro = models.ManyToManyField(Metro, blank=True)

    def __str__(self):
        return self.title


class HotelGallery(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.PROTECT)
    photo_route = models.CharField(max_length=1000, null=False, verbose_name='Путь до фотографии')

    def __str__(self):
        return self.photo_route
