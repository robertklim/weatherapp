import requests
from django.shortcuts import render
from .models import City

def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=dd9f63d91bf3db2c048962dbaef3ac94'
    city = 'Warsaw'

    cities = City.objects.all().order_by('name')

    weather_data = []

    for city in cities:

        res = requests.get(url.format(city.name)).json()

        city_weather = {
            'city': city.name,
            'temperature': res['main']['temp'],
            'description': res['weather'][0]['description'],
            'icon': res['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {
        'weather_data': weather_data
    }

    return render(request, 'weather/weather.html', context)
