#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from busrouteExtractor import *
from datetime import datetime
import time
import tkinter as tk
import getpass
import threading

busPlatform23411 = { 'BUS_PLATFORM' : 23411, 'BUS_LINE' : 17 }
busPlatform23337 = { 'BUS_PLATFORM' : 23337, 'BUS_LINE' : 'B' }
busPlatform32974 = { 'BUS_PLATFORM' : 32974, 'BUS_LINE' : 28 }
busPlatform11626 = { 'BUS_PLATFORM' : 11626, 'BUS_LINE' : 'Oc' } #Oc
busPlatformsNum = [ busPlatform23411, busPlatform23337, busPlatform32974, busPlatform11626 ]

mainThread = threading.current_thread()

onPi = getpass.getuser() == "pi"
sideColumnMinSize = 100
departureFontSize = 40
departureFontSize1 = 60
departureFontSize2 = 35
destinationFontSize = int(departureFontSize1 / 2) if onPi else departureFontSize2
headerFontSize = 25
subHeaderFontSize = 25


maxFutureDepartureTime = 120  # The maximum amount of time (in minutes) left for a departure that is displayed
guiRefreshRate = 15  # How often the gui checks for new departures (in seconds)

def disableScreenblanking():
    os.system("export DISPLAY=:0.0 && xset s off && xset s noblank && xset -dpms")

# Get the next trips as a list of busline numbers and minutes to leave for the next two trips
def getNextTrips():

    nextTrips = []
    for busPlatform in busPlatformsNum:
        platformNum = busPlatform['BUS_PLATFORM']
        busLine = busPlatform['BUS_LINE']
        route = BusPlatform(platformNum).getBusRoute(busLine)
        #print("{} {}".format(platformNum, busLine))
        for trip in route.trips:
            nextTrips.append((platformNum, route.routeNo, route.destination, trip.eta))

    return nextTrips

class GUI:
    def __init__(self, master, **kwargs):
        self.master = master
        # A list that will hold the temporary departure frames so to destroy them upon refreshing
        self.departureRowFrames = []
        self.currentlyDisplayedDepartures = []  # Used to decide whether to refresh the display

        self.master.grid()
        self.master.title("Departures")

        # A new frame inside master with border
        headerFrame = tk.Frame(master, bd="0")
        # Set the header frame's background to black
        headerFrame.configure(background='black')
        # Use the grid layout and expand the frame
        headerFrame.grid(row=0, sticky=tk.E + tk.W)

        # Label inside header frame
        headerLbl = tk.Label(headerFrame, text=" ", font=("Helvetica bold", headerFontSize), bg="black", fg="white")
        clock = tk.Label(headerFrame, text=time.strftime('%H:%M:%S'), font=("Helvetica bold", headerFontSize), bg="black", fg="white")
        # Place label on grid layout, row 0 and do not expand
        headerLbl.grid(row=0)
        clock.grid(row=0, column=1)
        # Center column 0 inside header frame
        headerFrame.grid_columnconfigure(0, weight=1)

        subHeadersFrame = tk.Frame(master)
        subHeadersFrame.configure(background='black')
        subHeadersFrame.grid(row=1, sticky=tk.E + tk.W)

        platformNoLbl = tk.Label(subHeadersFrame, text="{}Platform".format(" "*4), font=("Helvetica", subHeaderFontSize), bg="black", fg="white")
        busNoLbl = tk.Label(subHeadersFrame, text="{} Bus No.".format(" "*5), font=("Helvetica", subHeaderFontSize), bg="black", fg="white")
        busDestLbl = tk.Label(subHeadersFrame, text="Destination", font=("Helvetica", subHeaderFontSize), bg="black", fg="white")
        minsLeftLbl = tk.Label(subHeadersFrame, text="Minutes Left ", font=("Helvetica", subHeaderFontSize), bg="black", fg="white")

        platformNoLbl.grid(row=0, column=0)
        busNoLbl.grid(row=0, column=1)
        busDestLbl.grid(row=0, column=2)
        minsLeftLbl.grid(row=0, column=3)
        # Expand the middle column so the other two move to the sides
        subHeadersFrame.grid_columnconfigure(2, weight=1)

        # The frame that will contain the departures
        departuresFrame = tk.Frame(master)
        departuresFrame.grid(row=2, sticky=tk.E + tk.W)
        departuresFrame.grid_columnconfigure(1, weight=1)
        self.departuresFrame = departuresFrame  # Class variable to hold the container frame for all the departures

        # Keep everything in column 0 of master centered/expanded
        master.grid_columnconfigure(0, weight=1)

        w, h = master.winfo_screenwidth(), master.winfo_screenheight()
        master.overrideredirect(onPi)  # Set to 1 to force full window mode
        master.geometry("%dx%d+0+0" % (w, h))

        def tick():
            s = time.strftime('%H:%M:%S')
            if s != clock["text"]:
                clock["text"] = s
            clock.after(200, tick)
        tick()

    # Receives a list of tuples (busline, minutesToLeave) as the argument and displays them
    def populateTable(self, departures):
        currentRow = 0
        for departure in departures:
            (platform, bus, destination, minutes) = departure
            # If a departure is too far in the future, don't display it
            if minutes > maxFutureDepartureTime:
                continue
            # Change background color for each row
            bgColor = "#FFF289" if currentRow % 2 else "white"

            # The frame that will contain each departure
            rowFrame = tk.Frame(self.departuresFrame)
            rowFrame.grid(row=currentRow, columnspan=3, sticky=tk.E + tk.W)
            rowFrame.configure(background=bgColor)
            currentRow += 1

            # After we have created the frame that will hold each departure, create the labels
            platformNo = tk.Label(rowFrame, text="{} {}".format(" ", platform), font=("Helvetica", departureFontSize), bg=bgColor)
            busNo = tk.Label(rowFrame, text="{} {}".format(" "*4, bus), font=("Helvetica", departureFontSize), bg=bgColor)
            busDest = tk.Label(rowFrame, text=destination, font=("Helvetica", destinationFontSize), bg=bgColor)
            minsLeft = tk.Label(rowFrame, text="{} {}".format(int(minutes), " "*3) if int(minutes) != 0 else "Now", font=("Helvetica", departureFontSize), bg=bgColor)

            platformNo.grid(row=0, column=0)
            busNo.grid(row=0, column=1)
            busDest.grid(row=0, column=2)
            minsLeft.grid(row=0, column=3)

            # Expand the middle column to push the other two to the sides
            rowFrame.grid_columnconfigure(2, weight=1)
            # Set the minimum size of the side columns so the middle column text is always at the same position
            rowFrame.grid_columnconfigure(0, minsize=sideColumnMinSize)
            rowFrame.grid_columnconfigure(2, minsize=sideColumnMinSize)

            # Add the newly created frame to a list so we can destroy it later when we refresh the departures
            self.departureRowFrames.append(rowFrame)

    # Destroy any existing frames containing departures that already exist
    def resetDepartures(self):
        for frame in self.departureRowFrames:
            frame.destroy()
        # Empty the list as we have destroyed everything that was included in it
        self.departureRowFrames = []

def updateGui(gui):
    # Get the next trips from ECAN's public API for the station we are interested in
    nextTrips = getNextTrips()  # Contains a list of tuples (bus, minutesToDepart)
    # Sort the trips based on departure time (i.e. the third element in the tuples)
    nextTrips.sort(key=lambda trips: trips[3])
    # Update the displayed departures if they are different to the ones currently displayed
    if nextTrips != gui.currentlyDisplayedDepartures:
        gui.resetDepartures()  # Remove any already existing departures
        gui.populateTable(nextTrips)
        gui.currentlyDisplayedDepartures = nextTrips
    if mainThread.is_alive():
        threading.Timer(guiRefreshRate, updateGui, [gui]).start()


def main():
    # Initialize the API keys using the config file
    #initAPIkeys()
    # Initialize the connection to the Vasttrafik public API. If not succesful the script will exit here
    #initializeConnection()
    # When we are running on the raspberry pi we do not want the screen to turn off
    if onPi:
        disableScreenblanking()
    # Initialize UART towards the power control board
    #initializeSerial()
    root = tk.Tk()
    gui = GUI(root)
    updateGui(gui)  # Periodically update the gui with the latest departures
    #pollSerial()  # Poll UART for incoming commands from the control board
    root.mainloop()  # Blocking loop


if __name__ == "__main__":
    main()
