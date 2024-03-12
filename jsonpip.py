#This code sends a request to the Open Notify API to retrieve information about astronauts currently in space, then parses the JSON response to print out the names of the astronauts.

import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json() #to decode the json from the response
print(json)

for person in json['people']:
    print(person['name'])
