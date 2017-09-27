from tkinter import *
import time
import tkinter as tk
from busrouteExtractor import *

read = ReadXMLBusRoutes()
busPlatform = 23411

#get the data from Ecan for Bus No. 17 
busroutes = read.getBusRoutes(busPlatform)
route17 = busroutes.getBusRoute(17)
print(route17)

#print the ETA Bus No. 17 at Bus stop no. 23411
trip = route17.trips[0]
ETA = trip.eta

class GUI(object):
   def __init__(self, master, **kwargs):
      root.geometry("800x600")

      headerFontSize = 25
      subHeaderFontSize = 20
      
      # A new frame inside master with boarder
      headerFrame = tk.Frame(root)
      # Set the header frame's background to black
      headerFrame.configure(background='black')
      # Use the grid layout and expand the frame
      #headerFrame.grid(row=0, sticky=tk.E + tk.W)
      headerFrame.place(x=0, y=20)

      # Label inside heade frame
      headerLbl = tk.Label(headerFrame, text="                                      Departures                                 ", font=("Helvetica bold", headerFontSize), bg="black", fg="white")
      # Place label on grid layout, row 0 and do not expand
      headerLbl.grid(row=0)
      # Center column 0 inside header frame
      headerFrame.grid_columnconfigure(0, weight=1)


      subHeadersFrame = tk.Frame(root)
      subHeadersFrame.configure(background='black')
      #subHeadersFrame.grid(row=1, sticky=tk.E + tk.W)
      subHeadersFrame.place(x=0, y=70)

      busNoLbl = tk.Label(subHeadersFrame, text="Bus Number", font=("Helvetica", subHeaderFontSize), bg="black", fg="white")
      busDestLbl = tk.Label(subHeadersFrame, text="Destination", font=("Helvetica", subHeaderFontSize), bg="black", fg="white")
      minsLeftLbl = tk.Label(subHeadersFrame, text="Minutes Left", font=("Helvetica", subHeaderFontSize), bg="black", fg="white")

      busNoLbl.grid(row=0, column=0)
      busDestLbl.grid(row=0, column=100)
      minsLeftLbl.grid(row=0, column=200)

      # Expand the middle column so the other two move to the sides
      subHeadersFrame.grid_columnconfigure(1, weight=1)

      #trip and bus route not getting the information from ecan data and not displaying properly.
      busNoLbl = tk.Label(subHeadersFrame, text= "Bus_17", font=("Helvetica", subHeaderFontSize), bg="black", fg="white")
      busDestLbl = tk.Label(subHeadersFrame, text= route17.destination , font=("Helvetica", subHeaderFontSize), bg="black", fg="white")
      minsLeftLbl = tk.Label(subHeadersFrame, text= ETA , font=("Helvetica", subHeaderFontSize), bg="black", fg="white")

      #manually displaying in gui for bus 17 set row to 1
      busNoLbl.grid(row=1, column=0)
      busDestLbl.grid(row=1, column=100)
      minsLeftLbl.grid(row=1, column=200)

      self.clock = Label(root, font=('times', 25, 'bold',), bg='black', fg='white')
      self.clock.place(x=640, y=20)

   def tick(self):
      s = time.strftime('%H:%M:%S')
      if s != self.clock["text"]:
         self.clock["text"] = s
      self.clock.after(200, self.tick)


#Beginning of the creation of GUI.
root = tk.Tk()
gui = GUI(root)
gui.tick()
root.mainloop()
