# users choice stored in an empty list.
UserChoice = []

################################################################
###         Dictionary/Graph for Adventure, Quest and        ###
###                     Voyage & Return                      ###
################################################################

# Adventure Branch Code Dictionary
Adventure_Graph_Elements = {"a" : ["a1", "a2"],
                    "a1" : ["a3"],
                    "a2" : ["a3"],
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
Quest_Graph_Elements = {""



                    }


################################################################
###                                                          ###
###              Adventure Branch Function Code              ###
###                                                          ###
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
    # Node q2 is "Reason why Charecter wants Elixir"
    # Node q3 is "Inciting Incident"
    choice = input("You can choose 'q2' or 'q3': ")
    if choice == "q2": # player needs to input this in order to proceed through branch
        UserChoice.append(choice)
        print(UserChoice)
        q2()
    elif choice == "q3":
        UserChoice.append(choice)
        print(UserChoice)
        q3()
    else:
        print("Test q2 and q3: Invalid choice!")

# Node q2 is "Reason why Charecter wants Elixir"
def q2():
    # Node q3 is "Inciting Incident"
    choice = input("You can choose 'q3': ")
    if choice == "q3":
        UserChoice.append(choice)
        print(UserChoice)
        q3()
    else:
        print("Test q3: Invalid choice!")

# Node q3 is "Inciting Incident"
def q3():
    # Node q4 is "Don't gather 'buddies' for journey, Protagonist will journey alone"
    # Node q5 is "gather 'Buddies'", Protagoniost will journey with company
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

# Node q4 is "Don't gather 'buddies' for journey, Protagonist will journey alone"
def q4():
    # Node q6 is "Helper" will be present in the story.
    # Node q7 is "Commencing the Journey"
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

# Node q5 is "gather 'Buddies'", Protagoniost will journey with company
def q5():
    # Node q6 is "Helper" will be present in the story.
    # Node q7 is "Commencing the Journey"
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

# Node q6 is "Helper" will be present in the story.
def q6():
    # Node q7 is "Commencing the Journey"
    choice = input("You can choose 'q7': ")
    if choice == "q7":
        UserChoice.append(choice)
        print(UserChoice)
        q7()
    else:
        print("Test q7: Invalid choice!")

# Node q7 is "Commencing the Journey"
def q7():
    # Node q8 is "Event/Obstacle 1 in Journey"
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

# Node q8 is "Event/Obstacle 1 in Journey"
def q8():
    # Checks to see if element "q5" exist in UserChoice List
    # If so, it means branch chains q11 are unlocked
    # But also lets the User can down the  q9 and q10 path.
    if 'q5' in UserChoice:
        # Node q9 is "Event/Obstacle 1 in Journey has Failed"
        # Node q10 is "Event/Obstacle 1 in Journey has Passed"
        # Node q11 is "Event/Obstacle 1 is a 'Buddy' quest"
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
        # Node q9 is "Event/Obstacle 1 in Journey has Failed"
        # Node q10 is "Event/Obstacle 1 in Journey has Passed"
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

# Node q9 is "Event/Obstacle 1 in Journey has Failed"
def q9():
    # Node q15 is "Event 1 resolution"
    choice = input("You can choose 'q15': ")
    if choice == "q15":
        UserChoice.append(choice)
        print(UserChoice)
        q15()
    else:
        print("Test q9()-q15: Invalid choice!")

# Node q10 is "Event/Obstacle 1 in Journey has Passed"
def q10():
    # Node q15 is "Event 1 resolution"
    choice = input("You can choose 'q15': ")
    if choice == "q15":
        UserChoice.append(choice)
        print(UserChoice)
        q15()
    else:
        print("Test q10()-q15: Invalid choice!")

# Node q11 is "Event/Obstacle 1 is a 'Buddy' quest"
def q11():
    # Node q12 is "Buddy Quest 1 Passed"
    # Node q13 is "Buddy Quest 1 Failed"
    choice = input("You can choose 'q12' or 'q13': ")
    if choice == "q12":
        UserChoice.append(choice)
        print(UserChoice)
        q12()
    elif choice == "q13":
        UserChoice.append(choice)
        print(UserChoice)
        q13()
    else:
        print("Test q12 and q13: Invalid choice!")

# Node q12 is "Buddy Quest 1 Passed"
def q12():
    # Node q14 is "Resolution of Buddy Quest 1"
    choice = input("You can choose q14: ")
    if choice == "q14":
        UserChoice.append(choice)
        print(UserChoice)
        q14()
    else:
        print("Test q12()-q14(): Invalid choice!")

# Node q13 is "Buddy Quest 1 Failed"
def q13():
    # Node q14 is "Resolution of Buddy Quest 1"
    choice = input("You can choose 'q14': ")
    if choice == "q14":
        UserChoice.append(choice)
        print(UserChoice)
        q14()
    else:
        print("Test q13()-q14(): Invalid choice!")

# Node q14 is "Resolution of Buddy Quest 1"
def q14():
    # Node q15 is "Event 1 resolution"
    choice = input("You can choose 'q15': ")
    if choice == "q15":
        UserChoice.append(choice)
        print(UserChoice)
        q15()
    else:
        print("Test q14()-q15: Invalid choice!")

# Node q15 is "Event 1 resolution"
def q15():
    # Node q16 is "Journey to Act 3 OR Start of Event/Obstacle 2 in Journey"
    choice = input("You can choose 'q16': ")
    if choice == "q16":
        UserChoice.append(choice)
        print(UserChoice)
        q16()
    else:
        print("Test q16: Invalid choice!")

# Node q16 is "Journey to Act 3 OR Start of Event/Obstacle 2 in Journey"
def q16():
    # Node q17 is "Event/Obstacle 2 in Journey"
    # Node q34 is "Starts Act 3"
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

# Node q17 is "Event/Obstacle 2 in Journey"
# this Node reiterates the previous branch choices.
def q17():
    # Checks to see if element "q5" exist in UserChoice List
    # If so, it means branch chains q20 are unlocked
    # But also lets the User can down the q18 and q19 path.
    if 'q5' in UserChoice:
        # Node q18 is "Event/Obstacle 2, Passed, in Journey"
        # Node q19 is "Eevnt/Obstacle 2, Failed, in Journey"
        # Node q20 is "Event/Obstacle 2. Buddy Quest 2, In Journey"
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
        # Node q18 is "Event/Obstacle 2, Passed, in Journey"
        # Node q19 is "Eevnt/Obstacle 2, Failed, in Journey"
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

# Node q18 is "Event/Obstacle 2, Passed, in Journey"
def q18():
    # Node q24 is "Event 2 In Journey, Resolution"
    choice = input("You can choose 'q24': ")
    if choice == "q24":
        UserChoice.append(choice)
        print(UserChoice)
        q24()
    else:
        print("Test q18()-q24: Invalid choice!")

# Node q19 is "Eevnt/Obstacle 2, Failed, in Journey"
def q19():
    # Node q24 is "Event 2 In Journey, Resolution"
    choice = input("You can choose 'q24': ")
    if choice == "q24":
        UserChoice.append(choice)
        print(UserChoice)
        q24()
    else:
        print("Test q19()-q24: Invalid choice!")

# Node q20 is "Event/Obstacle 2. Buddy Quest 2, In Journey"
def q20():
    # Node q21 is "Buddy Quest 2, Passed"
    # Node q22 is "Buddy Quest 2, Failed"
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

# Node q21 is "Buddy Quest 2, Passed"
def q21():
    # Node q23 is "Resolution from Buddy Quest 2"
    choice = input("You can choose 'q23': ")
    if choice == "q23":
        UserChoice.append(choice)
        print(UserChoice)
        q23()
    else:
        print("Test q21()-q23: Invalid choice!")

# Node q22 is "Buddy Quest 2, Failed"
def q22():
    # Node q23 is "Resolution from Buddy Quest 2"
    choice = input("You can choose 'q23': ")
    if choice == "q23":
        UserChoice.append(choice)
        print(UserChoice)
        q23()
    else:
        print("Test q22()-q23: Invalid choice!")

# Node q23 is "Resolution from Buddy Quest 2"
def q23():
    # Node q24 is "Event 2 In Journey, Resolution"
    choice = input("You can choose 'q24': ")
    if choice == "q24":
        UserChoice.append(choice)
        print(UserChoice)
        q24()
    else:
        print("Test q23()-q24: Invalid choice!")

# Node q24 is "Event 2 In Journey, Resolution"
def q24():
    # Node q25 is "Journey to Act 3 or Event/Obstacle 3 in Journey"
    choice = input("You can choose 'q25': ")
    if choice == "q25":
        UserChoice.append(choice)
        print(UserChoice)
        q25()
    else:
        print("Test q24: Invalid choice!")

# Node q25 is "Journey to Act 3 or Event/Obstacle 3 in Journey"
def q25():
    # Node q26 is "Event/Obstacle 3 in Journey"
    # Node q34 is "Starts Act 3"
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

# Node q26 is "Event/Obstacle 3 in Journey"
def q26():
    # Checks to see if element "q5" exist in UserChoice List
    # If so, it means branch chains q29 are unlocked
    # But also lets the User can down the q27 and q28 path.
    if 'q5' in UserChoice:
        # Node q27 is "Event/Obstacle 3, Passed, in Journey"
        # Node q28 is "Event/Obstacle 3, Failed, in Journey"
        # Node q29 is "Buddy Quest 3 Event/Obstacle"
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
        # Node q27 is "Event/Obstacle 3, Passed, in Journey"
        # Node q28 is "Event/Obstacle 3, Failed, in Journey"
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

# Node q27 is "Event/Obstacle 3, Passed, in Journey"
def q27():
    # Node q33 is "Resolution from Event/Obstacle 3 in Journey"
    choice = input("You can choose 'q33': ")
    if choice == "q33":
        UserChoice.append(choice)
        print(UserChoice)
        q33()
    else:
        print("Test q27()-q33: Invalid choice!")

# Node q28 is "Event/Obstacle 3, Failed, in Journey"
def q28():
    # Node q33 is "Resolution from Event/Obstacle 3 in Journey"
    choice = input("You can choose 'q33': ")
    if choice == "q33":
        UserChoice.append(choice)
        print(UserChoice)
        q33()
    else:
        print("Test q28()-q33: Invalid choice!")

# Node q29 is "Buddy Quest 3 Event/Obstacle"
def q29():
    # Node q30 is "Buddy Quest 3, Passed"
    # Node q31 is "Buddy Quest, Failed"
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

# Node q30 is "Buddy Quest 3, Passed"
def q30():
    # Node q32 is "Resolution from Bussy Quest 3"
    choice = input("You can choose 'q32': ")
    if choice == "q32":
        UserChoice.append(choice)
        print(UserChoice)
        q32()
    else:
        print("Test q30()-q32: Invalid choice!")

# Node q31 is "Buddy Quest, Failed"
def q31():
    # Node q32 is "Resolution from Bussy Quest 3"
    choice = input("You can choose 'q32': ")
    if choice == "q32":
        UserChoice.append(choice)
        print(UserChoice)
        q32()
    else:
        print("Test q31()-q32: Invalid choice!")

# Node q32 is "Resolution from Bussy Quest 3"
def q32():
    # Node q33 is "Resolution from Event/Obstacle 3 in Journey"
    choice = input("You can choose 'q33': ")
    if choice == "q33":
        UserChoice.append(choice)
        print(UserChoice)
        q33()
    else:
        print("Test q32()-q33: Invalid choice!")

# Node q33 is "Resolution from Event/Obstacle 3 in Journey"
def q33():
    # Node q34 is "Starts Act 3"
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

# Node q34 is "Starts Act 3"
def q34():
    # Node q35 is "Event that leds to 'Revelation'"
    # Node q36 is "Revelation: True nature of the Elixir"
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

# Node q35 is "Event that leds to 'Revelation'"
def q35():
    # Node q36 is "Revelation: True nature of the Elixir"
    choice = input("You can choose 'q36': ")
    if choice == "q36":
        UserChoice.append(choice)
        print(UserChoice)
        q36()
    else:
        print("Test q35()-q36: Invalid choice!")

# Node q36 is "Revelation: True nature of the Elixir"
def q36():
    # Node q37 is "Protagonist gets Elixir"
    # Node q38 is "Protagonist doesn't get Elixir"
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

# Node q37 is "Protagonist gets Elixir"
def q37():
    # Node q39 is "Protagonist has negative charecter development change from Elixir Node Choice"
    # Node q40 is "Protagonist has positive charecter development change from Elixir Node Choice"
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

# Node q38 is "Protagonist doesn't get Elixir"
def q38():
    # Node q39 is "Protagonist has negative charecter development change from Elixir Node Choice"
    # Node q40 is "Protagonist has positive charecter development change from Elixir Node Choice"
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

# Node q39 is "Protagonist has negative charecter development change from Elixir Node Choice"
def q39():
    # Node q41 "Protagonist goes Home"
    # Node q42 "Protagonist doesn't go Home"
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

# Node q40 is "Protagonist has positive charecter development change from Elixir Node Choice"
def q40():
    # Node q41 "Protagonist goes Home"
    # Node q42 "Protagonist doesn't go Home"
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
