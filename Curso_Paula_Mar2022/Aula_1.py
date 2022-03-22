#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 18:18:51 2022

@author: samantha
"""

import pandas as pd
import numpy as np
import datetime

# criando variáveis
numero = 25
frac = 3.5
palavra ='python'
print (numero, frac, palavra)

# verificando o tipo de variável
numero = 25
frac = 3.5
palavra = 'python'
print (type( numero ), type( frac ), type( palavra ))

# tipo lista
lista = [1, 2, 3]
print(type(lista))

# operações básicas
soma = numero + 50
subtracao = 45 - 35
multiplicacao = 2 * 10
divisao = 31 / 5
exponencial = 2 ** 5
print("\nSoma = ", soma,"\nsubtracao = ", subtracao,"\nmultiplicacao = ", multiplicacao,"\ndivisao = ", divisao,"\nexponencial = ", exponencial)

# como obter a raíz quadrada de 25 ? (Resposta = 5)
raiz1 = 25 ** 1/2
raiz2 = 25 ** 0.5
raiz3 = 25 ** (1/2)

print("Raíz 1 = ", raiz1) # errado!
print("Raíz 2 = ", raiz2)
print("Raíz 3 = ", raiz3)

# simando strings
print(palavra)
print(type(palavra))

palavra0 = 'curso'
espaco0 = ' '
palavra1 = 'de'
espaco1 = ' '
print(palavra0 + espaco0 + palavra1 + espaco1 + palavra)
print('Curso de '+ palavra)

# operações básicas: True e False
x = 10
y = 5
z = 11

pergunta1 = x> y
print('X é maior que y? ', pergunta1)

pergunta2 = x == 2*y
print('x é igual a 2y?', pergunta2)

pergunta3 = x != z
print('x é diferente de z?', pergunta3)

pergunta4 = x == z
print('x é igual a z?', pergunta4)

# Condicionais
print('x = ', x)
print('y = ', y)
print('z = ', z)

if x == z:
    print('Sim! x é igual a z')
if x != z:
    print('Sim! x é diferente de z')

# if = se ; else = se não
if x != z:
    print('Sim! x é diferente de z')
else:
    print('Não! x é diferente de z')

# Usando o operador and ('E')
if x == 10 and y == 5:
    print('Sim!')
else:
    print('Não')

# Usando o operador or ('ou')
if x == 10 or y == 5:
    print('Sim!')
else:
    print('Não')

# Usando o operador and ('E')
if x == 10 and y == 6:    # para a resposta ser sim os dois valores tem que estar corretos
    print('Sim!')
else:
    print('Não')

# Usando o operador or ('ou')
if x == 10 or y == 6:    # Basta que apenas uma das condições seja verdadeira
    print('Sim!')
else:
    print('Não')

# Loops
for i in range(12):
    print(i)
    

for i in range(1, 13):
    print(i)

# Criando uma lista
meses = ['janeiro', 'fevereiro', 'março']
print('Lista de meses:', meses)
print('Comprimento da lista = ', len(meses))

print(meses[0])
print(meses[1])
print(meses[2])

print(meses[0][0:3])
print(meses[1][0:3])
print(meses[2][0:3])

for mes in range(3):
    print('indice: ', mes)
    print('mês: ', meses[mes])

for mes in meses:
    print(mes)

'''
        ABRINDO ARQUIVOS
'''

# Definindo os caminhos
# Verificar o caminho correto do aquivo
path = '/media/samantha/OCEAN/git/Learning/Curso_Paula_Mar2022/dados/'

# Definindo os caminhos
arq_nome = 'boia_santos.txt'
print(path+arq_nome)

# Abrindo o arquivo texto com a biblioteca pandas
# dados se torna um DataFrame que é o formato no pandas
dados = pd.read_csv(path+arq_nome)
dados.head()
dados.info()

# sep identifica o separados das colunas
# header identifica a linha onde está o cabeçalho
# index_col identifica a coluna onde está o índice
dados = pd.read_csv(path+arq_nome, sep=',', header = 0, index_col=0)
dados.head()
dados.info()

dados = pd.read_csv(path+arq_nome, sep=',', header = 0, index_col=0, parse_dates = ['# Datetime'],
                    date_parser = lambda x: datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))

dados.head()

# apresenta todos os indices
print(dados.index)
# apresenta todas as colunas
print(dados.columns)

# Soma 10000 a todos os valores do DataFrame
print(dados.add(10000)) # --> Não salva na variável dados

# Salvando na variável
dados2 = dados.add(10000)

# Divide todos os valores do DataFrame por 2
print(dados.div(2)) # --> Não salva na variável dados

# Acessa apenas uma coluna
dados['Wvht']
#ou
dados.Wvht

# Conta quantas vezes apareceu cada valor na coluna da altura significativa
print(dados['Wvht'].value_counts())

# Abrindo apenas as colunas que eu tenho interesse com usecols
dados = pd.read_csv(path+arq_nome, sep=',', header = 0, index_col=0, parse_dates = ['# Datetime'],
                    date_parser = lambda x: datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S'),
                    usecols = ['# Datetime', 'Wvht', 'Wmax', 'Dpd', 'Mwd', 'Spread'])

# Como apagar colunas
dados.drop(columns=['Wmax', 'Spread'], inplace = True)
print(dados)

# Renomear a altura significativa de onda para Hs, o eperíodo de pico é Tp, e a direção média Dm
dados.rename(columns={'Wvht': 'Hs', 'Dpd' : 'Tp', 'Mwd' : 'Dm'}, inplace=True)

# Para selecionar uma linha
dados.loc['2011-04-12 20:00:00']

tp1 = dados.loc['2011-04-12 20:00:00'].Tp
print(tp1)

# Abrindo arquivo folhas
folhas = pd.read_excel(path+'folhas_Especie_TIPO_FISIO_MEDIA.xlsx' )

# primeiras linhas
print(folhas.head())

# Últimas linhas
print(folhas.tail())

folhas = pd.read_excel(path+'folhas_Especie_TIPO_FISIO_MEDIA.xlsx', header = 0)
datas = pd.date_range('2008-08', '2020-01', freq = 'M')
print(datas)
anomes=datas.strftime('%Y-%m')
print(anomes)

folhas['datetime']=anomes
folhas.columns

folhas.set_index('datetime', inplace=True)
folhas.loc['2008-09']

folhas.drop(columns=['Anos', 'Mes'], inplace = True)

folhas.head()

folhas.rename(columns={'franja_rh': 'x', 'bacia_rh': 'y'}, inplace=True)

















