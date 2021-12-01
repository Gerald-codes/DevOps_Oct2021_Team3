from main import loadCity, loadSavedBuildingPools, loadSavedGame, initBuildingPools, loadSavedTurns
from gameMenu import gameMenu

def mainMenu():
    # Display Main Menu
    print('\nWelcome, mayor of Simp City!')
    print('----------------------------')
    option_list=('Start new game','Load saved game')
    for i in range(len(option_list)):
        print('[{}] {}'.format(i+1,option_list[i]))
    print('\n[0] Exit')

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