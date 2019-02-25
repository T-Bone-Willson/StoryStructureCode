


#Empty List for choices that user makes. Appended onto here
#UserChoice = []
#List of choices that can be made
#choices = ['a', 'a1', 'a2', 'a3', 'a4', 'a5', 'b', 'b1', 'b2', 'b3', 'b4', 'ab1', 'ab2', 'c', 'c1', 'c2', 'c3']
#################################################################

#Empty List to contain user input
UserChoice = []

#Goes through C options
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
if RootChoice == "c":
    Cdecision(RootChoice)

    # TEST WORKED - Can Now commit to Prototype-1 branch without Atom causing Run/Compiling errors.
