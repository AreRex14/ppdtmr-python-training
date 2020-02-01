# Conditions

x = 5
print(x == 2)
print(x == 5)
print(x < 7)

city = "Sunway City"
country = "Malaysia"
if city ==  "Sunway City" and country == "Malaysia":
	print("You live at %s" % city + " in %s" % country)

if city == "Sunway City" or city == "Sunway Boulevard":
	print("You live either in %s" % city + " or Sunway Boulevard.")

# in operator
if city in ["Sunway Boulevard", "Sunway District", "Sunway City"]:
	print("Your city is available.")

# is operator
x = [1,2,3]
y = [1,2,3]
print(x == y)
print(x is y)

# not operator
print(not False)
print((not False) == (False))

# EXERCISE > Change the variables in the first section, so that each if statement resolves as True.

# # change this code
# number = 10
# second_number = 10
# first_array = []
# second_array = [1,2,3]

# if number > 15:
#     print("1")

# if first_array:
#     print("2")

# if len(second_array) == 2:
#     print("3")

# if len(first_array) + len(second_array) == 5:
#     print("4")

# if first_array and first_array[0] == 1:
#     print("5")

# if not second_number:
#     print("6")


# SOLUTION

# change this code
number = 16
second_number = 10
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number == False:
    print("6")
