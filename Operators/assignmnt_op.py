#How Assignment Operators(=, +=, -=, *=, /=, %=, //=, **=, &=, /=, |=, ^=, >>=, <<=, :=) Work:

a = 5
a += 3
print(a)

b = 5
b -= 3
print(b)

c = 5
c *= 2
print(c)

d = 10
d /= 5
print(d)

e = 5
e %= 2
print(e)

f = 3
f **= 2
print(f)

g = 15
g //= 4
print(g)

# AND operator(&):
h = 5
h &= 3
print(h)

# OR operator(|):
i = 5
i |= 3
print(i)

# XOR operator(^):
j = 5
j ^= 3
print(j)

# Right-shift operator(>>):
k = 5
k >>= 3
print(k)

# Left-shift operator(<<):
l = 5
l <<= 3
print(l)

# Walrus operator(:=):
m = 5
print(m := 3)

"""Output: 8
           2
           10
           2.0
           1
           9
           3
           1
           7
           6
           0
           40
           3  
"""