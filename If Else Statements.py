 # code order matters
 # cant do print(a) then a = 1

a = int(input("Enter in a number: "))
b = int(input("Enter another number: "))

if(a>b):
    print(str(a) + " is bigger than " + str(b))
    # we can add as many lines of code that we want here
    # note use tab to indent code to keep all indentations the same
elif(a==b):
    print(str(a) + " equals " + str(b))
else:
    print(str(b) + " is bigger than " + str(a))

# above we are getting in a console input from the user using input
# we change the variable type of the input we are getting by casting the input
# e.g as above we are casting the user input to type integer int(input())
# if elif else statement allows you to check if something is true or false using boolean logic


# lets make a bmi calculator

    # get inputs from user
height_m = float(input("Enter in Height in metres: "))
weight_kg = float(input("Enter in Weight in kg: "))

    # calculate user bmi
bmi = weight_kg/(height_m**2)
print("bmi: " + str(bmi))

    # find out if user healthy or not
if(bmi <= 18):
    print("underweight")
elif(18< bmi <= 24):
    print("healthy")
elif(24 <bmi <=29):
    print("overweight")
elif(29<bmi<=39):
    print("obese")
else:
    print("extremely obese")

# above we have created a bmi calculator using boolean logic