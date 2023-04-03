from numpy import inf
def Calculate( weights, putC, quitC, swapC, height):
    up = 0
    down = 0

    for w in weights:
        if w > height :
            up += w - height

        else : 
            down += height - w

    toSwap = toQuit = toPut = 0
    if( swapC < quitC + putC):
        if down >= up : 
            toSwap = up
            toPut = down - up
        else: 
            toSwap = down
            toQuit = up - toSwap
    else: 
        toQuit = up
        toPut = down
    return toQuit * quitC + toPut * putC + toSwap * swapC



def MinecraftNH(weights, putC, quitC, swapC):
    minValue = min(weights)
    maxValue = max(weights)
    bestCost = inf
    bestHeight = inf
    for i in range(minValue, maxValue + 1):
        tempCost = Calculate(weights, putC, quitC, swapC, i)
        if tempCost < bestCost: 
            bestCost = tempCost
            bestHeight = i
            
    return bestCost, bestHeight