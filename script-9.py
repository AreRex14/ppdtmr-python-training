# Functions

def greet_function():
	print("Hello from My Function!")

greet_function()

# receive arguments(variables passed from the caller to the function)
def greet_with_args(username, greeting):
	print("Hello, %s, from Greet Function!, I wish you %s" % (username, greeting))

greet_with_args('arif', 'great')

# may return a value to the caller
def sum_two_numbers(a, b):
	return a + b

result = sum_two_numbers(1060, 20)
print(result)

# call above functions as we want it
greet_with_args('afiq', 'well')
result = sum_two_numbers(10, 5)
print(result)
greet_function()

# EXERCISE >
# you'll use an existing function, and while adding your own to create a fully functional program.

#    1. Add a function named list_benefits() that returns the following list of strings: "More organized code", "More readable code", 
#		"Easier code reuse", "Allowing programmers to share and connect code together"

#    2. Add a function named build_sentence(info) which receives a single argument containing a string and returns a sentence starting with
#		the given string and ending with the string " is a benefit of functions!"

#    3. Run and see all the functions work together!

# # Modify this function to return a list of strings as defined above
# def list_benefits():
#     pass

# # Modify this function to concatenate to each benefit - " is a benefit of functions!"
# def build_sentence(benefit):
#     pass

# def name_the_benefits_of_functions():
#     list_of_benefits = list_benefits()
#     for benefit in list_of_benefits:
#         print(build_sentence(benefit))

# name_the_benefits_of_functions()

# SOLUTION >

# Modify this function to return a list of strings as defined above
def list_benefits():
    strings_list = ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]
    return strings_list
# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()