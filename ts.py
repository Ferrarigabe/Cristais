from decimal import Decimal as dec
import numpy as np
from math import radians as rad

#Vectors definition
a = 2.4640
a1x = a*np.sin(rad(30))
a1y = a*np.cos(rad(30))

# R_0 definition
#atom 1
rx = [2.456, 3.684]
ry = [-2.83594, -2.12696]

positions = []
corddinates = []

for k in range(0,2,1):
    for n in range(0,5,1):
        for j in range(0,5,1):
           positions.append('%.7f'  % dec( rx[k] +  n*a1x + j*a1x ) )  # x cordinates
           positions.append('%.7f'  % dec( ry[k] + n*a1y - j*a1y ) )  # y cordinates
           corddinates.append(positions.copy())
           positions.clear()

arquivo = open("grafite.xyz","w")
arquivo.write("{}\n\n".format(len(corddinates)))

for t in range(0,3,1):
    for item in corddinates:
        arquivo.write('C\t{0[0]}\t{0[1]}\t {1}.00000000\n'.format(item,3*t))
