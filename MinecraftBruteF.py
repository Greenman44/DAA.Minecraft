import numpy as np
import math
def MinecraftBruteForce(swap,put,quit,wall):
    minV =  np.min(wall)
    maxV = np.max(wall) + 1
    sol = np.inf
    h = np.inf
    for i in range(minV,maxV):
        temp = BestWall(swap, put, quit, wall, i)
        if sol > temp:
            sol = temp
            h = i    
    return sol,h

def Check(height, wall):
    for i in range(len(wall)):
        if(wall[i] != height):
            return False
    return True


def BestWall(swap,put,quit,wall,height):
    if(Check(height,wall) ):
        return 0
    quitCost = np.inf
    putCost = np.inf
    moveCost = np.inf
    for i in range(len(wall)):
        if(wall[i] > height):
            nWall = [k for k in wall]
            nWall[i] = nWall[i] - 1
            quitCost = min(quitCost, quit + BestWall(swap, put, quit, nWall, height))
            for j in range(len(wall)):
                if(i != j and wall[j] < height):
                    nWall = [k for k in wall]
                    nWall[j] = nWall[j] + 1
                    nWall[i] = nWall[i] - 1
                    moveCost = min(moveCost, swap + BestWall(swap, put, quit, nWall, height))

        if(wall[i] < height):
            nWall = [k for k in wall]
            nWall[i] = nWall[i] + 1
            putCost = min(putCost, put + BestWall(swap, put, put, nWall, height))

    return min(quitCost, moveCost, putCost)   


 