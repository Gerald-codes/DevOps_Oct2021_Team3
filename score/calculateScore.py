# GameOption 4 - View Current Score
def calculateScore(playCity):

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
