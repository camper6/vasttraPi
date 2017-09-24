import os
from xml.dom import minidom
import urllib.request


urlBusRoute17 = 'http://rtt.metroinfo.org.nz/rtt/public/utility/file.aspx?ContentType=SQLXML&Name=JPRoutePositionET2&PlatformNo=23411'


#reading bus route function and it accepts a string. 
def readBusRoute(url):
    opendata = urllib.request.urlopen(url)
    dom = minidom.parse(opendata)
    routes = dom.getElementsByTagName('Route')
    for route in routes:
        print(route.)

readBusRoute(urlBusRoute17)
