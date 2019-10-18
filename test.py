import math as m 
from array import * 
b=input("Введите угол ") 
b=float(b) 
a = b * m.pi / 180 
v0=input("Введите скорость ") 
v0=float(v0) 
n=input("Введите n ") 
n=int(n) 
g = 9.81 
t = v0*m.sin(2*a)/m.cos(a)/g 
h = t/n 
y2 = v0 * m.sin(a) 
x2 = v0 * m.cos(a) 
x1=0 
y1=0 
x=[] 
y=[] 
x.append(x1) 
y.append(y1) 
for i in range(n): 
    x.append(x[i]) 
    x[i] = x[i-1] + h*x2 
    y.append(y[i]) 
    y[i] = y[i-1] + h*y2  
    y2 = y2 - h*g 
for i in range(n): 
    print (x[i], end = " ") 
print () 
for i in range(n): 
    print (y[i], end = " ")
