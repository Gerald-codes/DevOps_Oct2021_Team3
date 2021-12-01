# Imports
from math import trunc
import numpy as np
import csv
from random import randrange
from numpy.core.numeric import roll


# Variables
loc_col = []
loc_row = []
inserted_Buildings = []

# Functions
def mainMenu():
    # Display Main Menu
    print('\nWelcome, mayor of Simp City!')
    print('----------------------------')
    option_list=('Start new game','Load saved game')
    for i in range(len(option_list)):
        print('[{}] {}'.format(i+1,option_list[i]))
    print('\n[0] Exit')

# MenuMenu Option 1 - Load City For New Game
def loadCity(file):
    mainCity = []
    with open(file,encoding='utf-8-sig',newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for x in spamreader:
            col = []
            for i in x:
                if i == '*':
                    i = ' '
                col.append(i)

            mainCity.append(col)  
    import copy
    playCity=copy.deepcopy(mainCity)
    return playCity

# MenuMenu Option 1 - Initiate Building Pools With 8 Copies Of Each Building For New Game
def initBuildingPools():
    #Structured Array For Buildings Pool
    buildingPools = np.array([('BCH',8),('FAC',8),('HSE',8),('SHP',8),('HWY',8)],
                dtype=[('Building','U5'),('Copies','<i4')])
    return buildingPools

# MenuMenu Option 2 - Load Saved Game
def loadSavedGame():
    try:
        file=open('savedGame.csv','r')
        mainCity=[]
        lineList=[]
        for line in file:
            line=line.strip('\n')
            lineList=list(line)
            mainCity.append(lineList)
        return mainCity
    except Exception as e:
        print('\nThere is no saved game.')
        return ''

# MenuMenu Option 2 - Load Saved Building Pools
def loadSavedBuildingPools():
    try:
        file=open('savedBuildingPools.csv','r')
        varList=[]
        for line in file:
            line=line.strip('\n')
            bName = str(line[0:3])
            bAmount = int(line[-1])
            var = (bName, bAmount)
            varList.append(var)
        bPools = np.array(varList, dtype=[('Building','U5'),('Copies','<i4')])
        return bPools
    except Exception as e:
        print('\nThere is no saved Building Pools.')
        return ''

# MenuMenu Option 2 - Load Saved Turns
def loadSavedTurns():
    try:
        file=open('savedTurns.csv','r')
        for line in file:
            turn = int(line)
        return turn
    except Exception as e:
        print('\nThere is no saved turns.')
        return ''

# View Playing City
def viewCity(map):
    for i in map:
        print(*i)
    print()      

# Randomize 2 Building For Every Turn
def rollBuilding(bPool):
    b = bPool[randrange(5)]['Building']
    return b

#Inserting coordinates(col,row) given by user into column and row list
def insertColRow(arr,letter,number):               
    for i in arr:
        if number in i:
            loc_row.insert(0,arr.index(i))
            break
        for x in i:
            if  x == letter:
                loc_col.insert(0,i.index(x))
                break

#sub function(insertBuilding) required to remove coords from the col & row list 
#in the case where user entered an invalid input for building           
def removeColRow():
    loc_col.pop(0)
    loc_row.pop(0)

#sub function required(insertBuilding) to checks if there is any existing buildings
def checkExist(arr,nRow,nCol):
    if arr[nRow[0]][nCol[0]] == " ":
            return False
    else:
        print("You are trying to build on existing building!")
        return True

#Sub function of (insertBuilding) to perform swapping of 'item' in the city list
def mSwap(arr,bName,row,col,t):
    if t == 1:
        arr[row[0]][col[0]-1] = bName[0][0]
        arr[row[0]][col[0]] = bName[0][1]
        arr[row[0]][col[0]+1] = bName[0][2]
    else:
        arr[row[0]][col[0]-1] = bName[0][0]
        arr[row[0]][col[0]] = bName[0][1]
        arr[row[0]][col[0]+1] = bName[0][2]

#sub function(insertBuilding) required to do the necessary validation checks when user inserts a building
#True = can build
#False = cannot build
def checkCord(arr,nRow,nCol,oRow,oCol):
    #situation where trying to insert into same row & col
    if nCol[0] == oCol and nRow[0] == oRow:
            print("You are trying to build on existing Building!")
            #remove cordinates from col/row list
            removeColRow()
            return False
    #situation where same column insertion
    elif nCol[0] == oCol or nRow[0] == oRow:
        if nRow[0] - 2 == oRow or nRow[0] + 2 == oRow or nCol[0] - 6 == oCol or nCol[0] + 6 == oCol:
            if checkExist(arr,nRow,nCol) == False:
                return True
            else:
                print("Building already exists at where you try to build")
                removeColRow()
                return False
        else:
            print("Invalid input, please try again!")
            removeColRow()
            return False
    else:
        if nRow[0] - 2 == oRow or nRow[0] + 2 == oRow or nCol[0] - 6 == oCol or nCol[0] + 6 == oCol:
            if checkExist(arr,nRow,nCol) == False:
                return True
            else:
                print("Building already exists at where you try to build")
                removeColRow()
                return False
        else:
            print("Invalid input, please try again!")
            removeColRow()
            return False 

# GameOption 1 & 2 - Building A Building
def findColRow(arr,letter,number):               
    for i in arr:
        if number in i:
            #print("{} row found".format(i))
            loc_row.insert(0,arr.index(i))
            break
        for x in i:
            if  x == letter:
                #print("{} column found".format(i))
                loc_col.insert(0,i.index(x))
                break

def insertBuilding(arr,bPool,bName,row,col,t):
    if t == 1:
        mSwap(arr,bName,row,col,t)
        x = np.where(bPool['Building']==bName)
        index = x[0][0]
        bPool[index]['Copies']-=1
        inserted_Buildings.insert(0, bName)
        #checkCityScore(arr,bName)
        return (bPool)
    elif t > 1:
        if checkCord(arr,row,col,loc_row[1],loc_col[1]) == True:
            mSwap(arr,bName,row,col,t)
            inserted_Buildings.insert(0, bName)
            #checkCityScore(arr,bName)
    return (bPool)

# def mSwap(arr,bName,row,col):
#     arr[row[0]][col[0]-1] = bName[0][0]
#     arr[row[0]][col[0]] = bName[0][1]
#     arr[row[0]][col[0]+1] = bName[0][2]

# GameOption 3 - View Remaining Building Available
def viewRemainingBuilds(bPool):
    print('\nBuildings\tRemaining\n----------\t----------')
    for i in range(len(bPool)):
        print('{}\t\t{}'.format(bPool['Building'][i],bPool['Copies'][i]))

# GameOption 4 - View Current Score
def ViewCurrentScore(playCity):

    dict = mapBuildingsToCords(playCity)
   
   # Calculate HSE
    HSEScore = calculateHSE(dict)

   # Calculate FAC
    FACScore = calculateFAC(dict)

    # Calculate SHP
    SHPScore = calculateSHP(dict)
    
    # Calculate HWY
    HWPScore = calculateHWY(dict)

    # Calculate BCH
    BCHScore = calculateBCH(dict)

    totalScore = BCHScore + FACScore + HSEScore + SHPScore + HWPScore
    print("\nTotal score : ", totalScore)
    
def mapBuildingsToCords(playCity):
    # Create Dictionary 
        dict = {}
        col = 2
        row = 3
        AlphaNum = 4
        while row < 25:
            rowNumCount = 1
            while col < 9:
                colAlpha = playCity[0][AlphaNum]
                building = str(playCity[col][row])+str(playCity[col][row+1])+str(playCity[col][row+2])
                if building == '   ':
                    dict["{}{}".format(colAlpha,rowNumCount)] = None
                else:
                    dict["{}{}".format(colAlpha,rowNumCount)] = building
                rowNumCount +=1
                col +=2
            AlphaNum += 6
            row += 6
            col = 2
        # print(dict)
        return(dict)

def calculateBCH(dict):
    i = 2
    BCHCount = 0
    rowNumCount = 1
    while i < 9:
        # print(str(dict.get("D{}".format(rowNumCount))), "DDD")
        # print(str(dict.get("D2")))
        if str(dict.get("A{}".format(rowNumCount))) == "BCH":
            BCHCount += 1
        if str(dict.get("D{}".format(rowNumCount))) == "BCH":
            BCHCount += 1
        i += 2
        rowNumCount += 1
    if BCHCount == 0:
        print("BCH = 0 ")
        return 0
    else:
        stmt = ""
        num=1
        while num <= BCHCount:
            if num == BCHCount:
                stmt+= "3"
            else:
                stmt+= "3 + "
            num +=1
        subScore = 3*BCHCount
        print("BCH = " + stmt + " = " + str(subScore))
        return subScore

def calculateFAC(dict):
    FACCount = 0
    for building in dict.values():
        if building == "FAC":
            FACCount +=1
    # print(FACCount)
    stmt = ""
    if FACCount >= 4:
        stmt += "4 + 4 + 4 + 4"
        FACCount -= 4
        num=1
        while num <= FACCount:
            stmt+=" + 1"
            num +=1
        subScore = (4*4)+(num-1)
        print("FAC = " + stmt + " = " + str(subScore))
    else:
        num=1
        while num <= FACCount:
            if num == FACCount:
                stmt+= "{}".format(FACCount)
            else:
                stmt+= "{} + ".format(FACCount)
            num +=1
        subScore = FACCount*FACCount
        print("FAC = " + stmt + " = " + str(subScore))
    return subScore

def calculateHSE(dict):
    stmt = ""
    totalScore = 0
    HSECount = 0
    # print(dict.items())
    for item in dict.items():
        if item[1] == "HSE":
            subScore = 0
            # Check building around HSE if its FAC
            up = dict.get((item[0][0])+str(int(item[0][1])-1))
            down = dict.get((item[0][0])+str(int(item[0][1])+1))
            left = getLeftBuilding(dict,item[0])
            right = getRightBuilding(dict,item[0])
            if right == None:
                right = None
            else:
                right = right[-1]
            if left == None:
                left = None
            else:
                left = left[-1]
            # print(up,down,left,right)
            if up == "FAC" or down == "FAC" or left == "FAC" or right == "FAC":
                subScore +=1
            else:
                if up == "HSE" or up == "SHP":
                    subScore += 1
                if down == "HSE" or down == "SHP":
                    subScore += 1
                if left == "HSE" or left == "SHP":
                    subScore += 1
                if right == "HSE" or right == "SHP":
                    subScore += 1
                if up == "BCH":
                    subScore += 2
                if down == "BCH":
                    subScore += 2
                if left == "BCH":
                    subScore += 2
                if right == "BCH":
                    subScore += 2
            totalScore += subScore
            if HSECount == 0:
                stmt += str(subScore)
            else:
                stmt += " + {}".format(subScore)
            HSECount += 1
    if HSECount == 0:
        print("HSE = {}".format(totalScore))
    else:
        print("HSE = {} = {}".format(stmt,totalScore))
    return totalScore

def calculateSHP(dict):
    stmt = ""
    SHPCount = 0 
    totalScore = 0
    for item in dict.items():
        if item[1] == "SHP":
            subScore = 0
            # Check building around SHP
            up = dict.get(item[0][0]+str(int(item[0][1])-1))
            down = dict.get(item[0][0]+str(int(item[0][1])+1))
            left = getLeftBuilding(dict,item[0])
            right = getRightBuilding(dict,item[0])
            if right == None:
                right = None
            else:
                right = right[-1]
            if left == None:
                left = None
            else:
                left = left[-1]
            list = [up,down,left,right]
            res = []
            for i in list:
                if i not in res:
                    if i == None:
                        pass
                    else:
                        res.append(i)
            subScore += len(res)
            if SHPCount == 0:
                stmt += str(len(res))
            else:
                stmt += " + {}".format(len(res))
            totalScore += subScore
            SHPCount += 1
    if SHPCount == 0:
        print("SHP = 0")
        return 0
    else:
        print("SHP = {} = {}".format(stmt, totalScore))
        return totalScore

def getLeftBuilding(dict,cord):
    if cord[-1] == "0" or cord[-1] == "5":
        return None
    elif cord[0] == "D":
        left = "C" + cord[1]
    elif cord[0] == "C":
        left = "B" + cord[1]
    elif cord[0] == "B":
        left = "A" + cord[1]
    else:
        return None
    building = dict.get(left)
    leftList = [left,building]
    return leftList

def getRightBuilding(dict,cord):
    if cord[-1] == "0" or cord[-1] == "5":
        return None
    elif cord[0] == "A":
        right = "B" + cord[1]
    elif cord[0] == "B":
        right = "C" + cord[1]
    elif cord[0] == "C":
        right = "D" + cord[1]
    else:
        return None
    building = dict.get(right)
    rightList = [right,building]
    return rightList

def calculateHWY(dict):
    stmt = ""
    num = 0
    HWYCount = 0 
    totalScore = 0
    for item in dict.items():
        if item[1] == "HWY":
            subScore = 1
            cords = item[0]
            while True :
                left = getLeftBuilding(dict,cords)
                # print(left,"LEFT")
                if left  == None:
                    break
                elif left[-1] == "HWY":
                    cords = left[0]
                    subScore += 1
                else:
                    break
            cords = item[0]
            while True :
                right = getRightBuilding(dict,cords)
                # print(right,"right")
                if right == None:
                    break
                elif right[-1] == "HWY":
                    subScore += 1
                    cords = right[0]
                else:
                    break
            # print(subScore, "SUB")
            if subScore>1: 
                totalScore += subScore
            else:
                totalScore += 1
                subScore = 1
            if num == 0:
                stmt += "{}".format(subScore)
                num += 1
            else:
                stmt += " + {}".format(subScore)
                num += 1
            HWYCount += 1
    if HWYCount == 0:
        print("HWY = 0")
        return 0
    else:
        print("HWY = {} = {}".format(stmt,totalScore))    
        return totalScore

# Game Option 5 - Save Game
def saveGame(playCity,bPool,turn):
    file=open('savedGame.csv','w')
    for i in range(len(playCity)):
        file.write(str(''.join(playCity[i])))
        file.write('\n')
    file.close()
    file=open('savedBuildingPools.csv','w')
    for i in range(len(bPool)):
        file.write(str(bPool[i][0]))
        file.write(',')
        file.write(str(bPool[i][-1]))
        file.write('\n')
    file.close()
    file=open('savedTurns.csv','w')
    file.write(str(turn))
    file.close()
    print('\nGame saved!')

# Game Menu
def gameMenu(bPool,playCity,turn):

        while True:
            if turn == 17:
                # Diplay Final layout
                print('\nFinal layout of Simp City:\n')
                viewCity(playCity)
                ViewCurrentScore(playCity)
                print('\nThank you for playing Simp City!')
                return
            else:
                # Get Random Building Options
                b1 = rollBuilding(bPool)
                b2 = rollBuilding(bPool)

                # Game Menu Options
                game_menu = [[1,'Build a ' + b1],[2,'Build a '+b2],
                [3,'See remaining buildings'],[4,'See Current Score'],
                [5,'Save Game'],[0,'Exit to main menu']]
                
                # Diplay Turn
                print('\n-----------------------Turn {}-----------------------\n'.format(turn))

                # Display City
                viewCity(playCity)

                # Display Game Menu Options
                for i in range(len(game_menu)):
                    print('[{}] {}'.format(game_menu[i][0],game_menu[i][1]))
                    if i == 3:
                        print()
                
                # Prompt For User's Choice
                game_option= input(str('\nYour Choice? '))

                # GameOption 1 - Build A Building
                if game_option == '1':
                    #get index of building from bPool to retrieve building name
                    x = np.where(bPool['Building'] == b1)
                    currBuild = bPool['Building'][x]

                    build_loc = input(str('Build Where? '))
                    # print("col to search {} row to search {}".format(build_loc[0], type(build_loc[1])))
                    insertColRow(playCity,build_loc[0].upper(),build_loc[1])
                    col = loc_col
                    row = loc_row
                    bPool = insertBuilding(playCity,bPool,currBuild,row,col,turn)
                    turn +=1
                # GameOption 2 - Build A Building
                elif game_option == '2':
                #get index of building from bPool to retrieve building name
                    x = np.where(bPool['Building'] == b1)
                    currBuild = bPool['Building'][x]

                    build_loc = input(str('Build Where? '))
                    # print("col to search {} row to search {}".format(build_loc[0], type(build_loc[1])))
                    insertColRow(playCity,build_loc[0].upper(),build_loc[1])
                    col = loc_col
                    row = loc_row
                    bPool = insertBuilding(playCity,bPool,currBuild,row,col,turn)
                    turn +=1
                # GameOption 3 - View Remaining Building Available
                elif game_option == '3':
                    viewRemainingBuilds(bPool)
                # GameOption 4 - View Current Score
                elif game_option == '4':
                    print('\n-------------------Current Score--------------------\n')
                    ViewCurrentScore(playCity)
                # GameOption 5 - Save Game
                elif game_option =='5':
                    saveGame(playCity,bPool,turn)
                    break
                # GameOption 0 - Exit To Main Menu
                elif game_option =='0':
                    return
                else:
                    print("\nInvalid option, please try again")

# Menu Menu
while True:
    mainMenu()
    choice = input(str('\nEnter your choice? '))
    # Start New Game
    if (choice == '1'):    
        playCity = loadCity('start.csv')
        buildingPools = initBuildingPools()
        gameMenu(buildingPools,playCity,turn=1)
    # Load Saved game
    elif (choice == '2'): 
        playCity = loadSavedGame()
        if (playCity != ''):
            buildingPools = loadSavedBuildingPools()
            gameMenu(buildingPools,playCity,turn=loadSavedTurns())
        else:
            pass
    # Exit Menu
    elif (choice == '0'):
        print('\nThank you for playing Simp City!')
        break
    # Validate for Invalid Input
    else:
        print('\nInvalid option, please try again!')
    