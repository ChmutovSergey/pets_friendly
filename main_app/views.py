from os import environ
from django.http import HttpResponse
from django.shortcuts import render
from main_app.models import Hotel, Room

YANDEX_MAP_API_KEY = environ.get('MAP_API_KEY')


def index_page(request):
    return render(request, 'main_app/index.html', context={'yandex_map_api_key': YANDEX_MAP_API_KEY})


def hotels_page(request):
    data = {'yandex_map_api_key': YANDEX_MAP_API_KEY}
    # latitude = request.GET.get('latitude')
    # longitude = request.GET.get('longitude')

    data_hotels = Hotel.objects.select_related()

    if data_hotels:
        data['hotels'] = [
            {
                'title': hotel.title,
                'latitude': float(hotel.contact.latitude),
                'longitude': float(hotel.contact.longitude)
            } for hotel in data_hotels
        ]

    return render(request, 'main_app/hotels.html', context=data)


def card_hotel_page(request, hotel_id):
    data = {'yandex_map_api_key': YANDEX_MAP_API_KEY}
    try:
        room_data = Room.objects.select_related().filter(hotel_id=hotel_id)
        hotel_data = Hotel.objects.select_related().get(id=hotel_id)
    except Exception:
        return HttpResponse(status=404)

    rooms = [
        {
            'title': room.title,
            'description': room.description,
            'area': room.area,
            'seats': room.room_detail.seats,
            'rate': room.room_detail.rate,
        } for room in room_data]

    data.update({
        'title': hotel_data.title,
        'description': hotel_data.description,
        'address': hotel_data.contact.address,
        'latitude': float(hotel_data.contact.latitude),
        'longitude': float(hotel_data.contact.longitude),
        'rooms': rooms,

    })
    print(data)

    return render(request, 'main_app/card_hotel.html', context=data)
