from wsgiref.util import request_uri
import requests
import math

API_KEY = '70e89b01d957b9430680d0a43110fda6'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

city = input('Enter a city name: ')
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273, 2)

    print('Weather:', weather)
    print('Temperature:', temperature)
else: 
    print("There was an error!")