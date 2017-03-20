# appliedPathwaysInterviewScript

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
