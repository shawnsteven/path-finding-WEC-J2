# WEC Competition - Rhys, Anh, Shawn

def outputCoords(botPath, numMoves):
    
    print(botPath)
    print(numMoves)


def checkMove(moveCoord, obstacleArray):
    for i in range(0, len(obstacleArray), 2):
        
        #want to check if moveCoord is in obstacleArray
        if(moveCoord[i] == obstacleArray[i] and moveCoord[i+1] == obstacleArray[i+1]):
            return False

    else:
        return True


def path_Finding(dimension, botCoord, userCoord, obstacleArray, itemCoord):

    #set up variables
    newBotCoords = []
    testBotCoords = []
    numMoves = 0
    botPath = ""
    reachedObjective = False

    #set up our variables into arrays
    dimensionList = dimension.split(" ")
    botCoordList = botCoord.split(" ")
    userCoordList = userCoord.split(" ")
    obstacleArrayList = obstacleArray.split(" ")


    [3, 2, 3, 4, 3, 2] = 

    [[3, 2], [3, 4]]

    itemCoordList = itemCoord.split(" ")
    
    #main loop
    while(not reachedObjective):
        xDifference = botCoordList[0] - userCoordList[0]
        yDifference = botCoordList[1] - userCoordList[1]


        #to move horizontal
        if(abs(xDifference) > abs(yDifference)):
            #if difference is positive, then the bot needs to move left
            if(xDifference > 0):
                testBotCoords = botCoordList
                testBotCoords[0] -= 1
                

                #now we need to check if the move is allowed
                if(checkMove(testBotCoords, obstacleArrayList)):
                    botCoord = testBotCoords
                
                else:
                    
                    

            #if difference is negative, then the bot needs to move right
            else:
                testBotCoords = botCoordList
                testBotCoords[0] += 1
            


        #to move vertical
        elif(abs(xDifference) < abs(yDifference)):
            #if difference is positive, then the bot needs to move up
            if(yDifference > 0):
                testBotCoords = botCoordList
                testBotCoords[1] -= 1
                
            #if difference is negative, then the bot needs to move down
            else:  
                testBotCoords = botCoordList
                testBotCoords[1] += 1

        #move in any direction
        else:

    
    #once path has been found
    outputCoords(botPath, numMoves)

 



print(path_Finding())
