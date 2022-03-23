#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 18:21:23 2022

@author: samantha
"""

'''
            MANIPULANDO ARQUIVOS
'''

import pandas as pd
import numpy as np
import datetime

path = '/media/samantha/OCEAN/git/Learning/Curso_Paula_Mar2022/dados/'
arq_nome = 'boia_santos.txt'

dados = pd.read_csv(path+arq_nome, sep=',', header = 0, index_col=0, parse_dates = ['# Datetime'],
                    date_parser = lambda x: datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S'),
                    usecols = ['# Datetime', 'Wvht', 'Wmax', 'Dpd'])

# Renomear a altura significativa de onda para Hs, o eperíodo de pico é Tp, e a direção média Dm
dados.rename(columns={'Wvht': 'Hs', 'Dpd' : 'Tp', 'Wmax' : 'Dm'}, inplace=True)

dados.head()

'############   2. DADOS FALTANTES   ###########'

# Verifica se tem dados faltantes
dados.isnull().values.any()
# Conta quantos dados faltantes
dados.isnull().sum().sum()

# apresenta a quantidade de dados no dataframe
dados.shape

# Mostra quantas colunas tem no dado
dados.shape[1]

# Mostra quantas linhas tem no dado
dados.shape[0]

# Quantas datas tem entre a data final e a data inicial
datas = pd.date_range(dados.index[0], dados.index[-1], freq='H')
datas.shape

dados_c = dados.reindex(datas)

# Altera os valores nan
dados_c = dados_c.replace(-9999.00, np.nan)

# Verifica se tem dados faltantes
dados_c.isnull().values.any()
# Conta quantos dados faltantes
dados_c.isnull().sum().sum()


dados_semnan = dados_c.dropna()
print('Dados sem NaN = ', dados_semnan.shape[0])

# Criando DataFrame com duplicada
dfdup = dados_semnan.append([dados_semnan.loc['2011-04-12 19:00:00']])
print(dfdup)

# Remover dados duplicados (por exemplo: duas linhas com a mesma data)
dfdup = dfdup[~dfdup.index.duplicated()]
print(dfdup)

'############   3. ESTATÍSTICAS BÁSICAS   ###########'

print(dados_c)
dados_c.describe()

# o count() apenas conta os dados que não são nans
print(dados_c['Hs'].count())

# o numpy costuma ser bem mais rápido ao calcular as estatísticas

# Média
%time print('Média de Hs (pandas) =', dados_c['Hs'].mean())
%time print('Média de Hs (pandas) =', np.mean(dados_c['Hs']))

# Desvio padrão
%time print('Desvio padrão de Hs (pandas) = ', dados_c['Hs'].std())
%time print('Desvio padrão de Hs (numpy) = ', np.std(dados_c['Hs']))

# Criação de lista com valores aleatórios
aleat = np.random.rand(25)
print(aleat)

# Fixar a aleatoriedade
np.random.seed(50)
aleat = np.random.rand(25)
print(aleat)

'############   4. ANÁLISES ANUAIS   ###########'

# Escolhendo apenas um ano
dados_c['2017']

print('Máximo Hs em 2017 = ', dados_c.loc['2017'].Hs.max())
print('Máximo Tp em 2017 = ', dados_c.loc['2017'].Tp.max())
print('Máximo Dm em 2017 = ', dados_c.loc['2017'].Dm.max())






# Simplificando a escrita

hs_2017 = dados_c.loc['2017'].Hs

df_2017 = dados_c.loc['2017']

df_2017.index.name='# Datetime'

df_2017.to_csv(path+'boia_santos_2017.txt', index=True)



'############   5. ANÁLISES MENSAIS   ###########'

dados_jan = dados_c[dados_c.index.month == 1]
print(dados_jan)





























































