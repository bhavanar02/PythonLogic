import random


def getInput():
    rowCnt = input("# of rows: ")      
    colCnt = input("# of columns: ")  
    return colCnt, rowCnt 


def buildRoom(colCnt, rowCnt):   
    room = [[random.randint(0, 100) % 2 for x in range(int(colCnt))] for y in range(int(rowCnt))] 
    return room


def placeRobot():
    rowNum = random.randint(0, 100) % int(rowCnt)
    colNum = random.randint(0, 100) % int(colCnt)
    print("Starting row: ", rowNum)
    print("Starting column: ", colNum)
    return colNum, rowNum


def displayRoom(room):
    for i in room:
        print(*i, sep="\t")   #unpacking operator
        

def moveRobot(rowNum, colNum, rowCnt, colCnt):
    temprowNum = rowNum
    tempcolNum = colNum
    direction = random.randint(0, 100) % 4  	# 0 left, 1 right, 2 up, 3 down

    print("direction is: ", direction)
    if direction == 0:
        if tempcolNum != 0:
            tempcolNum -= 1
    elif direction == 1:
        if tempcolNum != 3:
            tempcolNum += 1
    elif direction == 2:
        if temprowNum != 0:
            temprowNum -= 1
    else:
        if temprowNum != 3:
            temprowNum += 1


    return tempcolNum, temprowNum


def robotAction(room, rowNum, colNum):
    if room[rowNum][colNum] == 1:
        room[rowNum][colNum] = 0
        print("Cleaned")
    else:
        print("No operation")


def isRoomDirty(room):
    for rowVal in range(int(rowCnt)):
        for colVal in range(int(colCnt)):
            if room[rowVal][colVal] == 1:
                return True
    return False       


colCnt, rowCnt = getInput()

room = buildRoom(colCnt, rowCnt)
displayRoom(room)
colNum, rowNum = placeRobot()

mess = True
while mess == True:
    robotAction(room, rowNum, colNum)
    displayRoom(room)
    colNum, rowNum = moveRobot(rowNum, colNum, rowCnt, colCnt)
    mess = isRoomDirty(room)
            