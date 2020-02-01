# define an integer
firstint = 4
print(firstint)

# define a float
firstfloat = 4.0
print(firstfloat)
firstfloat = float(4)
print(firstfloat)

# define strings
firststring = 'hello'
print(firststring)
firststring = "hello"
print(firststring)

secondstring = "This isn't valid"
print(secondstring)

# execute simple operators on numbers and strings
a = 1
b = 2
c = a + b
print(c)

x = "hello"
y = "world"
result = x + " " + y
print(result)

# assignments simultaneously on one line
a, b = 3, 4
print(a, b)

# mixing operators between numbers and strings is not supported
a = 1
b = 2
c = "hello"
# print(a + b + c)

# exercise
# The target of this exercise is to create a string, an integer, and a floating point number. 
# The string should be named mystring and should contain the word "hello". 
# The floating point number should be named myfloat and should contain the number 10.0, 
# and the integer should be named myint and should contain the number 20.

# change this code
mystr = None
myfloat = None
myint = None

# testing code
if mystr == "hello":
	print("String: %s" % mystr)
if isinstance(myfloat, float) and myfloat = 10.0:
	print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
	print("Integer: %d" % myint)