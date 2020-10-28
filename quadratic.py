print("_ _ _ _ _ _")
print("Quadratic Program")
print("_ _ _ _ _ _")
a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))
d=b*b-(4*a*c)
print(d)
if(d>0):
        x1=(-b-(d**(0.5)))/(2*a)
        x2=(-b+(d**(0.5)))/(2*a)
        print("x1= ",x1," x2= ",x2)
elif(d==0):
          x=-b/(2*a)
          print("x= ",x)
else:
    print("Roots are complex")
        
