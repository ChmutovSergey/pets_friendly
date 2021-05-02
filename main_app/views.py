from django.shortcuts import render
from os import environ

from main_app.base_logger import logger
from main_app.controllers.help import send_mail
from main_app.controllers.hotels import get_hotels_list


YANDEX_MAP_API_KEY = environ.get('MAP_API_KEY')


def index_page(request):
    return render(request, 'main_app/index.html', context={'yandex_map_api_key': YANDEX_MAP_API_KEY})


def hotels_page(request):
    # TODO: изменить на координаты города пользователя, когда сервис будет работать по Росссии
    #  пока заданы координаты центра Москвы latitude=37.617635, longitude=55.755814
    base_point = (
        float(request.GET.get('latitude', 55.755814)),
        float(request.GET.get('longitude', 37.617635)),
    )
    data = {
        'yandex_map_api_key': YANDEX_MAP_API_KEY,
        'center_map': base_point,
        'hotels': get_hotels_list(base_point),
    }

    return render(request, 'main_app/hotels.html', context=data)


def help_page(request):
    if not request.GET:
        return render(request, 'main_app/help.html')

    name, email, message = request.GET.get('name'), request.GET.get('email'), request.GET.get('msg')
    send_message_status = send_mail(name, email, message)
    if not send_message_status:
        logger.warning('Send mail fail')
    logger.info('Send mail success')

    return render(request, 'main_app/help.html')


def privacy_page(request):
    return render(request, 'main_app/privacy.html')
