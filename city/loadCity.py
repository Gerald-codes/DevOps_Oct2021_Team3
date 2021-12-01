import csv

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
