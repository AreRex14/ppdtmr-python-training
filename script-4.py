number = 1 + 2 * 3 / 4.0
print(number)

remainder = 11 % 3
print(remainder)

squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

helloworld = "hello" + " " + "world"
print(helloworld)

# multiplying strings to form a string with repeating sequence
lotsofgols = "gol!" * 5
print(lotsofgols)

mylist = ['a','b','c']
yourlist = ['d','e','f']
ourlist = mylist + yourlist
print(ourlist)

# forming a new lists with a repeating sequence
print([1,2,3] * 3)

# create two lists called x_list and y_list which containe 10 instances of the variables x and y respectively
# create a list called big_list too which containes the variables x and y, 10 times each

x = object()
y = object()

# TODO: change this code
x_list = [x]
y_list = [y]
big_list = []

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
    

# SOLUTION
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
	print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) ==10:
	print("Great!")