from django.db import models


class Contact(models.Model):
    __tablename__ = 'contact'

    adress = models.CharField(max_length=500, null=False)
    phone = models.BigIntegerField(null=False)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=False)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=False)

    def __str__(self):
        return self.adress


class Hotel(models.Model):
    __tablename__ = 'hotel'

    title = models.CharField(max_length=200, null=False)
    description = models.TextField()
    id_contacts = models.ForeignKey('main_app.Contact', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Room(models.Model):
    __tablename__ = 'room'

    uuid = models.UUIDField(primary_key=True, null=False)
    title = models.CharField(max_length=200, null=False)
    description = models.TextField()
    area = models.FloatField(null=False)
    id_hotel = models.ForeignKey('main_app.Hotel', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class RoomDetail(models.Model):
    __tablename__ = 'room_details'

    title = models.CharField(max_length=200, null=False)
    seats = models.IntegerField(null=False)
    rate = models.FloatField(null=False)
    id_room = models.ForeignKey('main_app.Room', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class PetsType(models.Model):
    __tablename__ = 'pets_type'

    pets_type = models.CharField(max_length=500, primary_key=True, null=False)

    def __str__(self):
        return self.pets_type
