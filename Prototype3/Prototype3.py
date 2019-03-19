# users choice stored in an empty list.
UserChoice = []

################################################################
###                                                          ###
###              Adventure Branch Function Code              ###
###                                                          ###
################################################################

def A_Chain(RootChoice):
    UserChoice.append("a")
    choice = input("You can choose 'a1' or 'a2': ")
    if choice == "a1":
        UserChoice.append(choice)
        print(UserChoice)
        a1()
    elif choice == "a2":
        UserChoice.append(choice)
        print(UserChoice)
        a2()
    else:
        print("Test a1 and a2: Invalid Choice!")

def a1():
    choice = input("You can choose 'a3': ")
    if choice == "a3":
        UserChoice.append(choice)
        print(UserChoice)
        a3()
    else:
        print("Test a1()-a3: Invalid choice!")

def a2():
    choice = input("You can choose 'a3': ")
    if choice == "a3":
        UserChoice.append(choice)
        print(UserChoice)
        a3()
    else:
        print("Test  a2()-a3: Invalid choice!")

def a3():
    choice = input("You can choose 'a4': ")
    if choice == "a4":
        UserChoice.append(choice)
        print(UserChoice)
        a4()
    else:
        print("Test a4: Invalid choice!")

def a4():
    choice = input("You can choose 'a5': ")
    if choice == "a5":
        UserChoice.append(choice)
        print(UserChoice)
        a5()
    else:
        print("Test a5: Invalid choice!")

def a5():
    choice = input("You can choose 'a6': ")
    if choice == "a6":
        UserChoice.append(choice)
        print(UserChoice)
        a6()
    else:
        print("Test a6: Invalid choice!")

def a6():
    choice = input("You can choose 'a7': ")
    if choice == "a7":
        UserChoice.append(choice)
        print(UserChoice)
        a7()
    else:
        print("Test a7: Invalid choice!")

def a7():
    choice = input("You can choose 'a8': ")
    if choice == "a8":
        UserChoice.append(choice)
        print(UserChoice)
        a8()
    else:
        print("Test a8: Invalid choice!")

def a8():
    # Checks to see if element "a2" exist in UserChoice List
    # If so, it means branch chains V10 and onwards are unlocked
    # If not, then branch chains a9, a13 and a14 are unlocked
    if 'a2' in UserChoice:
        print("a2 element search in list works")
    else:
        print("NOPE")












################################################################
###                                                          ###
###                    Start of Program                      ###
###                                                          ###
################################################################

#Presents user with Root choices of a, b, or c. Dependent on choice, will call it's associated Function
RootChoice = input("Choose a or v: ")
if RootChoice == "a":
    A_Chain(RootChoice) # Goes to A branch funtion chains
#elif RootChoice == "v":
#    V_Chain(RootChoice) # Goes to B branch function chains
else:
    print("SORRY! Invalid choice!") # error handler... kinda
