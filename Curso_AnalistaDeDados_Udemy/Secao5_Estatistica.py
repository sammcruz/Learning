#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 10:46:41 2022

@author: samantha
"""


import numpy as np
import pandas as pd
import seaborn as sns
import  matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

dados = sns.load_dataset('iris')
dados.head()

dados.shape

########## MEDIDAS DE TENDENCIA CENTRAL ##########

dados['petal_length'].mean()   # 3.75
dados['petal_length'].mode()   # 1.4 e 1.5
dados['petal_length'].median() # 4.35

########## MEDIDAS SEPARATRIZES ##########

'QUARTIS'
dados['sepal_length'].describe()
sns.boxplot(data=dados)

########## MEDIDAS DE DISPERSÃO ##########

#amplitude total
dados['sepal_length'].max() - dados['sepal_length'].min()

#amplitude interquartilica
dados['sepal_length'].describe()[6:7].values - dados['sepal_length'].describe()[4:5].values

#amplitude semi interquartilica
(dados['sepal_length'].describe()[6:7].values - dados['sepal_length'].describe()[4:5].values) /2

#variância e desvio padrão
dados['sepal_length'].var()
dados['sepal_length'].std()

#medidas de assimetria
dados['sepal_length'].skew()
sns.kdeplot(dados['sepal_length'])

#medidas de curtose
dados['sepal_length'].kurtosis()

########## CORRELAÇÃO DE PEARSON ##########

dados.corr('pearson') #  {'pearson', 'kendall', 'spearman'}
sns.heatmap(dados.corr(), annot = True)
sns.scatterplot(data=dados, x='petal_length', y='petal_width')

########## CORRELAÇÃO DE SPEARMAN ##########

dados.corr('spearman')
sns.heatmap(dados.corr('spearman'), annot = True)
sns.scatterplot(data=dados, x='sepal_length', y='petal_width')




































































