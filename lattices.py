import math
import numpy as np
from decimal import Decimal as dec

def cordinates(a,b):
    cordinatte.append( a )
    cordinatte.append( b )
    cordinatte.append(0)
    atom_add()

def atom_add():
    structure[base] = cordinatte.copy() # dados no dicionario
    cordinatte.clear()  
    xyz.append(structure.copy())
    structure.clear()

def square_network():
    for n in range(1, replication,1):
        for j in range(0, replication,1):
            cordinates(n * a1, j*a2)
            atom_add()

def hexagonal_network(a):
    #Vectors definition
    a1x = a * np.sin(60) 
    a1y = a * np.cos(60) 
    positions = []
    corddinates = []
    for k in range(0,2,1):
        for n in range(0,3,1):
            for j in range(0,3,1):
                positions.append('%.7f'  % dec(n*a1x + j*a1x ))  # x cordinates
                positions.append('%.7f'  % dec(n*a1y - j*a1y ))  # y cordinates
                corddinates.append(positions.copy())
                positions.clear()

hexagonal_network(1.44)
