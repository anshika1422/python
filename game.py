import math
import random
n=random.randint(1,20)
#print(n)
for x in range(7):
 guess=int(input("enter your guess from 1 to 20 "))
 if(guess<n):
  print("oops!!your guess is less than the answer")
 elif(guess>n):
  print("oops!1 your guess is greater than the answer")
 else:
  print("yay!! right answer! you won :)")
  break

if(x==6):
 print("GAME OVER")


 
