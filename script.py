__author__ = "Thomas Banas"
__copyright__ = "Copyright (C) 2017 Thomas Banas"
__license__ = "Public Domain"
__version__ = "1.0"

# The script assumes a set of preconditions:
# The text file is the same format as the one provided with the project directions specifically naming:
    # The ordering of the elements that make up a node in the text file:
        # #node_id is listed first, then #name, then #basetext, then #type,
        #  then #answer_names, and finally #additionaldata:result
    # The existence of a " " <space> after an element (i.e. #name:<space>Path 1 selected)

# OTHER NOTES:
# I took some liberties with the formatting of the output.
    # The way the script parses through the QuestionLabels, Answer Values, and Types,
    #  it needed 1 " " <space> after the QL,
               # 2 " " <spaces> after the AV,
               # 1 " " <space> after the Type
    #  to make the output look the same as how it should be according to the directions

# STRUCTURE
# The code is ready to handle the other elements (like #asset_id and #sub_type) with some additions.
# The main data structure I used is an array of type Node. If an array is improper or unwanted, the
#  Node class has a property nextNode and the get and set methods for the property. Some changes
#  would have to be made to accompany this change however.


class Node:
    def __init__(self, idOfNode):
        self.idOfNode = idOfNode

    def getIdOfNode(self):
        return self.idOfNode

    def setQuestionLabel(self, questionLabel):
        self.questionLabel = questionLabel

    def getQuestionLabel(self):
        return self.questionLabel

    def setAnswerValues(self, answerValues):
        self.answerValues = answerValues

    def getAnswerValues(self):
        return self.answerValues

    def setTypeOfNode(self, typeOfNode):
        self.typeOfNode = typeOfNode

    def getTypeOfNode(self):
        return self.typeOfNode

    # Next is currently unused
    def setNext(self, nextNode):
        self.next = nextNode

    def getNext(self):
        return self.next

def script():

    # Initialize array
    nodeList = []

    # Attempt to open the input text file
    with open("appliedpathways_input_file.txt", "r") as file:
        lines = file.read().split("#")
        for line in lines:
            # Splits the line into one or more parts (usually two)
            line = line.strip().split(" ")

            # Getting the ID and initializing the current Node
            if (line[0] == "node_id:"):
                # line[0] is node_id and line[1] is the number provided, i.e. 1199 for "Path 1 selected"
                n = Node(line[1])
                n.setQuestionLabel("")
                n.setAnswerValues("")
                n.setTypeOfNode("")
                # Add the node to the array
                nodeList.append(n)

            # Setting the Name aka the Question Label
            if (line[0] == "name:"):
                # line[1] in this case could be many words separated by spaces
                #  which is why the .join() method is necessary
                n.setQuestionLabel(" ".join(line[1:]))
            # Resetting the Name/Question Label to the #basetext if it exists for that node
            try:
                if (line[0] == "basetext:" and line[1]):
                    n.setQuestionLabel(" ".join(line[1:]))
            except IndexError:
                continue

            # Setting the Type
            if (line[0] == "type:"):
                n.setTypeOfNode(line[1])

            # Setting the Answer Values - Depends on the Type
            if (line[0] == "answer_names:"):
                if (n.getTypeOfNode() == "question/standard"):
                    n.setAnswerValues(" ".join(line[1:]))
            if (line[0] == "additionaldata:result:"):
                if (n.getTypeOfNode() == "expression"):
                    n.setAnswerValues(line[1])

        # Getting max lengths of the Question Labels, Answer Values, and Types for printing out the results
        maxQL = 0
        maxAV = 0
        maxT  = 0
        for n in nodeList:
            if (len(n.getQuestionLabel()) > maxQL):
                maxQL = len(n.getQuestionLabel())
            if (len(n.getAnswerValues()) > maxAV):
                maxAV = len(n.getAnswerValues())
            if (len(n.getTypeOfNode()) > maxT):
                maxT = len(n.getTypeOfNode())

        # Print title section of table
        print "+" + "-" * (maxQL + 2) + "+" + "-" * (maxAV + 2) + "+" + "-" * (maxT + 2) + "+"
        print "| Question Label" + " " * (maxQL - len("QuestionLabel")) + "| Answer Values " + " " * (maxAV - len("Answer Values")) + "| Type " + " " * (maxT - len("Type")) + "|"
        print "+" + "-" * (maxQL + 2) + "+" + "-" * (maxAV + 2) + "+" + "-" * (maxT + 2) + "+"

        #Print the data
        for n in nodeList:
            if (n.getTypeOfNode() != "stop"):
                print "| " + n.getQuestionLabel() + (maxQL - len(n.getQuestionLabel()) + 1) * " " + "| " + n.getAnswerValues() + (maxAV - len(n.getAnswerValues()) + 1) * " " + "| " + n.getTypeOfNode() + (maxT - len(n.getTypeOfNode()) + 1) * " " + "|"
            else:
                print "| Stop" + (maxQL - len("Stop") + 1) * " " + "| " + n.getAnswerValues() + (maxAV - len(n.getAnswerValues()) + 1) * " " + "| " + n.getTypeOfNode() + (maxT - len(n.getTypeOfNode()) + 1) * " " + "|"

        #Print bottom line
        print "+" + "-" * (maxQL + 2) + "+" + "-" * (maxAV + 2) + "+" + "-" * (maxT + 2) + "+"

    # Close the file
    file.close()


# Actually run the script
script()
