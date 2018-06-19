import time

def greeting(name, currentTime):

    if currentTime is "":
        currentTime = int(time.strftime("%H"))

    currentTime = int(currentTime)

    if currentTime < 14:
        print("Have a nice day, "+name+"!")

    else:
        print("Bonsoir, "+name+"!")

greeting("Niclas","")
