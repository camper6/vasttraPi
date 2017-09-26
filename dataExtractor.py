import os
from xml.dom import minidom
import urllib.request

class Trip(object):
    def __init__(self, eta, tripID, wheelchairAccess):
        self.eta = int(eta)
        self.tripID = tripID
        self.wheelchairAccess = wheelchairAccess

    def __str__(self):
        eta = "Estimate Time of Arrival: {}".format(self.eta)
        tripID = "TripID: {}".format(self.tripID)
        wheelchairAccess = "WheelchairAccess: {}".format(self.wheelchairAccess)
        tripStr = "{} {} {}".format(eta, tripID, wheelchairAccess)
        return tripStr

class BusRoute(object):
    def __init__(self, routeNo, routeName, destination, trips):
        self.routeNo = routeNo
        self.routeName = routeName
        self.destination = destination
        self.trips = trips

    def __str__(self):
        num = "Route Number: {}".format(self.routeNo)
        name = "Route Name: {}".format(self.routeName)
        destination = "Destination: {}".format(self.destination)
        tripStr = ""
        for trip in self.trips:
            tripStr += "{}\n".format(trip)
        return "{} {} {}:\n{}".format(num, name, destination, tripStr)

class BusRoutes(object):
    def __init__(self, busroutes):
        self.busroutes = busroutes

    # Gets a specific bus route by its route number
    def getBusRoute(self, routeNo):
        for route in self.busroutes:
            if str(routeNo) == route.routeNo:
                return route

    def __str__(self):
        routesStr = ""
        for route in self.busroutes:
            routesStr += "{}\n".format(route)
        return routesStr
        
class ReadXMLBusRoutes(object):
    
    def __init__(self, busPlatform):
        self.url = "http://rtt.metroinfo.org.nz/rtt/public/utility/file.aspx?ContentType=SQLXML&Name=JPRoutePositionET2&PlatformNo={}".format(busPlatform)
        self.dom = self.extractDatas()
        
    def extractDatas(self):
        opendata = urllib.request.urlopen(self.url)
        dom = minidom.parse(opendata)
        return dom

    #reading bus route function and it accepts a string. 
    def extractBusRoutes(self):
        routes = self.dom.getElementsByTagName('Route')
        busRoutes = []
        for route in routes:
            routeNo = route.getAttribute('RouteNo')
            routeName = route.getAttribute('Name')
            listofTrips = []
            for destination in route.getElementsByTagName('Destination'):
                destinationName = destination.getAttribute('Name')
                for trip in destination.getElementsByTagName('Trip'):
                    eta = trip.getAttribute('ETA')
                    tripID = trip.getAttribute('TripID')
                    if trip.hasAttribute('WheelchairAccess'):
                        wheelchairAccess = trip.getAttribute('WheelchairAccess') == 'true'
                    else:
                        wheelchairAccess = False
                    listofTrips.append(Trip(eta, tripID, wheelchairAccess))
            busRoutes.append(BusRoute(routeNo, routeName, destinationName, listofTrips))
        return BusRoutes(busRoutes)


busPlatform = 23411
    
busroutes = ReadXMLBusRoutes(busPlatform).extractBusRoutes()
route17 = busroutes.getBusRoute(17)
print(busroutes)
