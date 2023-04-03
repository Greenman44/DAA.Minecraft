from MinecraftNH import Calculate
def BinSearchMinecraft(weigths, swapC, quitC, putC):
    low = 0
    top = max(weigths)

    while (top - low > 1) :
        mid = int((low + top) / 2)
        midCost = Calculate(weigths, putC, quitC, swapC, mid)
        nextCost = Calculate(weigths, putC, quitC, swapC, mid + 1)
        if(midCost >= nextCost):
            low = mid
        else: top = mid

    return Calculate(weigths, putC, quitC, swapC, top),top

