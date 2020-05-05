print("Hello World")
# this outputs hello world to the console
# the print() function allows us to output anything to the console


print("printing integer " +str(3))
# to print an integer as well as a string we cast the int using str(int)

# we will now look at variables
# there are many types of variables for now we will work with integers and strings
# numbers are integers (whole numbers)
# strings are sets of characters

a = 1 # a = 1 means a is type integer
b = 2 # b = 2 means b is type integer

print(a)
print(b)

# A variable is a container for data

# how to swap variables

    # solution 1
    # here we have to temporary variables which hold v1 and v2
    # this allows us to say that v1 = v2 and v2 = v1 (make a swap)
v1 = "First String"
v2 = "Second String"
print("before")
print(v1)
print(v2)

tempv1 = v1
tempv2 = v2

v1 = tempv2
v2 = tempv1

print("after")
print(v1)
print(v2)

    # solution 2
    # here we are doing the same but with one temp var
    # we say temp = v1, allowing us to have two v1
    # now v1 = v2 with one v1 still existing that allows us to say v2 = temp thus swap is complete
v1 = "First String"
v2 = "Second String"

print("before")
print(v1)
print(v2)

temp = v1
v1 = v2
v2  = tempv1

print("after")
print(v1)
print(v2)


