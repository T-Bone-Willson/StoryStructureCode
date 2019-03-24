# users choice stored in an empty list.
UserChoice = []

TemplateList = []

def A_Chain(RootChoice):
    # Node a is "Home: Protagonist is there and they want the Elixir"
    UserChoice.append("a") # Adds Branch root to List
    a = "a: Protagonist starts at Home\n"
    TemplateList.append(a)

    # Node a1 is "Elixir: It is inanimate object"
    # Node a2 is "Elixir: Is another charecter"
    choice = input("You can choose 'a1' or 'a2': ")
    if choice == "a1": # player needs to input this in order to proceed through branch
        UserChoice.append(choice)
        #a1 == "a1: The Elixir is an object"
        TemplateList.append(str("Elixir: It is inanimate object\n"))
        print(UserChoice)
        a1()
    elif choice == "a2": # Will unlock a2() function/branch.
        UserChoice.append(choice)
        #a2 == "a2: The Elixir is a person"
        TemplateList.append(str("The Elixir is a person\n"))
        print(UserChoice)
        a2()
    else:
        print("Test a1 and a2: Invalid choice!")

def a1():
    print("")
    for elem in TemplateList:
        print(elem)

def a2():
    print("")
    for elem in TemplateList:
        print(elem)

RootChoice = input("Choose a: ")
if RootChoice == "a":
    A_Chain(RootChoice) # Goes to Adventure Branch Code
else:
    print("You failed")
