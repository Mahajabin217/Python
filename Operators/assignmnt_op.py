#How Assignment Operators(=, +=, -=, *=, /=, %=, //=, **=, &=, /=, |=, ^=, >>=, <<=, :=) Work:

a = 5
a += 3
print(a)
# Output: 8

b = 5
b -= 3
print(b)
# Output: 2

c = 5
c *= 2
print(c)
# Output: 10

d = 10
d /= 5
print(d)
# Output: 2.0

e = 5
e %= 2
print(e)
# Output: 1

f = 3
f **= 2
print(f)
# Output: 9

g = 15
g //= 4
print(g)
# Output: 3

# AND operator(&):
h = 5
h &= 3
print(h)
# Output: 1

# OR operator(|):
i = 5
i |= 3
print(i)
# Output: 7

# XOR operator(^):
j = 5
j ^= 3
print(j)
# Output: 6

# Right-shift operator(>>):
k = 5
k >>= 3
print(k)
# Output: 0

# Left-shift operator(<<):
l = 5
l <<= 3
print(l)
# Output: 40

# Walrus operator(:=):
m = 5
print(m := 3)
# Output: 3
