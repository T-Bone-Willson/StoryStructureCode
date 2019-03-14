# users choicec stored in an empty list.
UserChoice = []

# Diciontary for Key Nodes and their corresponding Edges
graph_elements = {"a" : ["a1", "a2"],
         "a1" : ["a3"],
         "a3" : ["a4", "a5"],
         "a4" : [], #Key will be empty since there are no more nodes connected to it
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
g = graph(graph_elements)

#Print test statement
print(g.getNodes()) # Print all nodes in graph
print(g.getEdges()) # print all edges within graph

#def Cdecision(self, RootChoice = 'c'):
#    opsC = True
#    while opsC:
#        choice = input("You can choose 'c': ")
#        if choice == "c":
#            UserChoice.append(choice)
#            self.graph_dictionary.key()
#            if self.graph_dictionary.key() == "c":
#                choice = input("You can choose 'c1': ")
#                UserChoice.append(choice)
#                self.graph_dictionary.key()
#                if self.graph_dictionary.key() == "c1":
#                    choice = input("You can choose 'c2': ")
#                    UserChoice.append(choice)
#                    self.graph_dictionary.key()
#                    if self.graph_dictionary.key() == "c2":
#                        choice = input("You can choose 'c3': ")
#                        UserChoice.append(choice)
#                        self.graph_dictionary.key()
#                        print(UserChoice)
#                        print(g.Cdecision())
#        else:
#            print("Wrong Input!")

def C_Chain(RootChoice):
    UserChoice.append("c")
    print(UserChoice)






#Presents user with Root choices of a, b, or c. Dependent on choice, will call it's associated Function
RootChoice = input("Choose a, b or c: ")
#if RootChoice == "a":
    #Adecision(RootChoice)
#elif RootChoice == "b":
    #Bdecision(RootChoice)
if RootChoice == "c":
    C_Chain(RootChoice)
else:
    print("SORRY! Invalid choice!")
