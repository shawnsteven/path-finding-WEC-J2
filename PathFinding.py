# WEC Competition - Rhys, Anh, Shawn


# from typing_extensions import Unpack


dimension = "3 3"
botCoord = "0 0"
userCoord = "2 2"
obstacleArray = ""
itemCoord =  ""

# set up variables
usedArray = []
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

# function to output


def outputCoords(botPath, numMoves):
    botPath = botPath[:-2]
    print(botPath)
    print(numMoves)

# function to check whether a move is legal


def checkMove(moveCoord, obstacleArray):
    for i in range(0, len(obstacleArray), 2):
        # want to check if moveCoord is in obstacleArray
        if( obstacleArray[0] == ""):
            return True

        if(moveCoord[0] == obstacleArray[i] and moveCoord[1] == obstacleArray[i+1]):
            return False
            
    return True


def xMoveRight(testBotCoords, obstacleArrayList):
    testBotCoords[0] += 1
    if(checkMove(testBotCoords, obstacleArrayList)):
        obstacleArrayList += testBotCoords
        return True
    else:
        testBotCoords[0] -= 1
        return False


def xMoveLeft(testBotCoords, obstacleArrayList):
    testBotCoords[0] -= 1
    if(checkMove(testBotCoords, obstacleArrayList)):
        obstacleArrayList += testBotCoords
        return True
    else:
        testBotCoords[0] += 1
        return False


def yMoveDown(testBotCoords, obstacleArrayList):
    testBotCoords[1] += 1
    if(checkMove(testBotCoords, obstacleArrayList)):
        obstacleArrayList += testBotCoords
        return True
    else:
        testBotCoords[1] -= 1
        return False


def yMoveUp(testBotCoords, obstacleArrayList):
    testBotCoords[1] -= 1
    if(checkMove(testBotCoords, obstacleArrayList)):
        obstacleArrayList += testBotCoords
        return True
    else:
        testBotCoords[1] += 1
        return False

# main function


def path_Finding(botPath, numMoves, botCoordList):

    testBotCoords = botCoordList
    xDifference = int(botCoordList[0]) - int(userCoordList[0])
    yDifference = int(botCoordList[1]) - int(userCoordList[1])

    # to move horizontal
    if(botCoordList == userCoord):
        return True

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
    else:
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

    # adding to the final output
    botPath += (str(botCoordList[0]) + " " + str(botCoordList[1]) + ", ")
    numMoves += 1
    # once path has been found run the print function


if(path_Finding(botPath, numMoves, botCoordList)):
    print(outputCoords(botPath, numMoves))
