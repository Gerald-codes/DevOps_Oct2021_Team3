# Game Option 5 - Save Game
def saveGame(playCity,bPool,turn):
    file=open('savedGame/savedGame.csv','w')
    for i in range(len(playCity)):
        file.write(str(''.join(playCity[i])))
        file.write('\n')
    file.close()
    file=open('savedGame/savedBuildingPools.csv','w')
    for i in range(len(bPool)):
        file.write(str(bPool[i][0]))
        file.write(',')
        file.write(str(bPool[i][-1]))
        file.write('\n')
    file.close()
    file=open('savedGame/savedTurns.csv','w')
    file.write(str(turn))
    file.close()
    print('\nGame saved!')

