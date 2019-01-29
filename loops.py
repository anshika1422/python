#this is a program for for loop
i=0
limit=int(input("enter the number for the table "))
for i in range(1,11):
 #print(i,"x",limit,"=",(i*limit))
 k=i*limit
 print("{}X{}={}".format(i,limit,k))
