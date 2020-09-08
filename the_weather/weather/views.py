from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=f25bc2de38b13f2ad677fa9435338e57'
    cities = City.objects.all()
    # print (cities)
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    
    form = CityForm()
    weather_data = []
    for city in cities:        
        city_weather = requests.get(url.format(city)).json()
        # print (city_weather)
    
        weather = {
            'city' : city,
            'temperature' : city_weather["main"]["temp"],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }
        weather_data.append(weather)
        
    context = {'weather_data' : weather_data, 'form' : form}
    
    return render(request, 'weather/index.html', context)