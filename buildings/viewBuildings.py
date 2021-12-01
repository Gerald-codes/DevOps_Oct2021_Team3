# GameOption 3 - View Remaining Building Available
def viewRemainingBuilds(bPool):
    print('\nBuildings\tRemaining\n----------\t----------')
    for i in range(len(bPool)):
        print('{}\t\t{}'.format(bPool['Building'][i],bPool['Copies'][i]))
