#Parsing XML data into Python
#Signal to UC via Purple Line


import os
from xml.dom import minidom
import urllib.request


#get the data from Ecan for Purple Line
downloaded_data = urllib.request.urlopen('http://rtt.metroinfo.org.nz/rtt/public/utility/file.aspx?ContentType=SQLXML&Name=JPRoutePositionET2&PlatformNo=53088')

#Parsing the data for Purple Line
dom = minidom.parse(downloaded_data)

#Getting the bus route for Purple Line
Purple_route = dom.getElementsByTagName('Route')
Destination_name = dom.getElementsByTagName('Destination')

for destination in Destination_name:
    Purple_dest = destination.getAttribute('Name')
    if Purple_dest == "Airport via University":

#print only Purple Line
        for route in Purple_route:
            Purple = route.getAttribute('RouteNo')
            
            if Purple == "P":
                name="Purple line"
                print("{}".format(name))

#print the Purple Line bus ETA at Bus stop no. 53088
trip = dom.getElementsByTagName('Trip')[0]

ETA = trip.getAttribute('ETA')
print("Bus arrives in {} minutes at bus stop #53088.".format(ETA))



