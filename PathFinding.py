# WEC Competition - Rhys, Anh, Shawn


dimension = input("Dimension: ")
botCoord = input("Robot's coordinates: ")
userCoord = input("User's coordinates: ")
obstacleArray = input("Array of obstacle: ")
itemCoord = input("Item's coordinates: )

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

#function to check whether a move is legal
def checkMove(moveCoord, obstacleArray):
    for i in range(0, len(obstacleArray), 2):
        # want to check if moveCoord is in obstacleArray
        if(moveCoord[0] == obstacleArray[i] and moveCoord[1] == obstacleArray[i+1]):
            return False

    else:
        return True

#function to move in the X direction
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
        

#function to move in the Y direction
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

#main function
def path_Finding(botPath, numMoves, botCoordList):

    testBotCoords = botCoordList
    xDifference = int(botCoordList[0]) - int(userCoordList[0])
    yDifference = int(botCoordList[1]) - int(userCoordList[1])

    # to move horizontal
    if(botCoordList == userCoord):
        return True

    if(abs(xDifference) > abs(yDifference)):
        # if difference is positive, then the bot needs to move left
        if(xMove(xDifference, testBotCoords, obstacleArrayList)):
            botCoordList = testBotCoords
        elif(yMove(yDifference, testBotCoords, obstacleArrayList)):
            botCoordList = testBotCoords
        else:
            return False

    # # to move vertical
    # elif(abs(xDifference) < abs(yDifference)):
    #     # if difference is positive, then the bot needs to move up
    #     if(yMove(yDifference, testBotCoords, obstacleArrayList)):
    #         botCoordList = testBotCoords
    #     elif(xMove(xDifference, testBotCoords, obstacleArrayList)):
    #         botCoordList = testBotCoords
    #     else:
    #         return False

    # # if both x and y differences are same then move in x direction (could be either)
    # else:
    #     if(xMove(xDifference, testBotCoords, obstacleArrayList)):
    #         botCoordList = testBotCoords
    #     elif(yMove(yDifference, testBotCoords, obstacleArrayList)):
    #         botCoordList = testBotCoords
    #     else:
    #         return False
            
    # adding to the final output
    botPath += (str(botCoordList[0]) + " " + str(botCoordList[1]) + ", ")
    numMoves += 1
    # once path has been found run the print function

path_Finding("4 4", "3 3", "0 1", "2 1 1 3", " ")
outputCoords(botPath, numMoves)
