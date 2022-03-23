#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 18:12:51 2022

@author: samantha
"""

# Importando as bibliotecas
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

numeros = np.arange(50, 325, 25)
print(numeros)

plt.plot(numeros)

# lista bagunçada
numeros_a = [225, 150, 75, 50, 200, 250, 125, 300, 100, 275, 175]

# tipos de linha
plt.plot(numeros_a, '-')
plt.plot(numeros_a, '.')
plt.plot(numeros_a, 'o-')

# Cores e estilos
plt.plot(numeros_a, 'o-k')
plt.plot(numeros_a, '^-r')
plt.plot(numeros_a, '-', c = 'indigo')

# Definir o tamanho do plot
plt.figure(figsize=(10,5))
plt.plot(numeros_a, '*', color = 'deeppink')

sna = np.sin(range(-10,10))
cna = np.cos(range(-10,10))
plt.plot(sna)
plt.plot(cna)
plt.grid(alpha = 0.5)

''' Add labels to line plots '''

plt.clf()

# using some dummy data for this example
xs = np.arange(0,10,1)
ys = np.random.normal(loc=3, scale=0.4, size=10)

# 'bo-' means blue color, round points, solid lines
plt.plot(xs,ys,'bo-')

# zip joins x and y coordinates in pairs
for x,y in zip(xs,ys):

    label = "{:.2f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.show()


''' Barplots '''

percent = np.random.randint(0,100, 5)
plantas = 'Asplenio', 'Columeia', 'Samambaia', 'Lírio da Praia', 'Monstera'
















