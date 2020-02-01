# Classes and Objects

# basic class
class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
	
class MyClass():
	variable = "hello"

	def function(self):
		print("This is a message inside a class.")		

myobjectx = MyClass() # assign above class(template) to an object

myobjectx.variable # access the variable inside the newly created object

print(myobjectx.variable)


myobjecty = MyClass() # create another object of the same class

myobjecty.variable = "assalamualaikum" # access the variable and change the value

# print out both values
print(myobjectx.variable)
print(myobjecty.variable)

# access object functions
myobjectx.function()

# EXERCISE > 
# Create two new vehicles called kereta1 and kereta2
# Set kereta1 to be a red convertible worth RM60,000.00 with a name of Fer
# and kereta2 to be a blue van named Jump worth RM10,000.00

# define the Vehicle class
# class Kenderaan:
#     nama = ""
#     jenis = "kereta"
#     warna = ""
#     harga = 5000.00
#     def penerangan(self):
#         str_penerangan = "%s adalah %s %s bernilai RM%.2f." % (self.nama, self.warna, self.jenis, self.harga)
#         return str_penerangan
# # your code goes here

# # test code
# print(kereta1.penerangan())
# print(kereta2.penerangan())


# SOLUTION >

class Kenderaan:
    nama = ""
    jenis = "kereta"
    warna = ""
    harga = 5000.00
    def penerangan(self):
        str_penerangan = "%s adalah %s %s bernilai RM%.2f." % (self.nama, self.jenis, self.warna, self.harga)
        return str_penerangan

kereta1 = Kenderaan()
kereta2 = Kenderaan()

kereta1.warna = "Merah"
kereta1.harga = 60000
kereta1.nama = "Fer"

kereta2.jenis = "van"
kereta2.warna = "Biru"
kereta2.harga = 10000
kereta2.nama = "Jump"

print(kereta1.penerangan())
print(kereta2.penerangan())