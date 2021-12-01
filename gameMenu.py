
from buildings.buildBuildings import rollBuilding, insertBuilding, insertColRow, loc_col, loc_row
from buildings.viewBuildings import viewRemainingBuilds
from score.calculateScore import calculateScore
from city.viewCity import viewCity
from savedGame.saveGame import saveGame
import numpy as np

# Game Menu
def gameMenu(bPool,playCity,turn):

        while True:
            if turn == 17:
                # Diplay Final layout
                print('\nFinal layout of Simp City:\n')
                viewCity(playCity)
                calculateScore(playCity)
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
                    calculateScore(playCity)
                # GameOption 5 - Save Game
                elif game_option =='5':
                    saveGame(playCity,bPool,turn)
                    break
                # GameOption 0 - Exit To Main Menu
                elif game_option =='0':
                    return
                else:
                    print("\nInvalid option, please try again")
