from os import environ
from django.http import HttpResponse
from django.shortcuts import render
from main_app.models import Hotel

YANDEX_MAP_API_KEY = environ.get('MAP_API_KEY')


def index_page(request):
    return render(request, 'main_app/index.html', context={'yandex_map_api_key': YANDEX_MAP_API_KEY})


def hotels_page(request):
    data = {'yandex_map_api_key': YANDEX_MAP_API_KEY}

    # TODO: изменить на координаты города пользователя, когда сервис будет работать по Росссии
    #  пока заданы координаты центра Москвы latitude=37.617635, longitude=55.755814
    latitude = request.GET.get('latitude', 37.617635)
    longitude = request.GET.get('longitude', 55.755814)
    data['center_map'] = [latitude, longitude]

    data_hotels = Hotel.objects.select_related()
    if data_hotels:
        data['hotels'] = [
            {
                'title': hotel.title,
                'geo_point': [float(hotel.contact.latitude), float(hotel.contact.longitude)],
            } for hotel in data_hotels
        ]

    return render(request, 'main_app/hotels.html', context=data)


def card_hotel_page(request, hotel_id):
    data = {'yandex_map_api_key': YANDEX_MAP_API_KEY}
    try:
        hotel_data = Hotel.objects.select_related().get(id=hotel_id)
    except Exception:
        return HttpResponse(status=404)

    data.update({
        'title': hotel_data.title,
        'description': hotel_data.description,
        'address': hotel_data.contact.address,
        'latitude': float(hotel_data.contact.latitude),
        'longitude': float(hotel_data.contact.longitude),

    })

    return render(request, 'main_app/card_hotel.html', context=data)
