from tkinter import *
import time


root = Tk()
root.geometry("800x600")

clock = Label(root, font=('times', 30, 'bold'), bg='black', fg='white')
clock.place(x=640, y=5)
#clock.pack(fill=BOTH, expand=1)
def tick():
    s = time.strftime('%H:%M:%S')
    if s != clock["text"]:
        clock["text"] = s
    clock.after(200, tick)
tick()
root.mainloop()
