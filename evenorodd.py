n = int(input("Enter a number: "))
ecount = 0
ocount = 0
for i in range(1,n+1):
    if i % 2 == 0:
        print(f"{i} is even")
        ecount += 1
    else:
        print(f"{i} is odd")
        ocount += 1
print("\nTotal even numbers:", ecount)
print("Total odd numbers:", ocount)
