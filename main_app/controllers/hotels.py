import datetime
from os import environ


YANDEX_MAP_API_KEY = environ.get('MAP_API_KEY')


def format_phone_number(phone_number: int) -> str:
    number = str(phone_number)

    return '+7 ({}) {}-{}-{}'.format(number[1:4], number[4:7], number[7:9], number[9:])


def get_work_time(opening_time: datetime.time, closing_time: datetime.time):
    if opening_time == closing_time:
        return 'Круглосуточно'

    return f'c {opening_time.isoformat(timespec="minutes")} до {closing_time.isoformat(timespec="minutes")}'
