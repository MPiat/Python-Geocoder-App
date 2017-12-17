import pandas
from geopy import Nominatim
import geopy
import sys
import os
import os.path

def file_handling(file_name):
    if os.path.isfile("./templates/home.html"):
        os.remove("./templates/home.html")
    data=pandas.read_csv(file_name)
    try:
        d = list(data["Address"])

    except:
        f = open('./templates/home.html','w')

        message = """<html>
        <head></head>
        <body><p>Input data does not contain an "Address" column.</p></body>
        </html>"""

        f.write(message)
        f.close()
        return 0


    #Create a new column in a submitted file and add every coordinate to a column
    #Or plot all the coordinates on a map
    geolocator = Nominatim()
    lat = []
    lng = []
    for address in d:

        #add an exception for bad data

        try:
            location = geolocator.geocode(address)
        except:
            with open('./templates/home.html','w') as file:
                error_msg = """<html>
                <head></head>
                <body><p>Geocoding service error.</p></body>
                </html>"""
                file.write(error_msg)

        if type(address) != str:
            lat.append("Error")
            lng.append("Error")
        else:
            lat.append(str(location.latitude))
            lng.append(str(location.longitude))



    data.insert(1, "Latitude", lat, allow_duplicates=True)
    data.insert(2, "Longitude", lng, allow_duplicates=True)

    #data["Latitude"]=data["Coordinates"].apply(lambda x: x.latitude if x != None else None)
    #data["Longitude"]=data["Coordinates"].apply(lambda x: x.lngitude if x != None else None)

    data.to_html("./templates/home.html", index=False)
