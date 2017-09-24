import os
from xml.dom import minidom
import urllib.request


#get the data from Ecan for Bus No. 28 
downloaded_data = urllib.request.urlopen('http://rtt.metroinfo.org.nz/rtt/public/utility/file.aspx?ContentType=SQLXML&Name=JPRoutePositionET2&PlatformNo=53116')

#Parsing the data for Bus No. 28
dom = minidom.parse(downloaded_data)

#Getting the bus route No. 28
route_28 = dom.getElementsByTagName('Route')

#print only Bus No.28
for route in route_28:
    Bus_28 = route.getAttribute('RouteNo')
    if Bus_28 == "28":
        print("Bus no. {}".format(Bus_28))

#print the ETA Bus No. 28 at Bus stop no. 53116
trip = dom.getElementsByTagName('Trip')[1]

ETA = trip.getAttribute('ETA')
print("Bus arrives in {} minutes at bus stop #53116.".format(ETA))
