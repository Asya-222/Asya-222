import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    url = 'https://samples.openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    cities = City.objects.all()
    weather_of_cities = []


    for city in cities:
        r = requests.get(url.format(city)).json()
        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
        }
        weather_of_cities.append(city_weather)

    print(weather_of_cities)


    context = {'weather_of_cities': weather_of_cities, 'form': form}
    return render(request, 'weather/weather.html',context)
