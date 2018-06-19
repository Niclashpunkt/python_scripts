def printRange(input_range):

    input_int = int(input_range)

    for i in range(input_int):
        print(i)


def i():

    user_input = input("Please define a range:\n")

    if user_input.isdigit():

        printRange(user_input)


    else:

        while not user_input.isdigit():

            print("\nPlease enter integer values only!")
            user_input = input("Please define a range:\n")

        printRange(user_input)
