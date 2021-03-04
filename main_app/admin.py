from django.contrib import admin
from .models import Contact, Hotel, Room, RoomDetail, PetsType


admin.site.register(Contact)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(RoomDetail)
admin.site.register(PetsType)
