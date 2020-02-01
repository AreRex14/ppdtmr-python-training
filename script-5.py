# String Formatting

name = "Arif"
print("Hello, %s!" % name)

age = 25
print("%s is %d years old" % (name, age))

# any object which is not a string can be formatted using %s operator too
mylist = [1,2,3]
print("A list: %s" % mylist)

# exercise - You will need to write a format string which prints 
# out the data using the following syntax: Hello Guido Rossum. 
# Your current balance is $150.33.

data = ("Guido", "Rossum", 150.33)
format_string = "Hello"

# print(format_string % data)

# solution

data = ("Guido", "Rossum", 150.33)
format_string = "Hello %s %s. Your current balance is $%s"

print(format_string % data)