import datetime
from math import sqrt
from typing import Any, Dict, List, Tuple

from main_app.models import Hotel


def format_phone_number(phone_number: int) -> str:
    number = str(phone_number)

    return '+7 ({}) {}-{}-{}'.format(number[1:4], number[4:7], number[7:9], number[9:])


def get_work_time(opening_time: datetime.time, closing_time: datetime.time) -> str:
    if opening_time == closing_time:
        return 'Круглосуточно'

    return f'c {opening_time.isoformat(timespec="minutes")} до {closing_time.isoformat(timespec="minutes")}'


def get_hotels_list(base_point: Tuple[float, float]) -> List[Dict[str, Any]]:
    hotels = Hotel.objects.select_related()

    if not hotels:
        return []

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

    return data_hotels
