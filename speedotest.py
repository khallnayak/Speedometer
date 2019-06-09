import speedometer
from tkinter import *
root=Tk()
canvas=Canvas(root,height=500,width=500)
canvas.pack()
canvas.create_oval(0,0,500,500,tag="oval")
A=speedometer.Speedometer(canvas,"oval",Range=(-500,1000))
A.moveto(-500,"oval")
A.changerange(Range=(0,20),rfont=("Verdana",9))
