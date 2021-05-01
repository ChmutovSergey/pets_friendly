from email.header import Header
from email.mime.text import MIMEText
from configparser import ConfigParser
import os
from math import sqrt
import smtplib

from django.shortcuts import render
from main_app.models import Hotel
from .controller import YANDEX_MAP_API_KEY, format_phone_number, get_work_time


CONFIGS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config')
MAIL_CONFIG_PATH = os.path.join(CONFIGS_PATH, 'mail_conf.ini')
print("CONFIGS_PATH", CONFIGS_PATH)
print("MAIL_CONFIG_PATH", MAIL_CONFIG_PATH)


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
                'metro': [[item.station, item.metro_line.first().img_url] for item in hotel.metro.all()],
            } for hotel in hotels
        ]
        # сортируем объекты по расстоянию от центра карты
        data_hotels.sort(key=lambda hotel: sqrt(
            (hotel['geo_point'][0] - base_point[0]) ** 2 + (hotel['geo_point'][1] - base_point[1]) ** 2
        ))
        data['hotels'].extend(data_hotels)

    return render(request, 'main_app/hotels.html', context=data)


def help_page(request):
    if not request.GET:
        return render(request, 'main_app/help.html')

    cfg = ConfigParser()
    try:
        cfg.read(MAIL_CONFIG_PATH)
    except Exception:
        return

    name = request.GET.get('name')
    email = request.GET.get('email')
    message = request.GET.get('msg')
    server, port = cfg.get('smtp_server', 'server'), cfg.get('smtp_server', 'port')
    send_mail, send_password = cfg.get('send_mail', 'mail'), cfg.get('send_mail', 'password')
    recipients_emails = cfg.get('recipients_emails', 'mail')

    if name and email and message:
        send_message = f'Отправитель: {name}\ne-mail: {email}\nСообщение: {message}'
        msg = MIMEText(send_message, 'plain', 'utf-8')
        msg['Subject'] = Header('Центр поддержки', 'utf-8')
        msg['From'] = send_mail
        msg['To'] = recipients_emails

        smtp_obj = smtplib.SMTP(server, 587, timeout=10)
        try:
            smtp_obj.starttls()
            smtp_obj.login(send_mail, send_password)
            smtp_obj.sendmail(send_mail, recipients_emails, msg.as_string())
        finally:
            smtp_obj.quit()

    return render(request, 'main_app/help.html')


def privacy_page(request):
    return render(request, 'main_app/privacy.html')
