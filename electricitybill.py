units=int(input("enter the units of electricity used "))
if units<=100:
 bill=units*5.95
else:
 a=100*5.95
 b=units-100
 c=b*6.95
 bill=a+c
print("the bill of ",units,"units is",bill)