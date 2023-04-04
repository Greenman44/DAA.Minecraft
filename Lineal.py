def Blocks(weights, putC, quitC, swapC):
    blocks = [0 for _ in range(max(weights)+1)]
    cant_bloques = 0
    
    for i in weights:
        cant_bloques += i
        blocks[i]+=1
    
    for i in range(len(blocks)-2,-1,-1):
        blocks[i]+=blocks[i+1]


    if putC + quitC <= swapC:
        costo = costo_1
    else:
        costo = costo_2
    
    down = len(weights)-blocks[0]
    up = cant_bloques
    c = costo(putC,quitC,swapC, down, up)
    for i in range(1,len(blocks)):
        up -= blocks[i]
        down += len(weights) - blocks[i]
        c_new = costo(putC,quitC,swapC, down, up)
        print(c_new)
        if c_new > c:
            return c
        else:
            c = c_new        
    return c


def costo_1(putC, quitC, swapC, down, up):
    return putC * down + quitC * up


def costo_2(putC, quitC, swapC, down, up):
    # p + q > s
    move = min(down,up)
    return swapC * move + putC *(down-move) +quitC * (up - move)


print(Blocks([5,0,1,1],26,8,100))