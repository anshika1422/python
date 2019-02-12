num=int(input("enter number to check "))
c=0
if(num<0): 
 print("prime cannot be checked number is negative")
elif(num==1):
 print("neither prime nor composite")
 
 
else:
 for i in range(2,num):
   if(num%i==0):
    c=c+1
 if(c!=0):
  print("the number is not prime")
 else:
  print("the number is prime")