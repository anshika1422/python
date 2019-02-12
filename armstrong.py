n=int(input("enter a num"))
sum=0
m=n
while(m!=0):
 d=m%10
 f=d*d*d
 sum=sum+f
 m=m//10
 
if(n==sum):
 print("the number is armstrong")
else:
 print("the number is not armstrong")
