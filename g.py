def greeting(name, currentTime):

    import time

    if currentTime is "":
        currentTime = int(time.strftime("%H"))

    currentTime = int(currentTime)

    if currentTime < 14:
        print("Have a nice day, "+name+"!")

    elif currentTime > 13:
        print("Bonsoir, "+name+"!")
