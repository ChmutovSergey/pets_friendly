from os import environ
from django.shortcuts import render
from main_app.models import Hotel

YANDEX_MAP_API_KEY = environ.get('MAP_API_KEY')


def index_page(request):
    data = {'yandex_map_api_key': YANDEX_MAP_API_KEY}

    return render(request, 'main_app/index.html', context=data)


def hotels_page(request):
    data = {'yandex_map_api_key': YANDEX_MAP_API_KEY}

    # latitude = request.GET.get('latitude')
    # longitude = request.GET.get('longitude')

    data_hotels = Hotel.objects.select_related()

    if data_hotels:
        data["hotels"] = [
            {
                'title': hotel.title,
                'latitude': hotel.contact.latitude,
                'longitude': hotel.contact.longitude
            } for hotel in data_hotels
        ]

    return render(request, 'main_app/hotels.html', context=data)
