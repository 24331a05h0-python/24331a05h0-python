p=float(input("enter the principal amount: "))
r=float(input("enter the rate of interest: "))
t=float(input("enter the time of yrs: "))
a=p*(1+(r/100))**(t)
ci=a-p
print("compound interest is: ",ci)
