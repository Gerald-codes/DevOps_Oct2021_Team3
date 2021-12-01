import numpy as np

# MenuMenu Option 2 - Load Saved Game
def loadSavedGame():
    try:
        file=open('savedGame/savedGame.csv','r')
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
        file=open('savedGame/savedBuildingPools.csv','r')
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
        file=open('savedGame/savedTurns.csv','r')
        for line in file:
            turn = int(line)
        return turn
    except Exception as e:
        print('\nThere is no saved turns.')
        return ''
