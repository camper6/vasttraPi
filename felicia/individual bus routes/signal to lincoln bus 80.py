import os
from xml.dom import minidom
import urllib.request


#get the data from Ecan for Bus No. 80 
downloaded_data = urllib.request.urlopen('http://rtt.metroinfo.org.nz/rtt/public/utility/file.aspx?ContentType=SQLXML&Name=JPRoutePositionET2&PlatformNo=53088')

#Parsing the data for Bus No. 80
dom = minidom.parse(downloaded_data)

#Getting the bus route No. 80
route_80 = dom.getElementsByTagName('Route')

#print only Bus No.80
for route in route_80:
    Bus_80 = route.getAttribute('RouteNo')
    if Bus_80 == "80":
        print("Bus no. {}".format(Bus_80))

#print the ETA Bus No. 80 at Bus stop no. 53116
trip = dom.getElementsByTagName('Trip')[3]

ETA = trip.getAttribute('ETA')
print("Bus arrives in {} minutes at bus stop #53088.".format(ETA))
