import requests


def explore():

    response = requests.get('https://api.ipify.org?format=json')
    ip_data = response.json()
    external_ip = ip_data['ip']

    response = requests.get(f'https://ipinfo.io/{external_ip}/json')
    geo_data = response.json()
    country = geo_data['country']
    city = geo_data['city']

    response = requests.get("http://api.openweathermap.org/data/2.5/find",
                            params={'q': city, 'APPID': "your_secret_key", 'units': 'metric'})
    weather_data = response.json()

    curr_weather = {
        'location': weather_data['list'][0]['name'],
        'temp': weather_data['list'][0]['main']['temp'],
        'wind': weather_data['list'][0]['wind']['speed'],
        'maxtemp': weather_data['list'][0]['main']['temp_max'],
        'mintemp': weather_data['list'][0]['main']['temp_min']
    }



    return curr_weather


