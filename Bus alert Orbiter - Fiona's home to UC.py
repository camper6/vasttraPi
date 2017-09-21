#Parsing XML data into Python
#Using data from ECan - Route Position ETA Version 2
#Fiona's home to UC:
#	Orbiter (Bus stop no. 11626)


import os
from xml.dom import minidom
import urllib.request


#get the data from Ecan for Orbiter 
downloaded_data = urllib.request.urlopen('http://rtt.metroinfo.org.nz/rtt/public/utility/file.aspx?ContentType=SQLXML&Name=JPRoutePositionET2&PlatformNo=11626')

#Parsing the data for Orbiter
dom = minidom.parse(downloaded_data)

#Getting the bus route No. 17
orbiter = dom.getElementsByTagName('Route')

#print only Orbiter
for route in orbiter:
    Orbiter = route.getAttribute('RouteNo')
    if Orbiter == "Oc":
        print("Bus {} - Orbiter".format(Orbiter))

#print the ETA Orbiter at Bus stop no. 11626
trip = dom.getElementsByTagName('Trip')[0]

ETA = trip.getAttribute('ETA')
print("Bus arrives in {} minutes at bus stop #11626.".format(ETA))

print()







