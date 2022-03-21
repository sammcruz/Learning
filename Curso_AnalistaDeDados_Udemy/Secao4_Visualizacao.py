#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 19:15:54 2022

@author: samantha
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#gera um vetor com numeros aleatórios entre 1,1500, com 10 amostras
np.random.seed(7)
y = np.random.randint(low = 1, high = 1500, size = 10)
plt.plot(y)

# Gráfico personalizado
plt.plot(y, color='#749187', marker = 'o', ms = 5, mec = 'k',
         markerfacecolor = 'w', ls = '-.')

plt.plot(y*2, marker = '+', color = 'k', ms = 5)

plt.xlabel('Eixo X', color = 'red', size = 12)
plt.ylabel('Eixo Y')
plt.title('Título', loc = 'left')

plt.grid(axis = 'y', color = 'gray', linestyle='--', linewidth=1, alpha = 0.8)

plt.show()

# SUBPLOTS

np.random.seed(6)

x = np.arange(1, 11)
y1 = np.random.randint(1, 400, 10)
y2 = np.random.randint(150, 500, 10)
y3 = np.random.randint(200, 600, 10)

plt.figure(figsize = (15, 5))
plt.suptitle('Figura', fontsize = 15)

plt.subplot(1, 3, 1)
plt.plot(x, y1, color = 'k')
plt.title('Subplot 1', pad = 10)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

plt.subplot(1, 3, 2)
plt.plot(x, y2, color = 'r')
plt.title('Subplot 2', pad = 10)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

plt.subplot(1, 3, 3)
plt.plot(x, y3, color = 'g')
plt.title('Subplot 3', pad = 10)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

plt.tight_layout(pad = 4)
plt.show()

# TERCEIRO GŔAFICO

fig, ax = plt.subplots(1, 3, figsize = (15, 5))
fig.suptitle('Figure')
ax[0].plot(x, y1, color = 'black')
ax[1].plot(x, y2, color = 'red')
ax[2].plot(x, y3, color = 'green')

for i in range(3):
    ax[i].set(title = f'Subplot {i+1}', xlabel = 'Eixo X', ylabel = 'Eixo Y')
    
'''
##############  -->  HISTOGRAMA, BOXPLOT
'''

data = np.random.normal(10, 0.5, 5000)
plt.hist(data)
plt.show()

plt.boxplot(data)
   
'''
##############  -->  SCATTER
'''
x = np.random.normal(10, 0.5, 100)
y = np.random.uniform(0, 20, 100)

fig = plt.figure()
ax = plt.axes()
ax.scatter(x, y, marker = 'o', color = 'red', label = 'data 1', alpha = 0.5)
ax.scatter(x*0.5, y*0.5, marker = 'v', color = 'black', label = 'data 2', alpha = 0.7)
ax.legend()
  
'''
##############  -->  plotly
'''

import plotly.express as px

px.data.gapminder()

df = px.data.gapminder().query('country == "Brazil"').set_index('year')

df.head()
df.info()

plt.plot(df.index, df['gdpPercap'])
plt.title("PIB per capta do Brasil")
plt.ylabel('PIB per capta')
plt.xlabel('Tempo')

title = 'Relação entre a expectativa de vida e a reda per capta no Brasil e Argentina'
plt.figure(figsize = (12, 4))
plt.scatter(df['lifeExp'], df['gdpPercap'], cmap = 'viridis')
plt.ylabel('Expectativa de vida')
plt.ylabel('Renda per capta')
plt.title(title, loc = 'left')
plt.show()

'''
##############  -->  BAR
'''

plt.bar(x = df.index, height = df['pop'], color = 'red')
plt.title('População brasileira')

def filtrar_continente (continente):
    df = px.data.gapminder()
    df = df[df['continent'] == continente]
    return df

def filtrar_pais( pais, variavel):
    'Filtra algum país da amostra para as variáveis "pop", "gdPercap" e "lifeExp'
    df = px.data.gapminder()
    df = df[df['country'] == pais][variavel]
    return df

americas = filtrar_continente('Americas')
paises = americas['country'].unique()
plt.figure(figsize = (12,8))
for pais in paises:
    plt.scatter(filtrar_pais(pais = pais, variavel = 'lifeExp'),
               filtrar_pais(pais = pais, variavel = 'gdpPercap'))
plt.legend(labels = paises, loc = 'best')
plt.title('Relação entre renda per capta e expectativa de vida', loc = 'left')
plt.xlabel('Expectativa de vida')
plt.ylabel('Renda per capta')



















