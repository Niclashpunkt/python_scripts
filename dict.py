dictA_N = {}
dictO_Z = {}

def d():
    # dataNiclas = {"name":"niclas", "age":"20", "origin":"hamburg"}
    # data = {"name":"niclas", "age":"20"}

    dict = {"name":"niclas", "age":"20", "origin":"hamburg"}
    print(dict.keys())

# def writeFile(dict):
#


def addValue(word_input):

    # print("addValue()")
    value_input = input("Please provide a definition for this word: ")

    if word_input[0].lower() <= "n":

        dictA_N.update({word_input : value_input})
        print("Word successfully added to A-N Dictionary")
        print(dictA_N)

    else:
        dictO_Z.update({word_input : value_input})
        print("Word successfully added to O-Z Dictionary")
        print(dictO_Z)

def alphaDict():

    word_input = input("Please provide a term you would like to add to the dictionary (If your term has spaces, wrap it in quotation marks): ")

    if word_input.isalpha():

        # print("Input is a word")
        # value_input = input("Please provide a definition for this word: ")
        addValue(word_input)

    else:

        while not word_input.isalpha():
            #
            print("\nPlease enter letters only!")
            word_input = input("Please provide a term you would like to add to the dictionary (If your term has spaces, wrap it in quotation marks): ")

        # new_def = input("Press y if you want to provide a new definition: ")
        #
        # if new_def == "Y" or new_def == "y":
        #     value_input = input("Please provide a new definition: ")

            addValue(word_input)




alphaDict()
