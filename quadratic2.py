#Quadratic equation
import math
a=int(input("enter value of a "))
b=int(input("enter value of b "))
c=int(input("enter value of c "))
d=(b*b)-(4*a*c)
if(d==0):
 print("the roots are real and equal")
 r1=(-b+math.sqrt(d))/(2*a)
 print("the root 1 is",r1)

elif(d<0):
 print("the roots are complex and different")
else:
 print("there will be 2 real and different roots")
 r1=(-b+math.sqrt(d))/(2*a)
 r2=(-b-math.sqrt(d))/(2*a)
 print("the root 1 is",r1)
 print("the root 2 is",r2)
 