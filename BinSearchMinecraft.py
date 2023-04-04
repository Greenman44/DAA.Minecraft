from MinecraftNH import Calculate
def BinSearchMinecraft(weigths, swapC, quitC, putC):
    low = 0
    top = max(weigths)

    while top - low > 1 :
        mid = low + top // 2
        midCost = Calculate(weigths, putC, quitC, swapC, mid)
        nextCost = Calculate(weigths, putC, quitC, swapC, mid + 1)
        if midCost >= nextCost:
            low = mid
        else: top = mid

    if top-low ==1:
        top_cost = Calculate(weigths, putC, quitC, swapC,top)
        low_cost = Calculate(weigths, putC, quitC, swapC,low)
        return min(top_cost,low_cost),min(top,low)

    return Calculate(weigths, putC, quitC, swapC, top),top

print(BinSearchMinecraft([5,0,1,1],100,8,26))