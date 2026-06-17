import statistics # For finding mean of coordinates.

# Import geopy library and Nominatim class.
from geopy.geocoders import Nominatim
# Call the Nominatim tool and create Nominatim class.
loc = Nominatim(user_agent="Geopy Library")
geolocator = Nominatim(user_agent='myapplication')

# User enters the addresses
addlist = ["80 Fen, city of london, UK",
           "Southfields station, London"]
### I would like to create a UI where the User inputs the addresses one by one.

# Find midpoint by averaging latitudes and longitudes (consider using Northings/Easting instead?).
# Create list of lats and longs for each address.
norths, easts = list(), list()
for addy in addlist:
    # Get address from geopy
    location = geolocator.geocode(addy, exactly_one=True, language="en", namedetails=True, addressdetails=True)
    
    # Check that all locations are in the UK.
    country = location.raw['address']['country']
    if country != "United Kingdom":
        print("Not all of your addresses are located in the United Kingdom. This may skew results.\nAre you sure you want to continue?")
    ### I want to create UI that allows user to accept and continue or not.

    # Fetch coordinates
    north, east = location.latitude, location.longitude
    norths.append(north)
    easts.append(east)

midpoint_north, midpoint_east = statistics.fmean(norths), statistics.fmean(easts)
midpoint_as_string = str(midpoint_north) + ", " + str(midpoint_east)
midpoint_address = geolocator.reverse(midpoint_as_string)
print("Midpoint: ", midpoint_address)
### I would like to output a map showing all the addresses and the central point. The map should be interactive: scrollable and zoomable.
