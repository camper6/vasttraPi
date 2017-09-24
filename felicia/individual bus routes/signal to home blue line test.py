import os
from xml.dom import minidom
import urllib.request

#get the data from Ecan for Blue line 
downloaded_data = urllib.request.urlopen('http://rtt.metroinfo.org.nz/rtt/public/utility/file.aspx?ContentType=SQLXML&Name=JPRoutePositionET2&PlatformNo=53116')

#Parsing the data for Blue line
dom = minidom.parse(downloaded_data)

#Getting the bus route Blue line
blue_line = dom.getElementsByTagName('Route')

#print Bus No.28
for route in blue_line:
    Blue = route.getAttribute('RouteNo')
    if Blue == "B":
        print("Blue line ({})".format(Blue))

#print the ETA Blue line at Bus stop no. 53116
trip = dom.getElementsByTagName('Trip')[4]

ETA = trip.getAttribute('ETA')
print("Bus arrives in {} minutes at bus stop #53116.".format(ETA))
