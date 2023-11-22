#thisIsMyString = "any string value"
#thisIsMyString = 'Any String value'

#print(len(thisIsMyString))
#print(len(thisIsMyString.split(" ")))

#print(thisIsMyString.lower())

#print(thisIsMyString.upper())

#if thisIsMyString.lower() == "any string value":
    #print("true")

#myList = thisIsMyString.split(" ")
#print(myList)
#print(thisIsMyString.split(" "))

#thisIsMyString = thisIsMyString.replace("Any"," Everything")
#print(thisIsMyString)

#thisIsMyString = thisIsMyString.replace("value","")
#print(thisIsMyString.strip())
#print(thisIsMyString[0])


thisIsMyInt = 2345
thisIsmyFloat = 2345.423
thisIsMyComplex1 = 2 + 25j
thisIsMyComplex2 = 2 + 25j
sum = thisIsMyComplex1 + thisIsMyComplex2
#print(sum)
#prod = thisIsMyComplex1 * thisIsMyComplex2
#print(prod)

thisIsMyIntA = 25
thisIsMyIntB = 30
sum = thisIsMyIntA + thisIsMyIntB
diff = thisIsMyIntA - thisIsMyIntB
prod = thisIsMyIntA * thisIsMyIntB
qou = thisIsMyIntA / thisIsMyIntB
#print("Sum : " + str(sum) + "\ndiff : " + str(diff) + "\nprod :  "+str(prod) + "\nqou : " +str(qou))
reminder = thisIsMyIntA % thisIsMyIntB
#print(reminder)

#print(thisIsMyString[0])
#print(thisIsMyString[1])
#print(thisIsMyString[2])
#print(thisIsMyString[3])
#print(thisIsMyString[4])
#print(thisIsMyString[5])

print("Please enter your name")
#myName = input()
#print("Hello, Good Morning Sir : " + myName)
print("Hello, Good Morning Sir : " + input())

print("Please Enter first number to add")
firstNum = int(input().replace(" ", ""))
print("Please Enter second number to add")
secNum = int(input().replace(" ", ""))
SUM = firstNum + secNum
print("The SUM is : " + str(sum))


myString = "hello world"
print(myString)
#myString = myString.strip()

#myString = myString.strip("hello")
#print(myString)
#myString = myString.replace("world", "jopay")
#print(myString)
myString = myString.replace("hello", "hi")
#print(myString)

#myString = myString.replace(input(), input())
#print(myString)
print(len(myString))
print(myString[1])

print(myString.upper())
print(myString.lower())


myString = "+960-586-3741"
print(myString[1])
print(myString[-1])

''' 
thisIsMyList = myString.split("-")
print(thisIsMyList)
print(len(thisIsMyList))
print(thisIsMyList[0])
print(thisIsMyList[1])
print(thisIsMyList[2])
thisIsMyList[1] = "111"
print(thisIsMyList)
#thisIsMyList[3] = "222" #out of range or index error
#print(thisIsMyList)
#thisIsMyList.append("1234")
#print(thisIsMyList)
thisIsMyList.insert(0, "0000")
print(thisIsMyList)

'''

thisIsAlist = ["asfje", 56, False, 56] #mutable
thisIsATuple = ("asfje", 56, False, 56, 56)#immutable
print(thisIsAlist)
print(thisIsATuple)
print(thisIsAlist.count(56))
print(thisIsATuple.count(56))



thisIsADictionary = {"name" : "Andrei Marceno", "age" : 19, "birthday" : "09-12-2004", "address" : "romblon"}
print(thisIsADictionary["name"])

thisIsADictionary = {"name" : {"first name" : "Andrei", "last name" : "Marceno"}, "age" : 19, "birthday" : "09-12-2004", "address" : "romblon"}
print(thisIsADictionary["name"])

FullNameDict = thisIsADictionary["name"]
print(FullNameDict["last name"])
print(FullNameDict["first name"])

thisIsADictionary = {"name" : {"first name" : "Andrei", "last name" : "Marceno"}, "hobbies" : ["basketball", "ball", "soccer"]}
#print(thisIsADictionary["hobbies"])
#print(thisIsADictionary["hobbies"][0])
#print(thisIsADictionary["hobbies"][1])
#print(thisIsADictionary["hobbies"][2])

thisIsASetA = {"hello", "byee", "goods"}
thisIsASetB = {"chill", "goo", "all"}
print(thisIsASetA.intersection(thisIsASetB))


#[] list
#{} value1, value2... set
#{} key1 : value1, key2 : ... dictionaru



#function
#print()
#len()
#int()
#input()

def addtwoNumbers(a, b):
    sum = a + b
    return sum

#print("please enter number to add")
#a = int(input())
#print("please enter number to add")
#b = int(input())
#mysum = addtwoNumbers(a, b)
#print(mysum)


#print(addtwoNumbers(5,10))

def divtwonumber(a, b) :
    reminder = a % b
    return reminder

def multiply(a, b) :
    prod = a * b
    return prod

def qout(a, b) :
    qout = a / b


print(divtwonumber(5, 25))
print(multiply(5, 25))
print(qout(5, 25))


'''
name  = "magic jhonson"
if name  == "luka doncic":
    print("basketball player")
    print("here!")


if name == "luka kurucs":
    print("basketball player")
if "luka" in name:
    print("he is luka")
elif "luka" in name:
    print("he is him")
else:
    print("here is else part")



age = int(input()) #string to integers
nationality = (input() #string to integers
yearsOfResidency = int(input())

if age >= 18 and yearsOfResidency >= 1 and nationality == "filipino":
    print("legal to vote")
elif age >= 18 and yearsOfResidency >= 1 and "filipino" in nationality:
    print("legal to vote with additional requirement")
else:
     print("not legal to vote")

if age <= 18 or age >= 60:
    print("may discount")

age = int(input())
if age != 13 and age != 25:
    print("allowed numbers")
else:
    print("not allowed numbers")

if (age <= 12 or age > 12) and (age <= 25 or age > 26):
    print("allowed")
else:
    print("not allowed")
'''
# == equal
# != not equal
# >= greater than or equal
#> greater than
# < less than
# <= less than or equal
# in -> if included
#


listOfCar = ["toyota", "hyundai", "honda"]
print("enter your car manufacturer")
mycar = input()

print("enter your car model year")
mycaryearmodel = int(input())

if mycar in listOfCar and mycaryearmodel > 2010:
    print("qualified")
else:
    print("not qualified")

if mycar in listOfCar:
    print("pre qualified")
    if mycaryearmodel > 2010:
        print("qualified")
    else:
        print("subject for inspection")
else:
    print("not qualified at all")



mystring = ""
if mystring == None:
    print("this is null")
elif mystring == "":
    print("this is empty")


grade = 92

if grade > 95:
    print("uno")
elif grade > 92:
    print("1.5")
elif grade > 85:
    print("tres")



#switch statement
fruits = input()
ripeness = input()

match fruits:
    case "banana":
        match ripeness:
            case "ripe":
                print("yellow")
            case "not ripe":
                print("green")
    case "apple":
            if ripeness == "ripe":
                print("red")
            else:
                print("green")
    case "grapes":
        print("indigo")
    case _:
        print("green")



 #infinite loop
for counter in iter(int,1): #for(int counter = 0; x <10; x++ {}
    userInput = int(input("enter AGE"))
    if userInput >= 18:
        print("not minor")
    else:
        print("minor")


#range loop
for counter in range(0,10): #for(int counter = 0; x <10; x++ {}
    userInput = int(input("enter AGE"))
    if userInput >= 18:
        print("not minor")
    else:
        print("minor")



import time

for counter in range(0,10): #for(int counter = 0; x <10; x++ {}
    signal = input()
    time.sleep(1)
    if signal == "500 error":
        print("retrying")
    elif signal == "200 ok":
        print("successfully connected")
        break

print("congratulation!")



import time
listOfCars = ["toyota", "suzuki", "hyundai", "honda", "others"]

for car in listOfCars:
    if "dai" in car:
        print(car + " is containing the word dai")
    else:
        print(car + "not containing the word dai")

profile = {"name" : "toyota", "age" : 5, "car" : "honda", "address": "manila"}
for key in profile:
    print(key + " -> " + str(profile[key]))

mystring = "aldeenvro"

for letra in mystring:
    print(letra)