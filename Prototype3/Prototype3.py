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

################################################################
###                         ACT 2                            ###
################################################################

def q8():
    # Checks to see if element "q5" exist in UserChoice List
    # If so, it means branch chains q11 are unlocked
    # But also lets the User can down the  q9 and q10 path.
    if 'q5' in UserChoice:
        choice = input("You can choose 'q9', 'q10' or 'q11': ")
        if choice == "q11": # Goes back to checking if input condition has been met
            UserChoice.append(choice)
            print(UserChoice)
            q11()
        elif choice == "q9": # Goes back to checking if input condition has been met
            UserChoice.append(choice)
            print(UserChoice)
            q9()
        elif choice == "q10":
            UserChoice.append(choice)
            print(UserChoice)
            q10()
        else:
            print("Test q9, q10 and q11: Invalid choice!")
    # Checks to see if element "q4" exist in UserChoice List
    # If so, then branch chains q9 and q10 are unlocked
    elif 'q4' in UserChoice:
        choice = input("You can choose 'q9' or 'q10': ")
        if choice == "q9": # Goes back to checking if input condition has been met
            UserChoice.append(choice)
            print(UserChoice)
            q9()
        elif choice == "q10":
            UserChoice.append(choice)
            print(UserChoice)
            q10()
        else:
            print("Test q9 and q10: Invalid choice!")
    else:
        print("I DON'T KNOW!")

def q9():
    choice = input("You can choose 'q15': ")
    if choice == "q15":
        UserChoice.append(choice)
        print(UserChoice)
        q15()
    else:
        print("Test q9()-q15: Invalid choice!")

def q10():
    choice = input("You can choose 'q15': ")
    if choice == "q15":
        UserChoice.append(choice)
        print(UserChoice)
        q15()
    else:
        print("Test q10()-q15: Invalid choice!")

def q11():
    choice = input("You can choose 'q12' or 'q13': ")
    if choice == "q12":
        UserChoice.append(choice)
        print(UserChoice)
        q14()
    elif choice == "q13":
        UserChoice.append(choice)
        print(UserChoice)
        q14()
    else:
        print("Test q12 and q13: Invalid choice!")

def q14():
    choice = input("You can choose 'q15': ")
    if choice == "q15":
        UserChoice.append(choice)
        print(UserChoice)
        q15()
    else:
        print("Test q14()-q15: Invalid choice!")

def q15():
    choice = input("You can choose 'q16': ")
    if choice == "q16":
        UserChoice.append(choice)
        print(UserChoice)
        q16()
    else:
        print("Test q16: Invalid choice!")

def q16():
    choice = input("You can choose 'q17' or 'q34': ")
    if choice == "q17":
        UserChoice.append(choice)
        print(UserChoice)
        q17()
    elif choice == "q34":
        UserChoice.append(choice)
        print(UserChoice)
        q34()
    else:
        print("Test q17 and q34: Invalid choice!")

# this Node reiterates the previous branch choices.
def q17():
    # Checks to see if element "q5" exist in UserChoice List
    # If so, it means branch chains q20 are unlocked
    # But also lets the User can down the q18 and q19 path.
    if 'q5' in UserChoice:
        choice = input("You can choose 'q18', 'q19' or 'q20': ")
        if choice == "q18": # Goes back to checking if input condition has been met
            UserChoice.append(choice)
            print(UserChoice)
            q18()
        elif choice == "q19": # Goes back to checking if input condition has been met
            UserChoice.append(choice)
            print(UserChoice)
            q19()
        elif choice == "q20":
            UserChoice.append(choice)
            print(UserChoice)
            q20()
        else:
            print("Test q18, q19 and q20: Invalid choice!")
    # Checks to see if element "q4" exist in UserChoice List
    # If so, then branch chains q9 and q10 are unlocked
    elif 'q4' in UserChoice:
        choice = input("You can choose 'q18' or 'q19': ")
        if choice == "q18": # Goes back to checking if input condition has been met
            UserChoice.append(choice)
            print(UserChoice)
            q18()
        elif choice == "q19":
            UserChoice.append(choice)
            print(UserChoice)
            q19()
        else:
            print("Test q18 and q19: Invalid choice!")
    else:
        print("Test q18, q19 and q20: Invalid choice!")

def q18():
    choice = input("You can choose 'q24': ")
    if choice == "q24":
        UserChoice.append(choice)
        print(UserChoice)
        q24()
    else:
        print("Test q18()-q24: Invalid choice!")

def q19():
    choice = input("You can choose 'q24': ")
    if choice == "q24":
        UserChoice.append(choice)
        print(UserChoice)
        q24()
    else:
        print("Test q19()-q24: Invalid choice!")

def q20():
    choice = input("You can choose 'q21' or 'q22': ")
    if choice == "q21":
        UserChoice.append(choice)
        print(UserChoice)
        q21()
    elif choice == "q22":
        UserChoice.append(choice)
        print(UserChoice)
        q22()
    else:
        print("Test q21 and q22: Invalid choice!")

def q21():
    choice = input("You can choose 'q23': ")
    if choice == "q23":
        UserChoice.append(choice)
        print(UserChoice)
        q23()
    else:
        print("Test q21()-q23: Invalid choice!")

def q22():
    choice = input("You can choose 'q23': ")
    if choice == "q23":
        UserChoice.append(choice)
        print(UserChoice)
        q23()
    else:
        print("Test q22()-q23: Invalid choice!")

def q23():
    choice = input("You can choose 'q24': ")
    if choice == "q24":
        UserChoice.append(choice)
        print(UserChoice)
        q24()
    else:
        print("Test q23()-q24: Invalid choice!")

def q24():
    choice = input("You can choose 'q25': ")
    if choice == "q25":
        UserChoice.append(choice)
        print(UserChoice)
        q25()
    else:
        print("Test q24: Invalid choice!")

def q25():
    choice = input("You can choose 'q26' or 'q34': ")
    if choice == "q26":
        UserChoice.append(choice)
        print(UserChoice)
        q26()
    elif choice == "q34":
        UserChoice.append(choice)
        print(UserChoice)
        q34()
    else:
        print("Test q26 and q34: Invalid choice!")

def q26():
    # Checks to see if element "q5" exist in UserChoice List
    # If so, it means branch chains q29 are unlocked
    # But also lets the User can down the q27 and q28 path.
    if 'q5' in UserChoice:
        choice = input("You can choose 'q27', 'q28' or 'q29': ")
        if choice == "q27": # Goes back to checking if input condition has been met
            UserChoice.append(choice)
            print(UserChoice)
            q27()
        elif choice == "q28": # Goes back to checking if input condition has been met
            UserChoice.append(choice)
            print(UserChoice)
            q28()
        elif choice == "q29":
            UserChoice.append(choice)
            print(UserChoice)
            q29()
        else:
            print("Test q27, q28 and q29: Invalid choice!")
    # Checks to see if element "q4" exist in UserChoice List
    # If so, then branch chains q27 and q28 are unlocked
    elif 'q4' in UserChoice:
        choice = input("You can choose 'q27' or 'q28': ")
        if choice == "q27": # Goes back to checking if input condition has been met
            UserChoice.append(choice)
            print(UserChoice)
            q27()
        elif choice == "q28":
            UserChoice.append(choice)
            print(UserChoice)
            q28()
        else:
            print("Test q18 and q19: Invalid choice!")
    else:
        print("Test q27, q28 and q29: Invalid choice!")

def q27():
    choice = input("You can choose 'q33': ")
    if choice == "q33":
        UserChoice.append(choice)
        print(UserChoice)
        q33()
    else:
        print("Test q27()-q33: Invalid choice!")

def q28():
    choice = input("You can choose 'q33': ")
    if choice == "q33":
        UserChoice.append(choice)
        print(UserChoice)
        q33()
    else:
        print("Test q28()-q33: Invalid choice!")

def q29():
    choice = input("You can choose 'q30' or 'q31': ")
    if choice == "q30":
        UserChoice.append(choice)
        print(UserChoice)
        q30()
    elif choice == "q31":
        UserChoice.append(choice)
        print(UserChoice)
        q31()
    else:
        print("Test q30 and q31: Invalid choice!")

def q30():
    choice = input("You can choose 'q32': ")
    if choice == "q32":
        UserChoice.append(choice)
        print(UserChoice)
        q32()
    else:
        print("Test q30()-q32: Invalid choice!")

def q31():
    choice = input("You can choose 'q32': ")
    if choice == "q32":
        UserChoice.append(choice)
        print(UserChoice)
        q32()
    else:
        print("Test q31()-q32: Invalid choice!")

def q32():
    choice = input("You can choose 'q33': ")
    if choice == "q33":
        UserChoice.append(choice)
        print(UserChoice)
        q33()
    else:
        print("Test q32()-q33: Invalid choice!")

def q33():
    choice = input("You can choose'q34': ")
    if choice == "q34":
        UserChoice.append(choice)
        print(UserChoice)
        q34()
    else:
        print("Test q34: Invalid choice!")

################################################################
###                         ACT 3                            ###
################################################################

# Leads to Node that intiates Act 3
def q34():
    choice = input("You can choose 'q35' or 'q36': ")
    if choice == "q35":
        UserChoice.append(choice)
        print(UserChoice)
        q35()
    elif choice == "q36":
        UserChoice.append(choice)
        print(UserChoice)
        q36()
    else:
        print("Test q35 and q36: Invalid choice!")

def q35():
    choice = input("You can choose 'q36': ")
    if choice == "q36":
        UserChoice.append(choice)
        print(UserChoice)
        q36()
    else:
        print("Test q35()-q36: Invalid choice!")

def q36():
    choice = input("You can choose 'q37' or 'q38': ")
    if choice == "q37":
        UserChoice.append(choice)
        print(UserChoice)
        q37()
    elif choice == "q38":
        UserChoice.append(choice)
        print(UserChoice)
        q38()
    else:
        print("Test q37 and q38: Invalid choice!")

def q37():
    choice = input("You can choose 'q39' or 'q40': ")
    if choice == "q39":
        UserChoice.append(choice)
        print(UserChoice)
        q39()
    elif choice == "q40":
        UserChoice.append(choice)
        print(UserChoice)
        q40()
    else:
        print("Test q37()-q39 and q37()-q40: Invalid choice!")

def q38():
    choice = input("You can choose 'q39' or 'q40': ")
    if choice == "q39":
        UserChoice.append(choice)
        print(UserChoice)
        q39()
    elif choice == "q40":
        UserChoice.append(choice)
        print(UserChoice)
        q40()
    else:
        print("Test q38()-q39 and q38()-q40: Invalid choice!")

def q39():
    choice = input("You can choose 'q41' or 'q42': ")
    if choice == "q41":
        UserChoice.append(choice)
        print(UserChoice)
        q41()
    elif choice == "q42":
        UserChoice.append(choice)
        print(UserChoice)
        q42()
    else:
        print("Test q39()-q41 and q39()-q42: Invalid choice!")

def q40():
    choice = input("You can choose 'q41' or 'q42': ")
    if choice == "q41":
        UserChoice.append(choice)
        print(UserChoice)
        print("You have reached the end of the Quest Branch!")
    elif choice == "q42":
        UserChoice.append(choice)
        print(UserChoice)
        print("You have reached the end of the Quest Branch!")
    else:
        print("Test q40()-q41 and q40()-q42: Invalid choice!")

################################################################
###                 Quest Branch Code Finished               ###
################################################################   

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
