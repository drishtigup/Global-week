from tkinter import *
#------------------------------------------------
def calculate():
    a=int(e1.get())
    b=int(e2.get())
    c=int(e3.get())
    d=b*b-(4*a*c)
    print(d)
    V.set(str(d))
    if(d>0):
        x1=(-b-(d**(0.5)))/(2*a)
        x2=(-b+(d**(0.5)))/(2*a)
        S.set(str("x1="+str(x1)))
        W.set(str("x2="+str(x2)))
    elif(d==0):
          x=-b/(2*a)
          S.set("x="+str(x))
    else:
        S.set(str("Roots are complex"))
#------------------------------------------------
#    Main Program
#------------------------------------------------
window=Tk()
window.title("Double")

l1=Label(window,text="a:")
l1.grid(row=0,column=0)
e1=Entry(window,bg="pink")
e1.grid(row=0,column=1)

l2=Label(window,text="b:")
l2.grid(row=1,column=0)
e2=Entry(window,bg="pink")
e2.grid(row=1,column=1)

l3=Label(window,text="c:")
l3.grid(row=2,column=0)
e3=Entry(window,bg="pink")
e3.grid(row=2,column=1)

l4=Label(window,text="Delta:")
l4.grid(row=3,column=0)

V=StringVar()
l5=Label(window,textvariable=V)
l5.grid(row=3,column=1)

S=StringVar()
l6=Label(window,textvariable=S)
l6.grid(row=5,column=1)

W=StringVar()
l7=Label(window,textvariable=W)
l7.grid(row=6,column=1)

b1=Button(window,text="Quit",command=quit)
b1.grid(row=4,column=0)

b2=Button(window,text="Calculate",command=calculate)
b2.grid(row=4,column=2)


window.mainloop()
