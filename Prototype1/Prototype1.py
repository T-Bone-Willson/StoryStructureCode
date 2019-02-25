#Empty List to contain user input
UserChoice = []

#Goes through C Branch options
def Cdecision(RootChoice):
    ops = True #variable was global, but made it local due to "UnboundLocalError"
    while ops:
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
                            ops = False
                            #break
                            print(UserChoice)
        else:
            ops = False
            print("Sorry You're not a winner")

#Presents user with Root choices of a, b, or c. Dependent on choice, will call it's associated Function
RootChoice = input("Choose a, b or c: ")
if RootChoice == "a":
    print("A Branch is not made yet!")
elif RootChoice == "b":
    print("B Branch is not made yet!")
elif RootChoice == "c":
        Cdecision(RootChoice)
else:
    print("SORRY! Invalid choice!")
