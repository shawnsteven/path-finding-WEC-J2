# WEC Competition - Rhys, Anh, Shawn


# from typing_extensions import Unpack


dimension = "6 8"
botCoord = "2 6"
userCoord = "3 5"
obstacleArray = "2 1 4 2 1 3 3 3 1 5 1 6 2 5 4 5 4 6"
itemCoord = "3 2"

# set up variables
gotItem = False
usedArray = []
testBotCoords = []
numMoves = -1
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
if(itemCoordList[0] != ""):
    for i in range(0, len(itemCoordList)):
        itemCoordList[i] = int(itemCoordList[i])
else:
    gotItem = True
# function to output


def outputCoords(botPath, numMoves):
    botPath = botPath[:-2]
    print(botPath)
    print(numMoves)

# function to check whether a move is legal


def checkMove(moveCoord, obstacleArray, gotItem):
    for i in range(0, len(obstacleArray), 2):
        # want to check if moveCoord is in obstacleArray
        if(obstacleArray[0] == ""):
            return True

        if(moveCoord[0] == obstacleArray[i] and moveCoord[1] == obstacleArray[i+1]):
            return False

    if(gotItem == False):
        if(moveCoord[0] == userCoordList[0] and moveCoord[1] == userCoordList[1]):
            return False

    if(moveCoord[0] == itemCoordList[0] and moveCoord[1] == itemCoordList[1]):
        gotItem = True

    return True


def xMoveRight(testBotCoords, obstacleArrayList):
    testBotCoords[0] += 1
    if(checkMove(testBotCoords, obstacleArrayList, gotItem)):
        obstacleArrayList += testBotCoords
        return True
    else:
        testBotCoords[0] -= 1
        return False


def xMoveLeft(testBotCoords, obstacleArrayList):
    testBotCoords[0] -= 1
    if(checkMove(testBotCoords, obstacleArrayList, gotItem)):
        obstacleArrayList += testBotCoords
        return True
    else:
        testBotCoords[0] += 1
        return False


def yMoveDown(testBotCoords, obstacleArrayList):
    testBotCoords[1] += 1
    if(checkMove(testBotCoords, obstacleArrayList, gotItem)):
        obstacleArrayList += testBotCoords
        return True
    else:
        testBotCoords[1] -= 1
        return False


def yMoveUp(testBotCoords, obstacleArrayList):
    testBotCoords[1] -= 1
    if(checkMove(testBotCoords, obstacleArrayList, gotItem)):
        obstacleArrayList += testBotCoords
        return True
    else:
        testBotCoords[1] += 1
        return False

# main function


def path_Finding(botPath, numMoves, botCoordList):

    gotItem = False
    testBotCoords = botCoordList

    botPath += (str(botCoordList[0]) + " " + str(botCoordList[1]) + ", ")
    numMoves += 1

    if(botCoordList[0] == itemCoordList[0] and botCoordList[1] == itemCoordList[1]):
        gotItem = True

    if(gotItem):
        xDifference = int(botCoordList[0]) - int(userCoordList[0])
        yDifference = int(botCoordList[1]) - int(userCoordList[1])
    else:
        xDifference = int(botCoordList[0]) - int(itemCoordList[0])
        yDifference = int(botCoordList[1]) - int(itemCoordList[1])

    if(abs(xDifference) > abs(yDifference)):
        if(xDifference > 0):
            if(xMoveLeft(testBotCoords, obstacleArrayList) == True):
                return(path_Finding(botPath, numMoves, botCoordList))
            elif(yDifference > 0):
                if(yMoveUp(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
                elif(yMoveDown(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
                elif(xMoveRight(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
                else:
                    return False
            else:
                if(yMoveDown(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
                elif(yMoveUp(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
                elif(xMoveRight(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
        if(xDifference < 0):
            if(xMoveRight(testBotCoords, obstacleArrayList) == True):
                return(path_Finding(botPath, numMoves, botCoordList))
            elif(yDifference > 0):
                if(yMoveUp(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
                elif(yMoveDown(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
                elif(xMoveLeft(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
            else:
                if(yMoveDown(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
                elif(yMoveUp(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
                elif(xMoveLeft(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
    elif(abs(yDifference) > abs(xDifference)):
        if(yDifference > 0):
            if(yMoveUp(testBotCoords, obstacleArrayList) == True):
                return(path_Finding(botPath, numMoves, botCoordList))
            elif(xDifference > 0):
                if(xMoveLeft(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
                elif(xMoveRight(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
                elif(yMoveDown(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
            else:
                if(xMoveRight(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
                elif(xMoveLeft(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
                elif(yMoveDown(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
        if(yDifference < 0):
            if(yMoveDown(testBotCoords, obstacleArrayList) == True):
                return(path_Finding(botPath, numMoves, botCoordList))
            elif(xDifference > 0):
                if(xMoveLeft(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
                elif(xMoveRight(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
                elif(yMoveUp(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
            else:
                if(xMoveRight(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
                elif(xMoveLeft(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
                elif(yMoveUp(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
    else:
        if(xDifference > 0):
            if(xMoveLeft(testBotCoords, obstacleArrayList) == True):
                return(path_Finding(botPath, numMoves, botCoordList))
            elif(yDifference > 0):
                if(yMoveUp(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
                elif(yMoveDown(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
                elif(xMoveRight(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
                else:
                    return False
            else:
                if(yMoveDown(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
                elif(yMoveUp(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
                elif(xMoveRight(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
        if(xDifference < 0):
            if(xMoveRight(testBotCoords, obstacleArrayList) == True):
                return(path_Finding(botPath, numMoves, botCoordList))
            elif(yDifference > 0):
                if(yMoveUp(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
                elif(yMoveDown(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
                elif(xMoveLeft(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
            else:
                if(yMoveDown(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
                elif(yMoveUp(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))
                elif(xMoveLeft(testBotCoords, obstacleArrayList) == True):
                    return(path_Finding(botPath, numMoves, botCoordList))

    # adding to the final output
    botPath += (str(botCoordList[0]) + " " + str(botCoordList[1]) + ", ")
    print()
    print(botPath[5:-7])
    print(numMoves)


path_Finding(botPath, numMoves, botCoordList)
