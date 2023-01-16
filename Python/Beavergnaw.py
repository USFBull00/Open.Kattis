#Beavergnaw, difficulty 1.7
import math
while True:
    D, V = input().split()
    if D == '0' and V == '0':
        break
    else:
        volumeD = (math.pi)*(float(D)**3)
        difference = volumeD - (6*float(V))
        d = (difference/(math.pi))**(1/3)
        print("{:.11}".format(d))