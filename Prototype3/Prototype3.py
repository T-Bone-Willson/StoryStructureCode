# users choice stored in an empty list.
UserChoice = []

################################################################
###         Dictionary/Graph for Adventure, Quest and        ###
###                     Voyage & Return                      ###
################################################################

# Adventure Branch Code Dictionary
Adventure_Graph_Elements = {"a" : ["a1", "a2"],
                    "a1" : ["a3"],
                    "a2" : ["a3"], # Can't represent "Romance Condition" properly here...
                    "a3" : ["a4"],
                    "a4" : ["a5"],
                    "a6" : ["a7"],
                    "a7" : ["a8"],
                    "a8" : ["a9", "a10"],
                    "a9" : ["a13", "a14"],
                    "a10" : ["a11", "a12"],
                    "a11" : ["a13", "a14"],
                    "a12" : ["a13", "a14"],
                    "a13" : [], # Key will be empty since there are no more nodes connected to it
                    "a14" : []
                    }

# Quest Branch Code Dictionary
Quest_Graph_Elements = {"q" : ["q1," "q2"],
                    "q1" : ["q2"],
                    "q2" : ["q3", "q4"],
                    "q3" : ["q5", "q6"],
                    "q4" : ["q5", "q6"], # Can't represent "Buddy Condition" properly here...
                    "q5" : ["q6"],
                    "q6" : ["q7"],
                    "q7" : ["q8", "q9", "q10"],
                    "q8" : ["q14"],
                    "q9" : ["q14"],
                    "q10" : ["q11", "q12"],
                    "q11" : ["q13"],
                    "q12" : ["q13"],
                    "q13" : ["q14"],
                    "q14" : ["q15"],
                    "q15" : ["q16", "q33"],
                    "q16" : ["q17", "q18", "q19"],
                    "q17" : ["q23"],
                    "q18" : ["q23"],
                    "q19" : ["q20", "q21"],
                    "q20" : ["q22"],
                    "q21" : ["q22"],
                    "q22" : ["q23"],
                    "q23" : ["q24"],
                    "q24" : ["q25", "q33"],
                    "q25" : ["q26", "q27", "q28"],
                    "q26" : ["q32"],
                    "q27" : ["q32"],
                    "q28" : ["q29", "q30"],
                    "q29" : ["q31"],
                    "q30" : ["q31"],
                    "q31" : ["q32"],
                    "q32" : ["q33"],
                    "q33" : ["q34", "q35"],
                    "q34" : ["q35"],
                    "q35" : ["q36", "q37"],
                    "q36" : ["q38", "q39"],
                    "q37" : ["q38", "q39"],
                    "q38" : ["q40", "q41"],
                    "q39" : ["q40", "q41"],
                    "q40" : [], # Key will be empty since there are no more nodes connected to it
                    "q41" : []
                    }

# Voyage and Return Branch Code Diciontary
VandR_Graph_Elements = {"v" : ["v1", "v2"],
                    "v1" : ["v3"],
                    "v2" : ["v3"],
                    "v3" : ["v4", "v5"],
                    "v4" : ["v6", "v7"],
                    "v5" : ["v6", "v7"],
                    "v6" : ["v8"],
                    "v7" : ["v8"],
                    "v8" : ["v9"],
                    "v9" : ["v10"],
                    "v10" : ["v11"],
                    "v11" : ["v12", "v13", "v14", "v15"],
                    "v12" : [], # Key will be empty since there are no more nodes connected to it
                    "v13" : [], # Can't represent "Romance Condition" properly here...
                    "v14" : [],
                    "v15" : []
                    }


################################################################
###                                                          ###
###              Adventure Branch Function Code              ###
###                                                          ###
################################################################

################################################################
###                         ACT 1                            ###
################################################################

# Start of Adventure branch chain. Triggerd by User making choice "a" at start of program.
def A_Chain(RootChoice):
    # Node a is "Home: Protagonist is there and they want the Elixir"
    UserChoice.append("a") # Adds Branch root to List
    # Node a1 is "Elixir: It is inanimate object"
    # Node a2 is "Elixir: Is another charecter"
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

#-------------------------------------------------------------#
# a1() function means the elixir is not a person.             #
# by having element "a1" in UserChoice List, it means that    #
# Function a9() will be unlocked automaticaly                 #
# but will close off Function a10()                           #
#-------------------------------------------------------------#
# Node a2 is "Elixir: Is another charecter"
def a1():
    choice = input("You can choose 'a3': ")
    if choice == "a3":
        UserChoice.append(choice)
        print(UserChoice)
        a3()
    else:
        print("Test a1()-a3: Invalid choice!")

#-------------------------------------------------------------#
# a2() function means the elixir is a person.                 #
# by having element "a2" in UserChoice List, it means that    #
# Function a10() will be unlocked automaticaly                #
# but will close off Function a9()                            #
#-------------------------------------------------------------#
# Node a2 is "Elixir: Is another charecter"
def a2():
    # Node a3 is "Inciting Incident: Forces the Protagonist to commence the Adventure/Journey"
    choice = input("You can choose 'a3': ")
    if choice == "a3":
        UserChoice.append(choice)
        print(UserChoice)
        a3()
    else:
        print("Test  a2()-a3: Invalid choice!")

# Node a3 is "Inciting Incident: Forces the Protagonist to commence the Adventure/Journey"
def a3():
    # Node a4 is "Protagonist commences the Journey"
    choice = input("You can choose 'a4': ")
    if choice == "a4":
        UserChoice.append(choice)
        print(UserChoice)
        a4()
    else:
        print("Test a4: Invalid choice!")

################################################################
###                         ACT 2                            ###
################################################################

# Node a4 is "Protagonist commences the Journey"
def a4():
    # Node a5 is "Journey: Protagonist goes to new, differnt world/places."
    choice = input("You can choose 'a5': ")
    if choice == "a5":
        UserChoice.append(choice)
        print(UserChoice)
        a5()
    else:
        print("Test a5: Invalid choice!")

# Node a5 is "Journey: Protagonist goes to new, differnt world/places."
def a5():
    # Node a6 is "Midpoint: Something from the previous Plot Point/Node will cause a dramatic moment
    # for the Protagonist, to which they will have to overcome, and will then lead to the next place
    # within their Journey."
    choice = input("You can choose 'a6': ")
    if choice == "a6":
        UserChoice.append(choice)
        print(UserChoice)
        a6()
    else:
        print("Test a6: Invalid choice!")

# Node a6 is "Midpoint: Something from the previous Plot Point/Node will cause a dramatic moment
# for the Protagonist, to which they will have to overcome, and will then lead to the next place
# within their Journey."
def a6():
    # Node a7 "The effects of the Midpoint lead the Protagonist into a new and
    # unfamilair place, in search for the Elixir."
    choice = input("You can choose 'a7': ")
    if choice == "a7":
        UserChoice.append(choice)
        print(UserChoice)
        a7()
    else:
        print("Test a7: Invalid choice!")

# Node a7 "The effects of the Midpoint lead the Protagonist into a new and
# unfamilair place, in search for the Elixir."
def a7():
    # Node a8 is "Conflict: The series of events throughout the story so far will lead
    # to the conflict in which the Protagonist has to overcome to carry on the Journey
    # and get the Elixir."
    choice = input("You can choose 'a8': ")
    if choice == "a8":
        UserChoice.append(choice)
        print(UserChoice)
        a8()
    else:
        print("Test a8: Invalid choice!")

################################################################
###                         ACT 3                            ###
################################################################

# Node a8 is "Conflict: The series of events throughout the story so far will lead
# to the conflict in which the Protagonist has to overcome to carry on the Journey
# and get the Elixir."
def a8():
    # Checks to see if element "a2" exist in UserChoice List
    # If so, it means branch chains a10 and onwards are unlocked
    if 'a2' in UserChoice:
        # Node a10 is "Elixir: Protagonist gets Elixir, who is another charecter."
        choice = input("You can choose 'a10': ")
        if choice == "a10": # Goes back to checking if input condition has been met
            UserChoice.append(choice)
            print(UserChoice)
            a10()
    # Checks to see if element "a1" exist in UserChoice List
    # If so, then branch chains a9, a13 and a14 are unlocked
    elif 'a1' in UserChoice:
        # Node a9 is "Elixir: Inanimate Elixir is aquired."
        choice = input("You can choose 'a9': ")
        if choice == "a9": # Goes back to checking if input condition has been met
            UserChoice.append(choice)
            print(UserChoice)
            a9()
    else:
        print("Test a9 OR a10: Invalid choice!")

# Adventure Branch with no possible love interest is operated from this chain
# Node a9 is "Elixir: Inanimate Elixir is aquired."
def a9():
    # Node a13 is "End: Protagonist Goes Home"
    # Node a14 is "End: Protagonist Carries on with Journey, doesn't go Home"
    choice = input("You can choose 'a13' or 'a14': ")
    if choice == "a13":
        UserChoice.append(choice)
        print(UserChoice)
        print("You have reached the end of this Branch!")
    elif choice == "a14":
        UserChoice.append(choice)
        print(UserChoice)
        print("You have reached the end of this Branch")
    else:
        print("Test a13 and a14: Invalid choice!")

# Adventure Branch with possible love interest is operated from this chain
# Node a10 is "Elixir: Protagonist gets Elixir, who is another charecter."
def a10():
    # Node a11 is "Elixir Charecter: Romance happens."
    # Node a12 is "Elixir Charecter: Romance doesn't happen."
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

# Node a11 is "Elixir Charecter: Romance happens."
def a11():
    # Node a13 is "End: Protagonist Goes Home"
    # Node a14 is "End: Protagonist Carries on with Journey, doesn't go Home"
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

# Node a12 is "Elixir Charecter: Romance doesn't happen."
def a12():
    # Node a13 is "End: Protagonist Goes Home"
    # Node a14 is "End: Protagonist Carries on with Journey, doesn't go Home"
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
###                Adventure Branch Code Finished            ###
################################################################

################################################################
###                                                          ###
###                Quest Branch Function Code                ###
###                                                          ###
################################################################

################################################################
###                         ACT 1                            ###
################################################################

def Q_Chain(RootChoice):
    # Node q is "Home"
    UserChoice.append("q") # Adds Branch root to List
    # Node q1 is "Reason why Charecter wants Elixir"
    # Node q2 is "Inciting Incident"
    choice = input("You can choose 'q1' or 'q2': ")
    if choice == "q1": # player needs to input this in order to proceed through branch
        UserChoice.append(choice)
        print(UserChoice)
        q1()
    elif choice == "q2":
        UserChoice.append(choice)
        print(UserChoice)
        q2()
    else:
        print("Test q1 and q2: Invalid choice!")

# Node q1 is "Reason why Charecter wants Elixir"
def q1():
    # Node q2 is "Inciting Incident"
    choice = input("You can choose 'q2': ")
    if choice == "q2":
        UserChoice.append(choice)
        print(UserChoice)
        q2()
    else:
        print("Test q2: Invalid choice!")

# Node q2 is "Inciting Incident"
def q2():
    # Node q3 is "Don't gather 'buddies' for journey, Protagonist will journey alone"
    # Node q4 is "gather 'Buddies'", Protagoniost will journey with company
    choice = input("You can choose 'q3' or 'q4': ")
    if choice == "q3":
        UserChoice.append(choice)
        print(UserChoice)
        q3()
    # This unlocks the Buddy Quest/Event choices for Act 2.
    elif choice == "q4":
        UserChoice.append(choice)
        print(UserChoice)
        q4()
    else:
        print("Test q3 and q4: Invalid choice!")

# Node q3 is "Don't gather 'buddies' for journey, Protagonist will journey alone"
def q3():
    # Node q5 is "Helper" will be present in the story.
    # Node q6 is "Commencing the Journey"
    choice = input("You can choose 'q5' or 'q6': ")
    if choice == "q5":
        UserChoice.append(choice)
        print(UserChoice)
        q5() # Unlocks "Helper" charecter.
    elif choice == "q6":
        UserChoice.append(choice)
        print(UserChoice)
        q6()
    else:
        print("Test q3()-q5 and q3()-q6: Invalid choice!")

# Node q4 is "gather 'Buddies'", Protagoniost will journey with company
def q4():
    # Node q5 is "Helper" will be present in the story.
    # Node q6 is "Commencing the Journey"
    choice = input("You can choose 'q5' or 'q6': ")
    if choice == "q5":
        UserChoice.append(choice)
        print(UserChoice)
        q5()
    elif choice == "q6":
        UserChoice.append(choice)
        print(UserChoice)
        q6()
    else:
        print("Test q4()-q5 and q4()-q6: Invalid choice!")

# Node q5 is "Helper" will be present in the story.
def q5():
    # Node q6 is "Commencing the Journey"
    choice = input("You can choose 'q6': ")
    if choice == "q6":
        UserChoice.append(choice)
        print(UserChoice)
        q6()
    else:
        print("Test q6: Invalid choice!")

# Node q6 is "Commencing the Journey"
def q6():
    # Node q7 is "Event/Obstacle 1 in Journey"
    choice = input("You can choose 'q7': ")
    if choice == "q7":
        UserChoice.append(choice)
        print(UserChoice)
        q7()
    else:
        print("Test q7: Invalid choice!")

################################################################
###                         ACT 2                            ###
################################################################

# Node q7 is "Event/Obstacle 1 in Journey"
def q7():
    # Checks to see if element "q4" exist in UserChoice List
    # If so, it means branch chains q10 are unlocked
    # But also lets the User can down the  q8 and q9 path.
    if 'q4' in UserChoice:
        # Node q8 is "Event/Obstacle 1 in Journey has Failed"
        # Node q9 is "Event/Obstacle 1 in Journey has Passed"
        # Node q10 is "Event/Obstacle 1 is a 'Buddy' quest"
        choice = input("You can choose 'q8', 'q9' or 'q10': ")
        if choice == "q10": # Goes back to checking if input condition has been met
            UserChoice.append(choice)
            print(UserChoice)
            q10()
        elif choice == "q8": # Goes back to checking if input condition has been met
            UserChoice.append(choice)
            print(UserChoice)
            q8()
        elif choice == "q9":
            UserChoice.append(choice)
            print(UserChoice)
            q9()
        else:
            print("Test q8, q9 and q10: Invalid choice!")
    # Checks to see if element "q3" exist in UserChoice List
    # If so, then branch chains q8 and q9 are unlocked
    elif 'q3' in UserChoice:
        # Node q8 is "Event/Obstacle 1 in Journey has Failed"
        # Node q9 is "Event/Obstacle 1 in Journey has Passed"
        choice = input("You can choose 'q8' or 'q9': ")
        if choice == "q8": # Goes back to checking if input condition has been met
            UserChoice.append(choice)
            print(UserChoice)
            q8()
        elif choice == "q9":
            UserChoice.append(choice)
            print(UserChoice)
            q9()
        else:
            print("Test q8 and q9: Invalid choice!")
    else:
        print("I DON'T KNOW!")

# Node q8 is "Event/Obstacle 1 in Journey has Failed"
def q8():
    # Node q14 is "Event 1 resolution"
    choice = input("You can choose 'q14': ")
    if choice == "q14":
        UserChoice.append(choice)
        print(UserChoice)
        q14()
    else:
        print("Test q8()-q14: Invalid choice!")

# Node q9 is "Event/Obstacle 1 in Journey has Passed"
def q9():
    # Node q14 is "Event 1 resolution"
    choice = input("You can choose 'q14': ")
    if choice == "q14":
        UserChoice.append(choice)
        print(UserChoice)
        q14()
    else:
        print("Test q9()-q14: Invalid choice!")

# Node q10 is "Event/Obstacle 1 is a 'Buddy' quest"
def q10():
    # Node q11 is "Buddy Quest 1 Passed"
    # Node q12 is "Buddy Quest 1 Failed"
    choice = input("You can choose 'q11' or 'q12': ")
    if choice == "q11":
        UserChoice.append(choice)
        print(UserChoice)
        q11()
    elif choice == "q12":
        UserChoice.append(choice)
        print(UserChoice)
        q12()
    else:
        print("Test q11 and q12: Invalid choice!")

# Node q11 is "Buddy Quest 1 Passed"
def q11():
    # Node q13 is "Resolution of Buddy Quest 1"
    choice = input("You can choose q13: ")
    if choice == "q13":
        UserChoice.append(choice)
        print(UserChoice)
        q13()
    else:
        print("Test q11()-q13(): Invalid choice!")

# Node q12 is "Buddy Quest 1 Failed"
def q12():
    # Node q13 is "Resolution of Buddy Quest 1"
    choice = input("You can choose 'q13': ")
    if choice == "q13":
        UserChoice.append(choice)
        print(UserChoice)
        q13()
    else:
        print("Test q12()-q13(): Invalid choice!")

# Node q13 is "Resolution of Buddy Quest 1"
def q13():
    # Node q14 is "Event 1 resolution"
    choice = input("You can choose 'q14': ")
    if choice == "q14":
        UserChoice.append(choice)
        print(UserChoice)
        q14()
    else:
        print("Test q13()-q14: Invalid choice!")

# Node q14 is "Event 1 resolution"
def q14():
    # Node q15 is "Journey to Act 3 OR Start of Event/Obstacle 2 in Journey"
    choice = input("You can choose 'q15': ")
    if choice == "q15":
        UserChoice.append(choice)
        print(UserChoice)
        q15()
    else:
        print("Test q15: Invalid choice!")

# Node q15 is "Journey to Act 3 OR Start of Event/Obstacle 2 in Journey"
def q15():
    # Node q16 is "Event/Obstacle 2 in Journey"
    # Node q33 is "Starts Act 3"
    choice = input("You can choose 'q16' or 'q33': ")
    if choice == "q16":
        UserChoice.append(choice)
        print(UserChoice)
        q16()
    elif choice == "q33":
        UserChoice.append(choice)
        print(UserChoice)
        q33()
    else:
        print("Test q16 and q33: Invalid choice!")

# Node q16 is "Event/Obstacle 2 in Journey"
# this Node reiterates the previous branch choices.
def q16():
    # Checks to see if element "q4" exist in UserChoice List
    # If so, it means branch chains q19 are unlocked
    # But also lets the User can down the q17 and q18 path.
    if 'q4' in UserChoice:
        # Node q17 is "Event/Obstacle 2, Passed, in Journey"
        # Node q18 is "Eevnt/Obstacle 2, Failed, in Journey"
        # Node q19 is "Event/Obstacle 2. Buddy Quest 2, In Journey"
        choice = input("You can choose 'q17', 'q18' or 'q19': ")
        if choice == "q17": # Goes back to checking if input condition has been met
            UserChoice.append(choice)
            print(UserChoice)
            q17()
        elif choice == "q18": # Goes back to checking if input condition has been met
            UserChoice.append(choice)
            print(UserChoice)
            q18()
        elif choice == "q19":
            UserChoice.append(choice)
            print(UserChoice)
            q19()
        else:
            print("Test q17, q18 and q19: Invalid choice!")
    # Checks to see if element "q3" exist in UserChoice List
    # If so, then branch chains q8 and q9 are unlocked
    elif 'q3' in UserChoice:
        # Node q17 is "Event/Obstacle 2, Passed, in Journey"
        # Node q18 is "Eevnt/Obstacle 2, Failed, in Journey"
        choice = input("You can choose 'q17' or 'q18': ")
        if choice == "q17": # Goes back to checking if input condition has been met
            UserChoice.append(choice)
            print(UserChoice)
            q17()
        elif choice == "q18":
            UserChoice.append(choice)
            print(UserChoice)
            q18()
        else:
            print("Test q17 and q18: Invalid choice!")
    else:
        print("Test q17, q18 and q19: Invalid choice!")

# Node q17 is "Event/Obstacle 2, Passed, in Journey"
def q17():
    # Node q23 is "Event 2 In Journey, Resolution"
    choice = input("You can choose 'q23': ")
    if choice == "q23":
        UserChoice.append(choice)
        print(UserChoice)
        q23()
    else:
        print("Test q17()-q23: Invalid choice!")

# Node q18 is "Eevnt/Obstacle 2, Failed, in Journey"
def q18():
    # Node q23 is "Event 2 In Journey, Resolution"
    choice = input("You can choose 'q23': ")
    if choice == "q23":
        UserChoice.append(choice)
        print(UserChoice)
        q23()
    else:
        print("Test q18()-q23: Invalid choice!")

# Node q19 is "Event/Obstacle 2. Buddy Quest 2, In Journey"
def q19():
    # Node q20 is "Buddy Quest 2, Passed"
    # Node q21 is "Buddy Quest 2, Failed"
    choice = input("You can choose 'q20' or 'q21': ")
    if choice == "q20":
        UserChoice.append(choice)
        print(UserChoice)
        q20()
    elif choice == "q21":
        UserChoice.append(choice)
        print(UserChoice)
        q21()
    else:
        print("Test q20 and q21: Invalid choice!")

# Node q20 is "Buddy Quest 2, Passed"
def q20():
    # Node q22 is "Resolution from Buddy Quest 2"
    choice = input("You can choose 'q22': ")
    if choice == "q22":
        UserChoice.append(choice)
        print(UserChoice)
        q22()
    else:
        print("Test q20()-q22: Invalid choice!")

# Node q21 is "Buddy Quest 2, Failed"
def q21():
    # Node q22 is "Resolution from Buddy Quest 2"
    choice = input("You can choose 'q22': ")
    if choice == "q22":
        UserChoice.append(choice)
        print(UserChoice)
        q22()
    else:
        print("Test q21()-q22: Invalid choice!")

# Node q22 is "Resolution from Buddy Quest 2"
def q22():
    # Node q23 is "Event 2 In Journey, Resolution"
    choice = input("You can choose 'q23': ")
    if choice == "q23":
        UserChoice.append(choice)
        print(UserChoice)
        q23()
    else:
        print("Test q22()-q23: Invalid choice!")

# Node q23 is "Event 2 In Journey, Resolution"
def q23():
    # Node q24 is "Journey to Act 3 or Event/Obstacle 3 in Journey"
    choice = input("You can choose 'q24': ")
    if choice == "q24":
        UserChoice.append(choice)
        print(UserChoice)
        q24()
    else:
        print("Test q23: Invalid choice!")

# Node q24 is "Journey to Act 3 or Event/Obstacle 3 in Journey"
def q24():
    # Node q25 is "Event/Obstacle 3 in Journey"
    # Node q33 is "Starts Act 3"
    choice = input("You can choose 'q25' or 'q33': ")
    if choice == "q25":
        UserChoice.append(choice)
        print(UserChoice)
        q25()
    elif choice == "q33":
        UserChoice.append(choice)
        print(UserChoice)
        q33()
    else:
        print("Test q25 and q33: Invalid choice!")

# Node q25 is "Event/Obstacle 3 in Journey"
def q25():
    # Checks to see if element "q4" exist in UserChoice List
    # If so, it means branch chains q28 are unlocked
    # But also lets the User can down the q26 and q27 path.
    if 'q4' in UserChoice:
        # Node q26 is "Event/Obstacle 3, Passed, in Journey"
        # Node q27 is "Event/Obstacle 3, Failed, in Journey"
        # Node q28 is "Buddy Quest 3 Event/Obstacle"
        choice = input("You can choose 'q26', 'q27' or 'q28': ")
        if choice == "q26": # Goes back to checking if input condition has been met
            UserChoice.append(choice)
            print(UserChoice)
            q26()
        elif choice == "q27": # Goes back to checking if input condition has been met
            UserChoice.append(choice)
            print(UserChoice)
            q27()
        elif choice == "q28":
            UserChoice.append(choice)
            print(UserChoice)
            q28()
        else:
            print("Test q26, q27 and q28: Invalid choice!")
    # Checks to see if element "q3" exist in UserChoice List
    # If so, then branch chains q26 and q27 are unlocked
    elif 'q3' in UserChoice:
        # Node q26 is "Event/Obstacle 3, Passed, in Journey"
        # Node q27 is "Event/Obstacle 3, Failed, in Journey"
        choice = input("You can choose 'q26' or 'q27': ")
        if choice == "q26": # Goes back to checking if input condition has been met
            UserChoice.append(choice)
            print(UserChoice)
            q26()
        elif choice == "q27":
            UserChoice.append(choice)
            print(UserChoice)
            q27()
        else:
            print("Test q17 and q18: Invalid choice!")
    else:
        print("Test q26, q27 and q28: Invalid choice!")

# Node q26 is "Event/Obstacle 3, Passed, in Journey"
def q26():
    # Node q32 is "Resolution from Event/Obstacle 3 in Journey"
    choice = input("You can choose 'q32': ")
    if choice == "q32":
        UserChoice.append(choice)
        print(UserChoice)
        q32()
    else:
        print("Test q26()-q32: Invalid choice!")

# Node q27 is "Event/Obstacle 3, Failed, in Journey"
def q27():
    # Node q32 is "Resolution from Event/Obstacle 3 in Journey"
    choice = input("You can choose 'q32': ")
    if choice == "q32":
        UserChoice.append(choice)
        print(UserChoice)
        q32()
    else:
        print("Test q27()-q32: Invalid choice!")

# Node q28 is "Buddy Quest 3 Event/Obstacle"
def q28():
    # Node q29 is "Buddy Quest 3, Passed"
    # Node q30 is "Buddy Quest, Failed"
    choice = input("You can choose 'q29' or 'q30': ")
    if choice == "q29":
        UserChoice.append(choice)
        print(UserChoice)
        q29()
    elif choice == "q30":
        UserChoice.append(choice)
        print(UserChoice)
        q30()
    else:
        print("Test q29 and q30: Invalid choice!")

# Node q29 is "Buddy Quest 3, Passed"
def q29():
    # Node q31 is "Resolution from Bussy Quest 3"
    choice = input("You can choose 'q31': ")
    if choice == "q31":
        UserChoice.append(choice)
        print(UserChoice)
        q31()
    else:
        print("Test q29()-q31: Invalid choice!")

# Node q30 is "Buddy Quest, Failed"
def q30():
    # Node q31 is "Resolution from Bussy Quest 3"
    choice = input("You can choose 'q31': ")
    if choice == "q31":
        UserChoice.append(choice)
        print(UserChoice)
        q31()
    else:
        print("Test q30()-q31: Invalid choice!")

# Node q31 is "Resolution from Bussy Quest 3"
def q31():
    # Node q32 is "Resolution from Event/Obstacle 3 in Journey"
    choice = input("You can choose 'q32': ")
    if choice == "q32":
        UserChoice.append(choice)
        print(UserChoice)
        q32()
    else:
        print("Test q31()-q32: Invalid choice!")

# Node q32 is "Resolution from Event/Obstacle 3 in Journey"
def q32():
    # Node q33 is "Starts Act 3"
    choice = input("You can choose'q33': ")
    if choice == "q33":
        UserChoice.append(choice)
        print(UserChoice)
        q33()
    else:
        print("Test q33: Invalid choice!")

################################################################
###                         ACT 3                            ###
################################################################

# Node q33 is "Starts Act 3"
def q33():
    # Node q34 is "Event that leds to 'Revelation'"
    # Node q35 is "Revelation: True nature of the Elixir"
    choice = input("You can choose 'q34' or 'q35': ")
    if choice == "q34":
        UserChoice.append(choice)
        print(UserChoice)
        q34()
    elif choice == "q35":
        UserChoice.append(choice)
        print(UserChoice)
        q35()
    else:
        print("Test q34 and q35: Invalid choice!")

# Node q34 is "Event that leds to 'Revelation'"
def q34():
    # Node q35 is "Revelation: True nature of the Elixir"
    choice = input("You can choose 'q35': ")
    if choice == "q35":
        UserChoice.append(choice)
        print(UserChoice)
        q35()
    else:
        print("Test q34()-q35: Invalid choice!")

# Node q35 is "Revelation: True nature of the Elixir"
def q35():
    # Node q36 is "Protagonist gets Elixir"
    # Node q37 is "Protagonist doesn't get Elixir"
    choice = input("You can choose 'q36' or 'q37': ")
    if choice == "q36":
        UserChoice.append(choice)
        print(UserChoice)
        q36()
    elif choice == "q37":
        UserChoice.append(choice)
        print(UserChoice)
        q37()
    else:
        print("Test q36 and q37: Invalid choice!")

# Node q36 is "Protagonist gets Elixir"
def q36():
    # Node q38 is "Protagonist has negative charecter development change from Elixir Node Choice"
    # Node q39 is "Protagonist has positive charecter development change from Elixir Node Choice"
    choice = input("You can choose 'q38' or 'q39': ")
    if choice == "q38":
        UserChoice.append(choice)
        print(UserChoice)
        q38()
    elif choice == "q39":
        UserChoice.append(choice)
        print(UserChoice)
        q39()
    else:
        print("Test q36()-q38 and q36()-q39: Invalid choice!")

# Node q37 is "Protagonist doesn't get Elixir"
def q37():
    # Node q38 is "Protagonist has negative charecter development change from Elixir Node Choice"
    # Node q39 is "Protagonist has positive charecter development change from Elixir Node Choice"
    choice = input("You can choose 'q38' or 'q39': ")
    if choice == "q38":
        UserChoice.append(choice)
        print(UserChoice)
        q38()
    elif choice == "q39":
        UserChoice.append(choice)
        print(UserChoice)
        q39()
    else:
        print("Test q37()-q38 and q37()-q39: Invalid choice!")

# Node q38 is "Protagonist has negative charecter development change from Elixir Node Choice"
def q38():
    # Node q40 "Protagonist goes Home"
    # Node q41 "Protagonist doesn't go Home"
    choice = input("You can choose 'q40' or 'q41': ")
    if choice == "q40":
        UserChoice.append(choice)
        print(UserChoice)
        q40()
    elif choice == "q41":
        UserChoice.append(choice)
        print(UserChoice)
        q41()
    else:
        print("Test q38()-q40 and q38()-q41: Invalid choice!")

# Node q39 is "Protagonist has positive charecter development change from Elixir Node Choice"
def q39():
    # Node q40 "Protagonist goes Home"
    # Node q41 "Protagonist doesn't go Home"
    choice = input("You can choose 'q40' or 'q41': ")
    if choice == "q40":
        UserChoice.append(choice)
        print(UserChoice)
        print("You have reached the end of the Quest Branch!")
    elif choice == "q41":
        UserChoice.append(choice)
        print(UserChoice)
        print("You have reached the end of the Quest Branch!")
    else:
        print("Test q39()-q40 and q39()-q41: Invalid choice!")

################################################################
###                 Quest Branch Code Finished               ###
################################################################

################################################################
###                                                          ###
###               Voyage and return Branch Code              ###
###                                                          ###
################################################################

################################################################
###                         ACT 1                            ###
################################################################

def VandR_Chain(RootChoice):
    # Node v is "Home"
    UserChoice.append("v") # Adds Branch root to List
    # Node v1 is "Inciting Incident: With no Intent of it to happen."
    # Node v2 is "Inciting Incident: With a vague sense of Intent of it to happen"
    choice = input("You can choose 'v1' or 'v2': ")
    if choice == "v1":
        UserChoice.append(choice)
        print(UserChoice)
        v1()
    elif choice == "v2":
        UserChoice.append(choice)
        print(UserChoice)
        v2()
    else:
        print("Test v1 and v2: Invalid choice!")

# Node v1 is "Inciting Incident: With no Intent of it to happen."
def v1():
    # Node v3 is "Protagonist is taken to 'other/abnormal world' which is
    # caused by the Inciting Incident 'v1' OR 'v2'"
    choice = input("You can choose 'v3': ")
    if choice == "v3":
        UserChoice.append(choice)
        print(UserChoice)
        v3()
    else:
        print("Test v1()-v3: Invalid choice!")

# Node v2 is "Inciting Incident: With a vague sense of Intent of it to happen"
def v2():
    # Node v3 is "Protagonist is taken to 'other/abnormal world' which is
    # caused by the Inciting Incident"
    choice = input("You can choose 'v3': ")
    if choice == "v3":
        UserChoice.append(choice)
        print(UserChoice)
        v3()
    else:
        print("Test v2()-v3: Invalid choice!")

################################################################
###                         ACT 2                            ###
################################################################

# Node v3 is "Protagonist is taken to 'other/abnormal world' which is
# caused by the Inciting Incident 'v1' OR 'v2'"
def v3():
    # Node v4 is "Protagonist Wants to explore the new 'other/abnormal world'."
    # Node v5 is "Protagonist wants to imediately find their way back Home"
    choice = input("You can choose 'v4' or 'v5': ")
    if choice == "v4":
        UserChoice.append(choice)
        print(UserChoice)
        v4()
    elif choice == "v5":
        UserChoice.append(choice)
        print(UserChoice)
        v5()
    else:
        print("Test v4 and v5: Invalid choice!")

# Node v4 is "Protagonist Wants to explore the new 'other/abnormal world'."
def v4():
    # Node v6 is "There is no Love Interest character in story."
    # Node v7 is "Protagonist meets Love Interest charecter."
    choice = input("You can choose 'v6' or 'v7': ")
    if choice == "v6":
        UserChoice.append(choice)
        print(UserChoice)
        v6()
    elif choice == "v7":
        UserChoice.append(choice)
        print(UserChoice)
        v7()
    else:
        print("Test v4()-v6 and v4()-v7: Invalid choice!")

# Node v5 is "Protagonist wants to imediately find their way back Home"
def v5():
    # Node v6 is "There is no Love Interest character in story."
    # Node v7 is "Protagonist meets Love Interest charecter."
    choice = input("You can choose 'v6' or 'v7': ")
    if choice == "v6":
        UserChoice.append(choice)
        print(UserChoice)
        v6()
    elif choice == "v7":
        UserChoice.append(choice)
        print(UserChoice)
        v7()
    else:
        print("Test v5()-v6 and v5()-v7: Invalid choice!")

# Node v6 is "There is no Love Interest character in story."
def v6():
    # Node v8 is "Protagonist learns about the 'other/abnormal world' that they are in."
    choice = input("You can choose 'v8': ")
    if choice == "v8":
        UserChoice.append(choice)
        print(UserChoice)
        v8()
    else:
        print("Test v6()-v8: Invalid choice!")

# Node v7 is "Protagonist meets Love Interest charecter."
def v7():
    # Node v8 is "Protagonist learns about the 'other/abnormal world' that they are in."
    choice = input("You can choose 'v8': ")
    if choice == "v8":
        UserChoice.append(choice)
        print(UserChoice)
        v8()
    else:
        print("Test v7()-v8: Invalid choice!")

# Node v8 is "Protagonist learns about the 'other/abnormal world' that they are in."
def v8():
    # Node v9 is "Midpoint: Protagonist Frustration of 'other/abnormal world' predicament."5
    choice = input("You can choose 'v9': ")
    if choice == "v9":
        UserChoice.append(choice)
        print(UserChoice)
        v9()
    else:
        print("Test v9: Invalid choice!")

# Node v9 is "Midpoint: Protagonist Frustration of 'other/abnormal world' predicament."
def v9():
    # Node v10 is "The Threat to the Protagonist becomes evidently more clear"
    choice = input("You can choose 'v10': ")
    if choice == "v10":
        UserChoice.append(choice)
        print(UserChoice)
        v10()
    else:
        print("Test v9: Invalid choice!")

# Node v10 is "The Threat to the Protagonist becomes evidently more clear"
def v10():
    # Node v11 is "Climax: The result of what happens to Protagonist from previous Event."
    choice = input("You can choose 'v11': ")
    if choice == "v11":
        UserChoice.append(choice)
        print(UserChoice)
        v11()
    else:
        print("Test v11: Invalid choice!")

################################################################
###                         ACT 3                            ###
################################################################

# Node v11 is "Climax: The result of what happens to Protagonist from previous Event."
def v11():
    if 'v7' in UserChoice:
        # Node v13 is "Ending 2: Get Home, with Love Interest"
        # Node v15 is "Ending 4: Get Home, but Love Interest must or is left behind
        # in the other/abnormal world."
        choice = input("You can choose 'v13' or 'v15': ")
        if choice == "v13":
            UserChoice.append(choice)
            print(UserChoice)
            print("You have reached the end of Voyage and Return Branch")
        elif choice == "v15":
            UserChoice.append(choice)
            print(UserChoice)
            print("You have reached the end of Voyage and Return Branch")
        else:
            print("Test v11()-v13 and v11()-v13: Invalid Choice")
    elif 'v6' in UserChoice:
        # Node v12 is "Ending 1: Get Home, with a happy ending."
        # Node v14 is "Ending 3: Get Home with Protagonist negatively changed.
        # OR Protagonist ends up trapped in the other/abnormal world."
        choice = input("You can choose 'v12' or 'v14': ")
        if choice == "v12":
            UserChoice.append(choice)
            print(UserChoice)
            print("You have reached the end of Voyage and Return Branch")
        elif choice == "v14":
            UserChoice.append(choice)
            print(UserChoice)
            print("You have reached the end of Voyage and Return Branch")
        else:
            print("Test v11()-v13 and v11()-v13: Invalid Choice")
    else:
        print("Honestly don't think this Test Print can happen...")

################################################################
###          Voyage and Return Branch Code Finished          ###
################################################################

################################################################
###                                                          ###
###                    Start of Program                      ###
###                                                          ###
################################################################

#Presents user with Root choices of a, b, or c. Dependent on choice, will call it's associated Function
RootChoice = input("Choose a, q or v: ")
if RootChoice == "a":
    A_Chain(RootChoice) # Goes to Adventure Branch Code
elif RootChoice == "q":
    Q_Chain(RootChoice) # Goes to Quest Branch Code
elif RootChoice == "v":
    VandR_Chain(RootChoice) # Goes to Voyage and return Branch Code
else:
    print("SORRY! Invalid choice!") # error handler... kinda
