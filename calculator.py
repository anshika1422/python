ch=int(input("enter choice 1:add/ 2:subtract/3: multiply/4:divide/5:modulus/6:power "))
num1=int(input("input number 1 "))
num2=int(input("input number 2 "))
if ch==1:
 print("the sum of the numbers is",num1+num2)
elif ch==2:
 print("the subtract of the numbers is",num1-num2)
elif ch==3:
  print("the product of the numbers is",num1*num2)
elif ch==4:
  print("the divide of the numbers is",num1/num2)
elif ch==5:
  print("the modulus of the numbers is",num1%num2)
elif ch==6:
   print("the exponent of the numbers is",num1**num2)
else:
 print("wrong choice")
