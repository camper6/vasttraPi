#Parsing XML data into Python
#Using data from ECan - Route Position ETA Version 2
#Fiona's home to Central Station:
#	Bus No. 17 (Bus stop no. 23411)
#	Bus No. 28 (Bus stop no. 32974)
#	Bus - Blue line (Bus stop no. 23337)


import os
from xml.dom import minidom
import urllib.request


#get the data from Ecan for Bus No. 17 
downloaded_data = urllib.request.urlopen('http://rtt.metroinfo.org.nz/rtt/public/utility/file.aspx?ContentType=SQLXML&Name=JPRoutePositionET2&PlatformNo=23411')

#Parsing the data for Bus No. 17
dom = minidom.parse(downloaded_data)

#Getting the bus route No. 17
route_17 = dom.getElementsByTagName('Route')

#print only Bus No.17
for route in route_17:
    Bus_17 = route.getAttribute('RouteNo')
    if Bus_17 == "17":
        print("Bus no. {}".format(Bus_17))

#print the ETA Bus No. 17 at Bus stop no. 23411
trip = dom.getElementsByTagName('Trip')[0]

ETA = trip.getAttribute('ETA')
print("Bus arrives in {} minutes at bus stop #23411.".format(ETA))

print()

#get the data from Ecan for Bus No. 28 
downloaded_data = urllib.request.urlopen('http://rtt.metroinfo.org.nz/rtt/public/utility/file.aspx?ContentType=SQLXML&Name=JPRoutePositionET2&PlatformNo=32974')

#Parsing the data for Bus No. 28
dom = minidom.parse(downloaded_data)

#Getting the bus route No. 28
route_28 = dom.getElementsByTagName('Route')

#print Bus No.28
for route in route_28:
    Bus_28 = route.getAttribute('RouteNo')
    if Bus_28 == "28":
        print("Bus no. {}".format(Bus_28))

#print the ETA Bus No. 28 at Bus stop no. 32974
trip = dom.getElementsByTagName('Trip')[0]

ETA = trip.getAttribute('ETA')
print("Bus arrives in {} minutes at bus stop #32974.".format(ETA))

print()

#get the data from Ecan for Blue line 
downloaded_data = urllib.request.urlopen('http://rtt.metroinfo.org.nz/rtt/public/utility/file.aspx?ContentType=SQLXML&Name=JPRoutePositionET2&PlatformNo=23337')

#Parsing the data for Blue line
dom = minidom.parse(downloaded_data)

#Getting the bus route Blue line
blue_line = dom.getElementsByTagName('Route')

#print Bus No.28
for route in blue_line:
    Blue = route.getAttribute('RouteNo')
    if Blue == "B":
        print("Blue line ({})".format(Blue))

#print the ETA Blue line at Bus stop no. 23337
trip = dom.getElementsByTagName('Trip')[0]

ETA = trip.getAttribute('ETA')
print("Bus arrives in {} minutes at bus stop #23337.".format(ETA))

print()






