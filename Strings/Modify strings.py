# How to Modify Strings:

# Using upper() method, we can return the strings in upper case:
s = "hello,world!"
print(s.upper())
# Output: HELLO,WORLD!

# Using lower() method, we can return the strings in lower case:
s = "Hello,World!"
print(s.lower())
# Output: hello,world!

# Using strip() method, we can remove whitespace from the start & end:
s = "Hello,World!  "
print(s.strip())
# Output: Hello,World!

# Using replace() method, we can replace one string with another:
s = "Hello,World!  "
print(s.replace("World","Ritu"))
# Output: Hello,Ritu!

# Using split() method, we can split the strings into sub-strings:
s = "Hello,World!"
print(s.split(","))
# Output: ['Hello', 'World!']