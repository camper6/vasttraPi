from tkinter import *
import time
import tkinter as tk


root = Tk()
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

busNoLbl = tk.Label(subHeadersFrame, text="      Bus Number          ", font=("Helvetica", subHeaderFontSize), bg="black", fg="white")
busDestLbl = tk.Label(subHeadersFrame, text="         Destination      ", font=("Helvetica", subHeaderFontSize), bg="black", fg="white")
minsLeftLbl = tk.Label(subHeadersFrame, text="       Minutes Left        ", font=("Helvetica", subHeaderFontSize), bg="black", fg="white")

busNoLbl.grid(row=0, column=0)
busDestLbl.grid(row=0, column=100)
minsLeftLbl.grid(row=0, column=200)
# Expand the middle column so the other two move to the sides
subHeadersFrame.grid_columnconfigure(1, weight=1)



clock = Label(root, font=('times', 25, 'bold',), bg='black', fg='white')
clock.place(x=640, y=20)

def tick():
   s = time.strftime('%H:%M:%S')
   if s != clock["text"]:
       clock["text"] = s
   clock.after(200, tick)
tick()
root.mainloop()
