# Import geopy library and Nominatim class
from geopy.geocoders import Nominatim
# Call the Nominatim tool and create Nominatim class
loc = Nominatim(user_agent="Geopy Library")
geolocator = Nominatim(user_agent='myapplication')

# User enters the addresses
addlist = ["City of derry airport, northern ireland",
           "80 Fen, city of london, UK",
           "eiffel tower, france"]
### I would like to create a UI where the User inputs the addresses one by one.

for addy in addlist:
    # Get address from geopy
    location = geolocator.geocode(addy, exactly_one=True, language="en", namedetails=True, addressdetails=True)
    
    # Check that all locations are in the UK.
    country = location.raw['address']['country']
    if country != "United Kingdom":
        print("Not all of your addresses are located in the United Kingdom. This may skew results.\nAre you sure you want to continue?")
    ### I want to create UI that allows user to accept and continue or not.

    # Print address
    print(location.address)
    # Print latitude and longitude
    print(location.latitude, location.longitude)

### I would like to output a map showing all the addresses and the central point. The map should be interactive: scrollable and zoomable.