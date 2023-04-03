from random import randint
def generator(n):
    samples = []
    weights = []
     
    for i in range(n):
        size = randint(2,10)    
        l = [randint(2,30) for j in range(size)]
        samples.append(l)
        weights.append( (randint(1,10), randint(1,10), randint(1, 10)) )

    return samples,weights

l = generator(30)
for i in l:
    print(i)