# https://automatetheboringstuff.com/chapter14/
# this is for the user to sign up for API
import json
import requests

location = ['quickWeather.py', 'San', 'Francisco,', 'CA']
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (
    location)
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
