ete=int(input("enter marks of end term out of 70 "))
mte=int(input("enter marks of mid term out of 40 "))
ca=int(input("enter the CA marks out of 100 "))
atten=int(input("enter the attendance out of 5 "))
etew=round((ete/70)*50)
mtew=round((mte/40)*20)
caw=round((ca/100)*25)
print("ete marks out of 50 is ",etew)
print("mte marks out of 20 is ",mtew)
print("CA marks out of 25 is ",caw)
print("attendance marks out of 5 is",atten)
totalmarks=etew+mtew+caw+atten
percent=(totalmarks/100)*100
cgpa=percent/10
print("the percentage of the subject CAP588 is",percent,"%")
print("the cgpa for the subject CAP588 is",cgpa)
