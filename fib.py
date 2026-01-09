def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

n = int(input("Enter the number of terms: "))

# Fibonacci using iteration
a, b = 0, 1
print("Fibonacci series using iteration:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

print("\nFibonacci series using recursion:")
# Fibonacci using recursion
for i in range(n):
    print(fib(i), end=" ")
