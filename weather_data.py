from pyowm import *
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('c3232b5e4b7ccbe150f5d751b0f96f41', config_dict)

reg = owm.geocoding_manager()


def weather_helper(user_location):
    """
    :param user_location: локация пользователя
    :return: текущую погоду в его локации
    """
    my_lat = user_location.latitude
    my_lon = user_location.longitude
    mgr = owm.weather_manager()
    one_call = mgr.one_call(lat=my_lat, lon=my_lon)
    city = reg.reverse_geocode(round(user_location.latitude, 2), round(user_location.longitude, 2))
    current_weather = """
    Текущая погода в {0}:
     - Температура: {1}C
     - Ощущается как: {2}C
     - Давление: {3} гПа
     - Влажность: {4}%
    """.format(city[0].name,
               one_call.current.temperature('celsius')['temp'],
               one_call.current.temperature('celsius')['feels_like'],
               one_call.current.pressure['press'],
               one_call.current.humidity)
    return current_weather
