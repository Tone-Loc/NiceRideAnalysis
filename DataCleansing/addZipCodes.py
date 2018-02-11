# reverse geocoding to get zip code of location from google api
# the zip code will be used to get daily weather

from googlemaps import GoogleMaps

gmaps = GoogleMaps(api_key)

destination = gmaps.latlng_to_address(38.887563, -77.019929)

print(destination)

# Independence and 6th SW, Washington, DC 20024, USA


http://py-googlemaps.sourceforge.net/

https://maps.googleapis.com/maps/api/geocode/json?latlng=37.383253,-122.078075&sensor=false
