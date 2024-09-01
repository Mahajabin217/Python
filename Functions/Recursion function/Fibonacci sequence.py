# How Fibonacci Sequence Works Using Recursion:

def fibo(n):
    # Base case:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case:
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(6))   

# Output: 8
