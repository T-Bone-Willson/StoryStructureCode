# users choice stored in an empty list.
UserChoice = []

# Diciontary for Key Nodes and their corresponding Edges
graph_elements = {"a" : ["a1", "a2"],
         "a1" : ["a3"],
         "a3" : ["a4", "a5"],
         "a4" : [], # Key will be empty since there are no more nodes connected to it
         "a5" : [],
         "a2" : ["ab1"],
         "ab1" : ["ab2"],
         "ab2" : [],
         "b" : ["b1", "b2"],
         "b1" : ["ab1"],
         "b2" : ["b3"],
         "b3" : ["b4"],
         "b4" : [],
         "c" : ["c1"],
         "c1" : ["c2"],
         "c2" : ["c3"],
         "c3" : []
         }

class graph:
    def __init__(self, graph_dictionary = None):
        if graph_dictionary is None:
            graph_dictionary = [] # sets graph_dictionary to an empty list
        self.graph_dictionary = graph_dictionary

# Get the keys of the dictionary
    def getNodes(self):
        return list(self.graph_dictionary.keys()) # "Keys()" method returns a list of
                                                  # all avaliable keys in a dictionary

# Find list of edges
    def getEdges(self):
        edge_name = []
        for node in self.graph_dictionary:
            for next_node in self.graph_dictionary[node]:
                if {next_node, node} not in edge_name:
                    edge_name.append({node, next_node})
        return edge_name

# "g" is assigned the graph element values from the class graph
g = graph(graph_elements) # name of the Dictionary

#Print test statement
print(g.getNodes()) # Print all nodes in graph
print(g.getEdges()) # print all edges within graph

################################################################
###                                                          ###
###                A Branch Function Code                    ###
###                                                          ###
################################################################

# The following 5 functions belong to the "a" Branch of choices
# Start of A branch chain. Triggerd by User making choice "a" at start of program.
def A_Chain(RootChoice):
    UserChoice.append("a") # Adds Branch root to List
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

def a1():
    choice = input("You can choose 'a3': ")
    if choice == "a3":
        UserChoice.append(choice)
        print(UserChoice)
        a3()
    else:
        print("Test a3: Invalid choice!")

def a3():
    choice = input("You can choose 'a4' or 'a5': ")
    if choice == "a4":
        UserChoice.append(choice)
        print(UserChoice)
        print("You have reached the end of this branch!")
    elif choice == "a5":
        UserChoice.append(choice)
        print(UserChoice)
        print("You have reached the end of this branch!")
    else:
        print("Test a4 and a5: Invalid choice!")

def a2():
    choice = input("You can choose 'ab1': ")
    if choice == "ab1":
        UserChoice.append(choice)
        print(UserChoice)
        ab1()
    else:
        print("Test ab1: Invalid choice")

def ab1():
    choice = input("You can choose 'ab2': ")
    if choice == "ab2":
        UserChoice.append(choice)
        print(UserChoice)
        print("You have reached the end of this branch!")
    else:
        print("Test ab2: Invalid choice!")

################################################################
###                                                          ###
###                B Branch Function Code                    ###
###                                                          ###
################################################################

# The following 5 functions belong to the "b" Branch of choices
# Start of B branch chain. Triggerd by User making choice "b" at start of program.
def B_Chain(RootChoice):
    UserChoice.append("b") # Adds Branch root to List
    choice = input("You can choose 'b1 or 'b2': ")
    if choice == "b1":
        UserChoice.append(choice)
        print(UserChoice)
        b1()
    elif choice == "b2":
        UserChoice.append(choice)
        print(UserChoice)
        b2()
    else:
        print("Test b1 and b2: Invalid choice!")

def b1():
    choice = input("You can choose 'ab1': ")
    if choice == "ab1":
        UserChoice.append(choice)
        print(UserChoice)
        ab1()
    else:
        print("Test ab1: Invalid choice!")

def ab1():
    choice = input("You can choose 'ab2': ")
    if choice == "ab2":
        UserChoice.append(choice)
        print(UserChoice)
        print("You have reached the end of this branch!")
    else:
        print("Test ab2: Invalid choice!")

def b2():
    choice = input("You can choose 'b3': ")
    if choice == "b3":
        UserChoice.append(choice)
        print(UserChoice)
        b3()
    else:
        print("Test b3: Invalid choice!")

def b3():
    choice = input("You can choose 'b4': ")
    if choice == "b4":
        UserChoice.append(choice)
        print(UserChoice)
        print("You have reached the end of this branch!")
    else:
        print("Test b4: Invalid choice!")

################################################################
###                                                          ###
###                C Branch Function Code                    ###
###                                                          ###
################################################################

# The following 3 functions belong to the "c" Branch of choices
# Start of C branch chain. Triggerd by User making choice "C" at start of program.
def C_Chain(RootChoice):
    UserChoice.append("c") # Adds Branch root to List
    choice = input("You can choose 'c1': ")
    if choice == "c1": # player needs to input this in order to proceed through branch
        UserChoice.append(choice)
        print(UserChoice)
        c1() # Triggers c1() function. Traverse deeper down C Branch.
    else:
        print("Test 1")

def c1():
    choice = input("You can choose 'c2': ")
    if choice == "c2":
        UserChoice.append(choice)
        print(UserChoice)
        c2() # Triggers c2() function. Traverse deeper down the C Branch
    else:
        print("Test 2")

def c2():
    choice = input("You can choose 'c3': ")
    if choice == "c3":
        UserChoice.append(choice)
        print(UserChoice)
        print("You have reached the end of this branch!")
    else:
        print("Test 3")

################################################################
###                                                          ###
###                    Start of Program                      ###
###                                                          ###
################################################################

#Presents user with Root choices of a, b, or c. Dependent on choice, will call it's associated Function
RootChoice = input("Choose a, b or c: ")
if RootChoice == "a":
    A_Chain(RootChoice) # Goes to A branch funtion chains
elif RootChoice == "b":
    B_Chain(RootChoice) # Goes to B branch function chains
elif RootChoice == "c":
    C_Chain(RootChoice) # Goes to C branch function chains
else:
    print("SORRY! Invalid choice!") # error handler... kinda
