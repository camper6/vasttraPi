import os
from xml.dom import minidom
import urllib.request

# The class for holding the attributes in the Trip element
class Trip(object):
    
    # Initializes the class
    def __init__(self, eta, tripID, wheelchairAccess):
        self.eta = int(eta)
        self.tripID = tripID
        self.wheelchairAccess = wheelchairAccess

    # A method call when trying to print the attributes in the class
    def __str__(self):
        eta = "Estimate Time of Arrival: {}".format(self.eta)
        tripID = "TripID: {}".format(self.tripID)
        wheelchairAccess = "WheelchairAccess: {}".format(self.wheelchairAccess)
        tripStr = "{} {} {}".format(eta, tripID, wheelchairAccess)
        return tripStr

# The class holding the attributes and elements in the Route element
class BusRoute(object):

    # Initializes the class
    def __init__(self, routeNo, routeName, destination, trips):
        self.routeNo = routeNo
        self.routeName = routeName
        self.destination = destination
        self.trips = trips # Holds a list of Trip

    # A method call when trying to print the attributes in the class
    def __str__(self):
        num = "Route Number: {}".format(self.routeNo)
        name = "Route Name: {}".format(self.routeName)
        destination = "Destination: {}".format(self.destination)
        tripStr = ""
        for trip in self.trips:
            tripStr += "{}\n".format(trip)
        return "{} {} {}:\n{}".format(num, name, destination, tripStr)

# The class holding the other classes as a property
class BusRoutes(object):

    # Initializes the class
    def __init__(self, busroutes):
        self.busroutes = busroutes # Holds a list of BusRoute

    # Gets a specific bus route by its route number
    def getBusRoute(self, routeNo):
        for route in self.busroutes:
            if str(routeNo) == route.routeNo:
                return route

    # A method call when trying to print the attributes in the class
    def __str__(self):
        routesStr = ""
        for route in self.busroutes:
            routesStr += "{}\n".format(route)
        return routesStr

# Holds no properties, ONLY FOR READING AND EXTRACTING
class ReadXMLBusRoutes(object):

    # Gets the BusRoutes, this method does everything
    def getBusRoutes(self, busPlatform):
        url = self.getBusPlatformURL(busPlatform)
        dom = self.getBusPlatformDOM(url)
        return self.extractBusRoutes(dom)

    # Gets the BusPlatform URL
    def getBusPlatformURL(self, busPlatform):
        url = "http://rtt.metroinfo.org.nz/rtt/public/utility/file.aspx?ContentType=SQLXML&Name=JPRoutePositionET2&PlatformNo={}".format(busPlatform)
        return url

    # Gets the extracted the data from the class's url and parses it into a document
    def getBusPlatformDOM(self, url):
        opendata = urllib.request.urlopen(url)
        dom = minidom.parse(opendata)
        return dom

    # Extracts the values in the document and returns a BusRoutes instance 
    def extractBusRoutes(self, dom):
        busRoutes = []
        
        # gets the Routes elements and its attributes
        routes = dom.getElementsByTagName('Route')
        for route in routes:
            routeNo = route.getAttribute('RouteNo')
            routeName = route.getAttribute('Name')
            
            listofTrips = [] # reinitialize and clears the list of Trip
            
            # gets the Destination elements and its attribute name
            for destination in route.getElementsByTagName('Destination'):
                destinationName = destination.getAttribute('Name')
                
                # gets the Trip elements and its attributes
                for trip in destination.getElementsByTagName('Trip'):
                    eta = trip.getAttribute('ETA')
                    tripID = trip.getAttribute('TripID')
                    # checks if it has wheelchair access
                    if trip.hasAttribute('WheelchairAccess'):
                        wheelchairAccess = trip.getAttribute('WheelchairAccess') == 'true'
                    else:
                        wheelchairAccess = False

                    # adds Trip into the list listofTrips
                    listofTrips.append(Trip(eta, tripID, wheelchairAccess))

            # adds an instance of BusRoute into the list busRoutes
            busRoutes.append(BusRoute(routeNo, routeName, destinationName, listofTrips))

        # returns an instance of the class BusRoutes holding the list
        return BusRoutes(busRoutes)
