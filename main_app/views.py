from math import sqrt

from django.shortcuts import render
from main_app.models import Hotel
from .controller import YANDEX_MAP_API_KEY, format_phone_number, get_work_time


def index_page(request):
    return render(request, 'main_app/index.html', context={'yandex_map_api_key': YANDEX_MAP_API_KEY})


def hotels_page(request):
    # TODO: изменить на координаты города пользователя, когда сервис будет работать по Росссии
    #  пока заданы координаты центра Москвы latitude=37.617635, longitude=55.755814
    base_point = (
        float(request.GET.get('latitude', 55.755814)),
        float(request.GET.get('longitude', 37.617635))
    )
    data = {
        'yandex_map_api_key': YANDEX_MAP_API_KEY,
        'center_map': base_point,
        'hotels': [],
    }

    hotels = Hotel.objects.select_related()
    if hotels:
        data_hotels = [
            {
                'title': hotel.title,
                'address': hotel.address,
                'short_description': hotel.short_description,
                'phone': format_phone_number(hotel.phone),
                'work_time': get_work_time(hotel.opening_time, hotel.closing_time),
                'geo_point': (float(hotel.latitude), float(hotel.longitude)),
            } for hotel in hotels
        ]
        # сортируем объекты по расстоянию от центра карты
        data_hotels.sort(key=lambda hotel: sqrt(
            (hotel['geo_point'][0] - base_point[0]) ** 2 + (hotel['geo_point'][1] - base_point[1]) ** 2
        ))
        data['hotels'].extend(data_hotels)

    return render(request, 'main_app/hotels.html', context=data)


def help_page(request):
    return render(request, 'main_app/help.html')


def privacy_page(request):
    return render(request, 'main_app/privacy.html')


# def card_hotel_page(request, hotel_id):
#     data = {'yandex_map_api_key': YANDEX_MAP_API_KEY}
#     try:
#         hotel = Hotel.objects.select_related().get(id=hotel_id)
#     except Exception:
#         return HttpResponse(status=404)
#
#     data.update({
#         'title': hotel.title,
#         'description': hotel.description,
#         'address': hotel.address,
#         'latitude': float(hotel.latitude),
#         'longitude': float(hotel.longitude),
#
#     })
#
#     return render(request, 'main_app/card_hotel.html', context=data)
