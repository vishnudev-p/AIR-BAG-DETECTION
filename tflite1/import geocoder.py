import geocoder

# Retrieve the location of the laptop
location = geocoder.ip('me')

# Access latitude and longitude from the location object
latitude = location.latlng[0]
longitude = location.latlng[1]
