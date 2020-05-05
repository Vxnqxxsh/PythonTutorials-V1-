# While loop is a loop that continue to execute the code until the condition is no longer met
# A try except allows us to catch errors within the program and provide the user with an error message
# float is a type of variable that allows us to store decimal places



#Q1
print("Q1")
print("")
valid = False
while(valid == False):
    try:
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))

        valid = True
    except:
        print("can only enter in digits")

if (length == width):
    print("Yes, it's a square")
else:
    print("No, it's a rectangle")

#Q2
print("")
print("Q2")
print("")

valid = False
while(valid == False):
    try:
        num1 = int(input("Enter an integer: "))
        num2 = int(input("Enter an integer: "))
        valid = True
    except:
        print("can only enter in whole numbers")

if(num1>num2):
    print(num1)
elif(num1<num2):
    print(num2)
else:
    print("both numbers are the same")

#Q3
print("")
print("Q3")
print("")

valid = False

while(valid == False):
    try:
        quantity = int(input("How many items are required: "))
        valid = True
    except:
        print("can only enter in whole numbers")

cost = quantity*100

if(quantity>1000):
    cost = cost*0.9

print(cost)

#Q4
print("")
print("Q4")
print("")

valid = False

while(valid == False):
    try:
        marks = int(input("Enter in marks: "))
        if(marks > 100):
            print("marks cannot be over 100")
        else:
            valid = True
    except:
        print("can only enter in whole numbers")

result = ""
if(marks<25):
    result = "F"
elif(25<=marks<45):
    result = "E"
elif(45<=marks<50):
    result = "D"
elif(50<=marks<60):
    result = "C"
elif(60<=marks<80):
    result = "B"
else:
    result = "A"

print(result)

#Q5
print("")
print("Q5")
print ("")

valid = False

while(valid == False):
    try:
        num = float(input("enter in a number: "))
        valid = True
    except:
        print("can only enter in digits")

if(num<0):
    num = num*-1

print(num)

#Q6
print("")
print("Q6")
print ("")

valid = False

while(valid == False):
    try:
        classesHeld = int(input("enter in number of classes held: "))
        classesAttended = int(input("enter number of classes attended: "))
        if(classesAttended>classesHeld):
            print("classes attended cant be bigger than classes held")
        else:
            valid = True
    except:
        print("can only enter in whole numbers")

attendance = (classesAttended/classesHeld)*100

print(attendance)
if(attendance<75):
    print("The student is not allowed to sit the exam")
else:
    print("The student is allowed to sit the exams")

#Q7
print("")
print("Q7")
print ("")

validAge = False
validSex = False
validMartialStatus = False
age = 0
sex = ""
martialStatus = ""

while(validAge == False):
    try:
        age = int(input("Enter in user age: "))
        validAge = True
    except:
        print("Age can only be entered in digits and be a whole number")

while(validSex == False):
    try:
        sex = input("Enter in user sex M or F: ")
        if(sex == "M" or sex == "F"):
            validSex = True
        else:
            print("Sex can only be 'M' or 'F'")
    except:
        print("Sex can only be 'M' or 'F'")

while(validMartialStatus == False):
    try:
        martialStatus = input("Enter in martial status 'Y' or 'No' : ")
        if(martialStatus == "Y" or martialStatus == "N"):
            validMartialStatus = True
        else:
            print("Martial Status can only be 'Y' or 'N'")
    except:
        print("Martial Status can only be 'Y' or 'N'")

if(sex == "F"):
    print("can only work in urban areas")
else:
    if(20<=age<40):
        print("can work anywhere")
    elif(40<=age<60):
        print("can only work in urban areas")
    else:
        print("Error")

#Q8
print("")
print("Q8")
print ("")

numlen4 = str(input("Enter in a 4 digit number"))
numlen4 = numlen4[::-1]
print(numlen4)
