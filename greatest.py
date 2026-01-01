a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))
if a>=b and a>=c:
        print("maximum: ",a)
elif b>=a and b>=c:
        print("maximumn: ",b)
else:
        print("maximum: ",c)
if a<=b and a<=c:
        print("minimum: ",a)
elif b<=a and b<=c:
        print("minimumn: ",b)
else:
        print("minimum: ",c)