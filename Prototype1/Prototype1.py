#Empty List to contain user input
UserChoice = []

#Goes through C Branch options
def Cdecision(RootChoice):
    opsC = True #variable was global, but made it local due to "UnboundLocalError"
    while opsC:
        choice = input("You can choose 'c': ")
        if choice == "c":
            UserChoice.append(choice)
            print(UserChoice)
            if UserChoice[-1] == "c":
                choice = input("You can choose 'c1': ")
                UserChoice.append(choice)
                print(UserChoice)
                if UserChoice[-1] == "c1":
                    choice = input("You can choose 'c2': ")
                    UserChoice.append(choice)
                    print(UserChoice)
                    if UserChoice[-1] == "c2":
                        choice = input("You can choose 'c3': ")
                        UserChoice.append(choice)
                        print(UserChoice)
                        if UserChoice[-1] == "c3":
                            #print(UserChoice)
                            opsC = False
                            #break
                            print(UserChoice)
        else:
            opsC = False
            print("Sorry You're not a winner")

#Goes through B Branch options
def Bdecision(RootChoice):
    opsB = True
    while opsB:
        choice = input("You can choose 'b': ")
        if choice == "b":
            UserChoice.append(choice)
            print(UserChoice)
            if UserChoice[-1] == "b":
                choice = input("You can choose 'b1' or 'b2': ")
                UserChoice.append(choice)
                print(UserChoice)
                if UserChoice[-1] == "b1":
                    choice = input("You can choose 'ab1': ")
                    UserChoice.append(choice)
                    print(UserChoice)
                elif UserChoice[-1] == "b2":
                    choice = input("You can choose 'b3': ")
                    UserChoice.append(choice)
                    print(UserChoice)
                if UserChoice[-1] == "ab1":
                    choice = input("You can choose 'ab2': ")
                    UserChoice.append(choice)
                    print(UserChoice)
                elif UserChoice[-1] == "b3":
                    choice = input("You can choose 'b4': ")
                    UserChoice.append(choice)
                    print(UserChoice)
                if UserChoice[-1] == "ab2" or UserChoice[-1] == "b4":
                    opsB = False
                    print(UserChoice)

        else:
            opsB = False
            print("You put in the wrong input man")


#Presents user with Root choices of a, b, or c. Dependent on choice, will call it's associated Function
RootChoice = input("Choose a, b or c: ")
if RootChoice == "a":
    print("A Branch is not made yet!")
elif RootChoice == "b":
    Bdecision(RootChoice)
elif RootChoice == "c":
        Cdecision(RootChoice)
else:
    print("SORRY! Invalid choice!")
