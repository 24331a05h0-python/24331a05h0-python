lst = []
n = int(input("Enter number of tuples: "))
for i in range(n):
    a = int(input("Enter first element: "))
    b = int(input("Enter second element: "))
    lst.append((a, b))
lst.sort(key=lambda x: x[-1])
print(lst)
