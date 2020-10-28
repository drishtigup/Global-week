from tkinter import *
#------------------------------------------------
def calculate():
    x1=float(e1.get())
    y1=float(e2.get())
    x2=float(e3.get())
    y2=float(e4.get())
    d=(((x2-x1)**2)+((y2-y1)**2))**0.5
    S.set("Distance is "+str(d)+" m")
#------------------------------------------------
#    Main Program
#------------------------------------------------
window=Tk()
window.title("Distance")

l1=Label(window,text="Longitude 1:")
l1.grid(row=0,column=0)
e1=Entry(window,bg="pink")
e1.grid(row=0,column=1)

l2=Label(window,text="Latitude 1:")
l2.grid(row=1,column=0)
e2=Entry(window,bg="pink")
e2.grid(row=1,column=1)

l3=Label(window,text="Longitude 2:")
l3.grid(row=2,column=0)
e3=Entry(window,bg="pink")
e3.grid(row=2,column=1)

l4=Label(window,text="Latitude 2:")
l4.grid(row=3,column=0)
e4=Entry(window,bg="pink")
e4.grid(row=3,column=1)

S=StringVar()
l6=Label(window,textvariable=S)
l6.grid(row=5,column=1)

b1=Button(window,text="Quit",command=quit)
b1.grid(row=4,column=0)

b2=Button(window,text="Calculate",command=calculate)
b2.grid(row=4,column=2)


window.mainloop()
