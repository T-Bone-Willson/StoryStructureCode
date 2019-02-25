


#Empty List for choices that user makes. Appended onto here
#UserChoice = []
#List of choices that can be made
#choices = ['a', 'a1', 'a2', 'a3', 'a4', 'a5', 'b', 'b1', 'b2', 'b3', 'b4', 'ab1', 'ab2', 'c', 'c1', 'c2', 'c3']
#################################################################

#Empty List to contain user input
UserChoice = []

ops = True
###
##
##
##
#Goes through C options
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
















###############################################################
#input variable
#dec = input("Please choose: ")

#Choices if-elif-else chain
#if dec == "c":
    #UserChoice.extend("c")
    #input("Your following options are: c1 ")
    #if dec == "c1":
        #UserChoice.extend("c1")
        #print(UserChoice)
        #input("Your following options are: c2 ")
        #if dec == "c2":
            #UserChoice.extend("c2")
            #print(UserChoice)
    #print(UserChoice)


#checking type of name
#print(type(dec))

#print("Test")

#pseudo code
#if choices == 'a':
