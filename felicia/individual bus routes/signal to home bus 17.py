import os
from xml.dom import minidom
import urllib.request


#get the data from Ecan for Bus No. 17 
downloaded_data = urllib.request.urlopen('http://rtt.metroinfo.org.nz/rtt/public/utility/file.aspx?ContentType=SQLXML&Name=JPRoutePositionET2&PlatformNo=53116')

#Parsing the data for Bus No. 17
dom = minidom.parse(downloaded_data)

#Getting the bus route No. 17
route_17 = dom.getElementsByTagName('Route')

#print only Bus No.17
for route in route_17:
    Bus_17 = route.getAttribute('RouteNo')
    if Bus_17 == "17":
        print("Bus no. {}".format(Bus_17))

#print the ETA Bus No. 17 at Bus stop no. 53116
trip = dom.getElementsByTagName('Trip')[0]

ETA = trip.getAttribute('ETA')
print("Bus arrives in {} minutes at bus stop #53116.".format(ETA))
