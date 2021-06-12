# WEC Competition - Rhys, Anh, Shawn

def outputCoords(botPath, numMoves):
    botPath = botPath[:-2]
    print(botPath)
    print(numMoves)


def checkMove(moveCoord, obstacleArray):
    for i in range(0, len(obstacleArray), 2):

        # want to check if moveCoord is in obstacleArray
        if(moveCoord[0] == obstacleArray[i] and moveCoord[1] == obstacleArray[i+1]):
            return False

    else:
        return True


def xMove(xDifference, testBotCoords, obstacleArrayList):
    if(xDifference > 0):
        testBotCoords[0] -= 1
        if(checkMove(testBotCoords, obstacleArrayList)):
            return True
        else:
            testBotCoords[0] += 1
            return False
    else:
        testBotCoords[0] += 1
        if(checkMove(testBotCoords, obstacleArrayList)):
            return True
        else:
            testBotCoords[0] -= 1
            return False


def yMove(yDifference, testBotCoords, obstacleArrayList):
    if(yDifference > 0):
        testBotCoords[1] -= 1
        if(checkMove(testBotCoords, obstacleArrayList)):
            return True
        else:
            testBotCoords[1] += 1
            return False
    else:
        testBotCoords[1] += 1
        if(checkMove(testBotCoords, obstacleArrayList)):
            return True
        else:
            testBotCoords[1] -= 1
            return False


def path_Finding(dimension, botCoord, userCoord, obstacleArray, itemCoord):

    # set up variables
    newBotCoords = []
    testBotCoords = []
    numMoves = 0
    botPath = ""
    reachedObjective = False

    # set up our variables into arrays
    dimensionList = dimension.split(" ")
    for i in range(0, len(dimensionList)):
        dimensionList[i] = int(dimensionList[i])

    botCoordList = botCoord.split(" ")
    for i in range(0, len(botCoordList)):
        botCoordList[i] = int(botCoordList[i])

    userCoordList = userCoord.split(" ")
    for i in range(0, len(userCoordList)):
        userCoordList[i] = int(userCoordList[i])

    obstacleArrayList = obstacleArray.split(" ")
    if(obstacleArrayList[0] != ""):
        for i in range(0, len(obstacleArrayList)):
            obstacleArrayList[i] = int(obstacleArrayList[i])

    itemCoordList = itemCoord.split(" ")

    # main loop
    while(not reachedObjective):
        testBotCoords = botCoordList
        xDifference = int(botCoordList[0]) - int(userCoordList[0])
        yDifference = int(botCoordList[1]) - int(userCoordList[1])

        # to move horizontal
        if(abs(xDifference) > abs(yDifference)):
            # if difference is positive, then the bot needs to move left
            if(xMove(xDifference, testBotCoords, obstacleArrayList)):
                botCoordList = testBotCoords
            elif(yMove(yDifference, testBotCoords, obstacleArrayList)):
                botCoordList = testBotCoords

        # to move vertical
        elif(abs(xDifference) < abs(yDifference)):
            # if difference is positive, then the bot needs to move up
            if(yMove(yDifference, testBotCoords, obstacleArrayList)):
                botCoordList = testBotCoords
            elif(xMove(xDifference, testBotCoords, obstacleArrayList)):
                botCoordList = testBotCoords

        # if both x and y differences are same then move in x direction (could be either)
        else:
            if(xMove(xDifference, testBotCoords, obstacleArrayList)):
                botCoordList = testBotCoords
            elif(yMove(yDifference, testBotCoords, obstacleArrayList)):
                botCoordList = testBotCoords

        botPath += (str(botCoordList[0]) + " " + str(botCoordList[1]) + ", ")
        numMoves += 1

        if(botCoordList == userCoordList):
            reachedObjective = True

    # once path has been found
    outputCoords(botPath, numMoves)


path_Finding("3 3", "0 0", "1 2", "0 1 0 2", " ")
