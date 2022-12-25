import imp
import sys
from django.shortcuts import render
import json
import urllib.request
# from django.http import HttpResponse

# Create your views here.

def index(request):

    # return HttpResponse('Hi Najeem')
    if request.method == 'POST':
        city = request.POST['city']
        # res = urllib.request.urlopen(url = "https://api.openweathermap.org/data/2.5/weather?q= + city + &appid=94a1bc3e0d833ef61d89f77cdd9d5fba").read()
        res = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=94a1bc3e0d833ef61d89f77cdd9d5fba&units=metric").read()
        json_data = json.loads(res)

        data = {
            'country_code': str(json_data['sys']['country']),
            'coordinate': str(json_data['coord']['lon']) + " " + str(json_data['coord']['lat']),
            'temp': str(json_data['main']['temp']) + 'k',
            'humidity': str(json_data['main']['humidity']),
            'pressure': str(json_data['main']['pressure']),
            'wind': str(json_data['wind']['speed']) + " " + str(json_data['wind']['deg']),
            'weather':  json_data['weather'][0]['description']


        }
    else:
        city = ''
        data = {}

    return render (request, 'index.html',{'city':city,'data':data})
