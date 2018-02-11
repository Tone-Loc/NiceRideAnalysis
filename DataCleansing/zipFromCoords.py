import requests


def zipFromCoords(latitude, longitude, sensor):
    requests.get("http://maps.googleapis.com/maps/api/geocode/json?latlng=" + latitude + longitude + "&sensor=" + sensor)


    response = requests.get(url)
                                                                                    
    return response.json()['results'][0]['formatted_address']
