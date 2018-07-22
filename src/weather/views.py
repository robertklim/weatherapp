import requests
from django.shortcuts import render

def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=dd9f63d91bf3db2c048962dbaef3ac94'
    city = 'Warsaw'

    res = requests.get(url.format(city)).json()

    city_weather = {
        'city': city,
        'temperature': res['main']['temp'],
        'description': res['weather'][0]['description'],
        'icon': res['weather'][0]['icon'],
    }

    context = {
        'city_weather': city_weather
    }

    return render(request, 'weather/weather.html', context)
