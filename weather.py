
import requests

city= input('Bienvenido, cual es la ciudad de la cual necesita ver el clima \n')

url = 'http://api.weatherapi.com/v1/current.json?key=897d79d9ed0c423da82160640241806&q='+city+'&aqi=no'
response = requests.get(url)

weather_json = response.json()

temp = weather_json.get('current').get('temp_c') 
descriptiom = weather_json.get('current').get('condition').get('text')

print(f'El clima en {city} capital es {descriptiom} y con {temp} grados')


