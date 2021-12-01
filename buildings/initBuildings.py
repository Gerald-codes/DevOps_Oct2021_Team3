import numpy as np

# MenuMenu Option 1 - Initiate Building Pools With 8 Copies Of Each Building For New Game
def initBuildingPools():
    #Structured Array For Buildings Pool
    buildingPools = np.array([('BCH',8),('FAC',8),('HSE',8),('SHP',8),('HWY',8)],
                dtype=[('Building','U5'),('Copies','<i4')])
    return buildingPools
