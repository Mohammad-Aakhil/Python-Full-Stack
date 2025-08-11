#if statement
age = 12

if(age>18):
    print("You can drive")
    print("Thank you ")

print("End of program")

#if else statement
age = int(input("Enter your age: "))

if(age>18):
    print("You can drive")
else:
    print("You cannot drive")

print("End of program")


#if elif statement
age = int(input("Enter your age: "))

if(age>18):
    print("You can drive")
elif(age == 18):
    print("Lets schedule an interview")
elif(age == 0):
    print("Hey you are just born")
else:
    print("Sorry you cannot drive")