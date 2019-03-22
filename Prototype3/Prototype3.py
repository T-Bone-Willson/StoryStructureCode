# users choice stored in an empty list.
UserChoice = []

# Global Variables for Node definition
a1 = "a1: The elixir is an object"
a2 = "a2: The elixir is a person"

################################################################
###                                                          ###
###              Adventure Branch Function Code              ###
###                                                          ###
################################################################

# Start of Adventure branch chain. Triggerd by User making choice "a" at start of program.
def A_Chain(RootChoice):
    UserChoice.append("a") # Adds Branch root to List
    # For reasons I don't fully understand, I have to state it as global
    # Even though it has been declared global, outside the scope of the function
    global a1
    global a2
    # Then reassign the value to the "global a1" or "global a2"
    # This is duplicating the code and it's not what I originally intended.
    a1 = "a1: The elixir is an object"
    a2 = "a2: The elixir is a person"
    print(a1)
    print(a2)
    choice = input("You can choose 'a1' or 'a2': ")
    if choice == "a1": # player needs to input this in order to proceed through branch
        UserChoice.append(choice)
        print(UserChoice)
        a1()
    elif choice == "a2": # Will unlock a2() function/branch.
        UserChoice.append(choice)
        print(UserChoice)
        a2()
    else:
        print("Test a1 and a2: Invalid choice!")

# a1() function means the elixir is not a person.
# by having element "a1" in UserChoice List, it means that
# Function a9() will be unlocked automaticaly
# but will close off Function a10()
def a1():
    choice = input("You can choose 'a3': ")
    if choice == "a3":
        UserChoice.append(choice)
        print(UserChoice)
        a3()
    else:
        print("Test a1()-a3: Invalid choice!")

# a2() function means the elixir is a person.
# by having element "a2" in UserChoice List, it means that
# Function a10() will be unlocked automaticaly
# but will close off Function a9()
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
    # If so, it means branch chains a10 and onwards are unlocked
    if 'a2' in UserChoice:
        choice = input("You can choose 'a10': ")
        if choice == "a10": # Goes back to checking if input condition has been met
            UserChoice.append(choice)
            print(UserChoice)
            a10()
    # Checks to see if element "a1" exist in UserChoice List
    # If so, then branch chains a9, a13 and a14 are unlocked
    elif 'a1' in UserChoice:
        choice = input("You can choose 'a9': ")
        if choice == "a9": # Goes back to checking if input condition has been met
            UserChoice.append(choice)
            print(UserChoice)
            a9()
    else:
        print("Test a9 OR a10: Invalid choice!")

# Adventure Branch with no possible love interest is operated from this chain
def a9():
    choice = input("You can choose 'a13': ")
    if choice == "a13":
        UserChoice.append(choice)
        print(UserChoice)
        print("You have reached the end of this Branch!")
    else:
        print("Test a13: Invalid choice!")

# Adventure Branch with possible love interest is operated from this chain
def a10():
    choice = input("You can choose 'a11' or 'a12': ")
    if choice == "a11":
        UserChoice.append(choice)
        print(UserChoice)
        a11()
    elif choice == 'a12':
        UserChoice.append(choice)
        print(UserChoice)
        a12()
    else:
        print("Test a11 and a12: Invalid choice!")

def a11():
    choice = input("You can choose 'a13' or 'a14': ")
    if choice == "a13":
        UserChoice.append(choice)
        print(UserChoice)
        print("You have reached the end of this Branch!")
    elif choice == 'a14':
        UserChoice.append(choice)
        print(UserChoice)
        print("You have reached the end of this Branch!")
    else:
        print("Test a11()-a13 and a11()-a14: Invalid choice!")

def a12():
    choice = input("You can choose 'a13' or 'a14': ")
    if choice == "a13":
        UserChoice.append(choice)
        print(UserChoice)
        print("You have reached the end of this Branch!")
    elif choice == 'a14':
        UserChoice.append(choice)
        print(UserChoice)
        print("You have reached the end of this Branch!")
    else:
        print("Test a12()-a13 and a12()-a14: Invalid choice!")

################################################################
###                                                          ###
###                Quest Branch Function Code                ###
###                                                          ###
################################################################

################################################################
###                         ACT 1                            ###
################################################################

def Q_Chain(RootChoice):
    UserChoice.append("q") # Adds Branch root to List
    choice = input("You can choose 'q2' or 'q3': ")
    if choice == "q2": # player needs to input this in order to proceed through branch
        UserChoice.append(choice)
        print(UserChoice)
        q2()
    elif choice == "q3": # Will unlock a2() function/branch.
        UserChoice.append(choice)
        print(UserChoice)
        q3()
    else:
        print("Test q2 and q3: Invalid choice!")

def q2():
    choice = input("You can choose 'q3': ")
    if choice == "q3":
        UserChoice.append(choice)
        print(UserChoice)
        q3()
    else:
        print("Test q3: Invalid choice!")

def q3():
    choice = input("You can choose 'q4' or 'q5': ")
    if choice == "q4":
        UserChoice.append(choice)
        print(UserChoice)
        q4()
    # This unlocks the Buddy Quest/Event choices for Act 2.
    elif choice == "q5":
        UserChoice.append(choice)
        print(UserChoice)
        q5()
    else:
        print("Test q4 and q5: Invalid choice!")

def q4():
    choice = input("You can choose 'q6' or 'q7': ")
    if choice == "q6":
        UserChoice.append(choice)
        print(UserChoice)
        q6() # Unlocks "Helper" charecter.
    elif choice == "q7":
        UserChoice.append(choice)
        print(UserChoice)
        q7()
    else:
        print("Test q4()-q6 and q4()-q7: Invalid choice!")

def q5():
    choice = input("You can choose 'q6' or 'q7': ")
    if choice == "q6":
        UserChoice.append(choice)
        print(UserChoice)
        q6()
    elif choice == "q7":
        UserChoice.append(choice)
        print(UserChoice)
        q7()
    else:
        print("Test q5()-q6 and q5()-q7: Invalid choice!")

# This only happens if Buddy has been unlocked.
def q6():
    choice = input("You can choose 'q7': ")
    if choice == "q7":
        UserChoice.append(choice)
        print(UserChoice)
        q7()
    else:
        print("Test q7: Invalid choice!")

def q7():
    choice = input("You can choose 'q8': ")
    if choice == "q8":
        UserChoice.append(choice)
        print(UserChoice)
        q8()
    else:
        print("Test q8: Invalid choice!")

def q8():
    print("You have gotten to the end of Act 1!")

################################################################
###                                                          ###
###                    Start of Program                      ###
###                                                          ###
################################################################

#Presents user with Root choices of a, b, or c. Dependent on choice, will call it's associated Function
RootChoice = input("Choose a or q: ")
if RootChoice == "a":
    A_Chain(RootChoice) # Goes to A branch funtion chains
elif RootChoice == "q":
    Q_Chain(RootChoice) # Goes to B branch function chains
else:
    print("SORRY! Invalid choice!") # error handler... kinda
