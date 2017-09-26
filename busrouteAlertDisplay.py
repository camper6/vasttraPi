from datetime import datetime
import tkinter as tk
import getpass
onPi = getpass.getuser() == "pi" 
sideColumnMinSize = 100
departureFontSize = 40
destinationFontSize = int(departureFontSize / 2) if onPi else departureFontSize
headerFontSize = 25
subHeaderFontSize = 20
class GUI:
    def __init__(self, master, **kwargs):
        self.master = master
        # A list that will hold the temporary departure frames so to destroy them upon refreshing
        self.departureRowFrames = []
        self.currentlyDisplayedDepartures = []  # Used to decide whether to refresh the display

        self.master.grid()
        self.master.title("Departures")

        # A new frame inside master with boarder
        headerFrame = tk.Frame(master, bd="0")
        # Set the header frame's background to black
        headerFrame.configure(background='black')
        # Use the grid layout and expand the frame
        headerFrame.grid(row=0, sticky=tk.E + tk.W)

        # Label inside heade frame
        headerLbl = tk.Label(headerFrame, text="Departures", font=("Helvetica bold", headerFontSize), bg="black", fg="white")
        # Place label on grid layout, row 0 and do not expand
        headerLbl.grid(row=0)
        # Center column 0 inside header frame
        headerFrame.grid_columnconfigure(0, weight=1)

        subHeadersFrame = tk.Frame(master)
        subHeadersFrame.configure(background='black')
        subHeadersFrame.grid(row=1, sticky=tk.E + tk.W)

        busNoLbl = tk.Label(subHeadersFrame, text="Bus Number", font=("Helvetica", subHeaderFontSize), bg="black", fg="white")
        busDestLbl = tk.Label(subHeadersFrame, text="Destination", font=("Helvetica", subHeaderFontSize), bg="black", fg="white")
        minsLeftLbl = tk.Label(subHeadersFrame, text="Minutes Left", font=("Helvetica", subHeaderFontSize), bg="black", fg="white")

        busNoLbl.grid(row=0, column=0)
        busDestLbl.grid(row=0, column=1)
        minsLeftLbl.grid(row=0, column=2)
        # Expand the middle column so the other two move to the sides
        subHeadersFrame.grid_columnconfigure(1, weight=1)

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

root = tk.Tk()
gui = GUI(root)
root.mainloop()
