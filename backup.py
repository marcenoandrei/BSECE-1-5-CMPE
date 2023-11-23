for counter in iter(int,1): #for(int counter = 0; x <10; x++ {}
    userInput = int(input("enter AGE: "))
    if userInput >= 18:
        print("not minor")
    else:
        print("minor")