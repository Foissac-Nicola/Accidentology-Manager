import urllib3
from urllib.parse import urlencode
import json

http = urllib3.PoolManager()

data = {
    'id': 1,
    'waypoint': {
        'x': 1,
        'y': 1
    },
    'waypoint': {
        'x': 2,
        'y': 3
    }
}

def getRequest(hhtp, data):
    request = http.request(
        'GET',
        'http://localhost:5000/Indicator',
        fields=data)
    print(json.loads(request.data))

def postRequest(http, data):
    encoded_data = urlencode(data)
    url = 'http://localhost:5000/Indicator' + encoded_data
    request = http.request(
        'POST',
        url)
    print(request.data)

getRequest(http, data)

#postRequest(http,data)