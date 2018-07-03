list1 = ["hello", 75, False]
list2 = [4,8,"sechszehn"]
intList = [64,128,16,32,8]

def lists():



    print("  list1:")
    prntLst(list1)
    print("  list2:")
    prntLst(list2)



    list1.extend(list2)

    print("  longList: ")
    prntLst(list1)

def sort():

    for i in list1:
        str(i)
        
    print("sortedList:", list1)
    # list1.sort()
    # prntLst(list1)

# lists()
sort()
