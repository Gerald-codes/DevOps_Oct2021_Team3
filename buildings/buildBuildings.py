from random import randrange
import numpy as np

# Variables
loc_col = []
loc_row = []
inserted_Buildings = []

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
