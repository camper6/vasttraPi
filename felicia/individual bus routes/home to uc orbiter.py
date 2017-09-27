#Parsing XML data into Python
#Home to UC via Orbiter


import os
from xml.dom import minidom
import urllib.request


#get the data from Ecan for Orbiter
downloaded_data = urllib.request.urlopen('http://rtt.metroinfo.org.nz/rtt/public/utility/file.aspx?ContentType=SQLXML&Name=JPRoutePositionET2&PlatformNo=11626')

#Parsing the data for Orbiter
dom = minidom.parse(downloaded_data)

#Getting the bus route for Orbiter
Orbiter_route = dom.getElementsByTagName('Route')

#print only Orbiter
for route in Orbiter_route:
    Orbiter = route.getAttribute('RouteNo')
    if Orbiter == "Oc":
        name="Orbiter"
        print("{}".format(name))
        
#print the ETA Orbiter at Bus stop no. 11626
trip = dom.getElementsByTagName('Trip')[0]

ETA = trip.getAttribute('ETA')
print("Bus arrives in {} minutes at bus stop #11626.".format(ETA))



