#factorial with recursion

x=int(input("enter the number to calculate factorial: "))
def fact(x):
    if(x==0 or x==1):
        return 1
    else:
        return x*fact(x-1)
print("factorial of number is: ",fact(x))

#factorial with iteration

n = int(input("enter the number to calculate factorial: "))
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
print("the factorial of entered number is:", factorial(n))
