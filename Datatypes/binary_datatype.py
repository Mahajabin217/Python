# How Binary Datatype(bytes,bytearray,memoryview) work:

#How bytes work:
x = {1,30,40,100,200}
b = bytes(x)
print(type(b))

#Output: <class 'bytes'>
      
#How bytearray work:
x = {1,30,40,100,200}
b = bytearray(x)
b[1] = 50
print(type(b))
print(b[1])

#Output: <class 'bytearray'>
#        50

#How memoryview work:
x = memoryview(bytes(3))
print(x)
print(type(x))

#Output: <memory at 0x000001E9DC91C880>
#        <class 'memoryview'>