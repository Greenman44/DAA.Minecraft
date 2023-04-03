from MinecraftNH import MinecraftNH
from BinSearchMinecraft import BinSearchMinecraft
from colorama import Fore
from Generator import generator

samples,weigths = generator(10000)

for i in range(len(samples)):
   test = BinSearchMinecraft(samples[i], weigths[i][2], weigths[i][1], weigths[i][0])
   safe = MinecraftNH(samples[i],weigths[i][0] , weigths[i][1], weigths[i][2])
   if test[0] == safe[0]:
    print(Fore.GREEN,safe ,"==" , test )
   else:
    print(Fore.RED,safe,"==",test)
   print(Fore.WHITE,samples[i])
   print(Fore.WHITE,weigths[i])

