#prime with recursion
def prime(n, i=2):
    if n <= 1:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return prime(n, i + 1)
num = int(input("Enter a number: "))
if prime(num):
    print(f"{num} is a Prime number")
else:
    print(f"{num} is Not a Prime number")


#prime without recursion
def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
n1 = int(input("Enter a number: "))
if prime(n1):
    print(f"{n1} is a Prime number")
else:
    print(f"{n1} is Not a Prime number")
