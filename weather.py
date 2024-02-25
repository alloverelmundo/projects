import requests

city = 'London'
url = 'http://api.weatherapi.com/v1/current.json?key=b75e05ec14fc49c7adc163932232012&q='+city+'&aqi=no'

response = requests.get(url)
weather_json = response.json() #to decode the json from the response

temp = weather_json.get('current').get('temp_f')
description = weather_json.get('current').get('condition').get('text')

print(description)

_____________________

temperature = 95;
if temperature > 85: 
    print("It's too hot!");
    print("Stay inside!");
elif temperature < 60:
    print("It's too cold!")
else:
    print("Enjoy the outdoors!");

temperature1 = 50;
if temperature1 > 90 or temperature1 <60:
    print("Stay inside!")

temperature2 = 75;
forecast = "rainy";
if temperature2 < 80 and forecast != "rainy":
    print("Go outside!")
else:
    print("Stay inside!");

if not forecast == "rainy": #not true = false, and not false = true
    print("Go outside!");
else:
    print("Stay inside!");

# boolean variables
raining = True;
if raining:
    print("Stay in!");
