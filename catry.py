
num=int(input("enter range to check prime numbers "))
n=0
for i in range(2,num):

 for x in range(2,i):
  if (i % x) == 0: 
   break
 else:
  n=n+1
  print(i)
print("the total numbers of prime numbers in the range is",n)