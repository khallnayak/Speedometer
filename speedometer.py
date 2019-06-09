from tkinter import *
import math as m
class RadiusError(Exception):
    pass

class Speedometer():
    def changerange(self,Range=(-10,190),rfont=("Verdana",12)):
        for i in range(-10,195,10):
            self.canvas.itemconfig(self.range_marks[int((i+10)/10)],text=str((i+10)*(Range[1]-Range[0])/200+Range[0]),font=rfont)                        
    def moveto(self,value,tag):
        if(value>self.range[1]):
            value=self.range[1]
            self.canvas.itemconfig(self.needle,fill="#000000")
        elif(value<self.range[0]):
            value=self.range[0]
            self.canvas.itemconfig(self.needle,fill="#000000")
        else:
            self.canvas.itemconfig(self.needle,fill=self.needlecolor)
        self.canvas.coords(self.needle,self.radius,self.radius,self.radius+self.radius*m.cos((value*self.slope+self.intercept)*m.pi/180),self.radius-self.radius*m.sin((value*self.slope+self.intercept)*m.pi/180))
    def __init__(self,canvas,tag,bg="#ffffff",needlecolor="#0d47a1",markscolor="#000000",Range=(0,200),digitscolor="#ff9933"):
        self.range=Range
        self.needlecolor=needlecolor
        self.canvas=canvas
        self.tag=tag
        temp=self.canvas.coords(tag)
        if((temp[0]-temp[2])!=(temp[1]-temp[3])):
            raise RadiusError
        else:
            self.radius=(temp[2]-temp[0])/2
        self.slope=200.0/(self.range[1]-self.range[0])
        self.intercept=190-self.range[1]*self.slope
        self.range_marks=[]
        q=10
        u=0
        for i in range(-10,195,5):
            if(i%10==0):
                x1,y1=self.radius+(self.radius-20)*m.cos(i*m.pi/180),self.radius-(self.radius-20)*m.sin(i*m.pi/180)
                canvas.create_line(x1,y1,self.radius+self.radius*m.cos(i*m.pi/180),self.radius-self.radius*m.sin(i*m.pi/180),fill=markscolor,width=3) 
                self.range_marks.append(canvas.create_text(x1+u,y1+q,text=str((i+10)*(self.range[1]-self.range[0])/200+self.range[0]),font=("Courier",int(self.radius/25)),fill=digitscolor))
            else:
                x1,y1=self.radius+(self.radius-10)*m.cos(i*m.pi/180),self.radius-(self.radius-10)*m.sin(i*m.pi/180)
                canvas.create_line(x1,y1,self.radius+self.radius*m.cos(i*m.pi/180),self.radius-self.radius*m.sin(i*m.pi/180),fill="#acace6",width=2)
            if(i>=90):
                q=+10
                u=q
            else:
                q=10
                u=0
        self.needle=canvas.create_line(self.radius,self.radius,self.radius,20,fill=needlecolor,width=2)
        canvas.create_oval(self.radius-30,self.radius-30,self.radius+30,self.radius+30,fill="#e936a7")
