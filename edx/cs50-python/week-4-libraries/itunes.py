import requests
# import json
from sys import argv, exit

if len(argv) != 2:
    exit('Invalid number of arguments')

response = requests.get(
    'https://itunes.apple.com/search?entity=song&limit=10&term='+argv[1])

output = response.json()
for result in output['results']:
    print(result['trackName'])

response = requests.get(
    'https://itunes.apple.com/search?entity=song&limit=1&term='+argv[1])

# print(json.dumps(response.json(), indent=2))
