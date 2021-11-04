from django.shortcuts import get_object_or_404, redirect, render
import requests
from decouple import config
from pprint import pprint
from .models import City
from django.contrib import messages
# Create your views here.

def index(request):
    cities = City.objects.all()
    g_city = request.GET.get('name')
    if g_city:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={g_city}&appid={config('API_KEY')}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            content = response.json()
            a_city = content["name"]
            if City.objects.filter(name=a_city):
                messages.warning(request, "City already exists.")
            else:
                City.objects.create(name=a_city)
                messages.success(request, "City successfully saved.")
        else:
            messages.warning(request, "City does not exist.")
        return redirect("home")
        
    cityData = []
    for city in cities:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={config('API_KEY')}&units=metric"
        response = requests.get(url)
        content = response.json()
        data = {
			"city" : city,
            "temp" : content["main"]["temp"],
            "desc" : content["weather"][0]["description"],
            "icon" : content["weather"][0]["icon"],
		}
        cityData.append(data)
        
    context = {
		"city_data" : cityData,
	}
    
    return render(request, "weather_app/index.html", context)


def delete_city(request, id):
    city = get_object_or_404(City, id=id)
    city.delete()
    return redirect('home')