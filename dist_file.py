from tkinter import *
from math import *
from datetime import datetime,timedelta
from tkinter.ttk import Combobox
def degree(la1,lo1,la2,lo2):
    return(cal(radians(la1),radians(lo1),radians(la2),radians(lo2)))
def cal(la1,lo1,la2,lo2):
    R=6371*(10**3)
    x=(lo2-lo1)*cos((la1+la2)/2)
    y=la2-la1
    d=sqrt(pow(x,2)+pow(y,2))*R
    d=round(d,3)
    return d
def time(t):
    T=float(t[-1])-float(t[1])
    time=T*(10**(-3))
    h=time//3600
    v=time%3600
    m=v//60
    s=v%60
    return(str(h)+"hrs "+str(m)+"m "+str(s)+"s")
    
    
    return T
def speed(d,t):
    T=float(t[-1])-float(t[1])
    time=T*(10**(-3))
    s=d/time
    s=round(s,3)
    return s
def input():
    a=[[],[]]
    t=[]
    d=0
    fname=cb.get()
    f=open(fname,"r")
    for l in f.readlines():
        L=l.split(",")
        a[0].append((L[0]))
        a[1].append(L[1])
        t.append(L[-1])
    for i in range(1,len(a[0])-1):
        la1=float(a[0][i])
        lo1=float(a[1][i])
        la2=float(a[0][i+1])
        lo2=float(a[1][i+1])
        d=d+degree(la1,lo1,la2,lo2)
    V.set(str(d))
    T=time(t)
    g.set(str(T))
    S=speed(d,t)
    h.set(str(S))
    f.close()
window=Tk()
window.title("GPS Data")
l1=Label(window,text="File name:")
l1.grid(row=0,column=0)
var = StringVar()
var.set("one")
data=("tracesGPS1.csv", "tracesGPS2.csv", "tracesGPS3.csv", "tracesGPS4.csv")
cb=Combobox(window, values=data)
cb.grid(row=0,column=1)
#e1=Entry(window,bg="pink")
#e1.grid(row=0,column=1)
l2=Label(window,text="Distance:")
l2.grid(row=1,column=0)
l3=Label(window,text="Time:")
l3.grid(row=2,column=0)
l4=Label(window,text="Speed:")
l4.grid(row=3,column=0)
l5=Label(window,text="Meters")
l5.grid(row=1,column=2)
l6=Label(window,text="")
l6.grid(row=2,column=2)
l7=Label(window,text="m/s")
l7.grid(row=3,column=2)
b1=Button(window,text="Quit",command=quit)
b1.grid(row=4,column=0)
b2=Button(window,text="Calculate",command=input)
b2.grid(row=4,column=2)
V=StringVar()
l8=Label(window,textvariable=V)
l8.grid(row=1,column=1)
g=StringVar()
l8=Label(window,textvariable=g)
l8.grid(row=2,column=1)
h=StringVar()
l8=Label(window,textvariable=h)
l8.grid(row=3,column=1)
window.mainloop()
