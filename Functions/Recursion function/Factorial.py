# How Factorial Works Using Recursion:

def fact(n):
    # Base case:
    if n == 0:
        return 1
    # Recursive case
    else:
        return n * fact(n-1)

print(fact(5))

# Output: 120