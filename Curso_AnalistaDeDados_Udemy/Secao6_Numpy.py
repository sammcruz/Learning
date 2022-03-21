#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 11:22:22 2022

@author: samantha
"""

import numpy as np

print(np.__version__)

myarray = np.array([10, 20, 30, 40, 50])

type(myarray)

duas = np.array([
    [10, 9,8, 7, 6],
    [5, 4, 3, 2 , 1]
    ])
print(duas)
    
tres = np.array([
    [15, 14, 13, 12, 11],
    [10, 9, 8, 7, 6],
    [5, 4, 3, 2, 1]
    ])
print(tres)
    
# experimento de processamento
estressando_NP = np.arange(1000000)    
estressando_NP_2 = np.arange(5000000)  
estressando_NP_3 = np.arange(10000000)  
estressando_NP_4 = np.arange(50000000)  

len(estressando_NP)

%time for loop in estressando_NP: pass
%time for loop in estressando_NP_2: pass
%time for loop in estressando_NP_3: pass
%time for loop in estressando_NP_4: pass

# acessando posições
myarray[0]
myarray[-1]
myarray[2:]
myarray[3:4]

# operações matematicas
myarray[0] + myarray[1]
myarray[0] * myarray[1]
myarray[0] - myarray[1]
myarray[0] / myarray[1]
myarray[0] ** myarray[1]

# operações logicas
myarray[0] == myarray[1]
myarray[0] != myarray[1]
myarray[0] <= myarray[1]
myarray[0] >= myarray[1]
myarray[0] > myarray[1]

# verificar dimensões
myarray.shape()

# loop no array com uma dimensão
for loop in myarray:
    print(loop)

# para matriz com mais de uma dimensão
for loop in tres:
    for interno in loop:
        print(interno)

# array 3D
a3D = np.zeros((2, 3, 4))
for loop in a3D:
    for interno in loop:
        for maisInterno in interno:
            print(maisInterno)

