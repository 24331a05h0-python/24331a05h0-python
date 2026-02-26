from functools import reduce

n = int(input("Enter number of elements: "))
elements = []

for i in range(n):
    value = int(input("Enter element: "))
    elements.append(value)

tup = tuple(elements)

tup_map = map(lambda x: x * x, tup)
print(list(tup_map))

tup_fltr = filter(lambda x: x % 2 == 0, tup)
print(list(tup_fltr))

tup_reduce = reduce(lambda x, y: x + y, tup)
print("Sum of elements:", tup_reduce)
