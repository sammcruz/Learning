#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 18:21:23 2022

@author: samantha
"""

# Importando as bibliotecas
import pandas as pd
import numpy as np
import datetime

"""#### 1. Abrindo o arquivo da aula passada"""

# Definindo os caminhos
# Verificar o caminho correto no terminal
path = '/media/samantha/OCEAN/git/Learning/Curso_Paula_Mar2022/dados/'
print(path)

# Definindo os caminhos
arq_nome = 'boia_santos.txt'
print(path+arq_nome)

# Abrindo apenas as colunas que eu tenho interesse com usecols

# Quero apenas alguns dados de onda da boia
dados = pd.read_csv(path+arq_nome, sep=',', header = 0, index_col = 0, parse_dates = ['# Datetime'],
                   date_parser = lambda x: datetime.datetime.strptime(x ,"%Y-%m-%d %H:%M:%S"),
                   usecols = ['# Datetime','Wvht','Dpd','Mwd'])
print(dados)

# Renomeando
dados.rename(columns={'Wvht': 'Hs', 'Dpd': 'Tp', 'Mwd': 'Dm'}, inplace = True)
print(dados)

"""#### 2. Dados faltantes"""

# Checa se existem valores NaN em todo DataFrame
dados.isnull().values.any()

# Conta quantos valores NaN existem em todo DataFrame
dados.isnull().sum().sum()

# Verificar a quantidade de dados

# Quantos linhas eu tenho no DataFrame dos dados?
print(dados.shape)  #(linhas x colunas)

quant_linhas = dados.shape[1]
print(quant_linhas)

# 0 - linha
# 1 - coluna

# Quantos dados eu esperaria ter de 2011-01-01 00:00:00 a 2018-12-31 23:59:59??
datas = pd.date_range('2011-01-01 00:00:00', '2018-12-31 23:59:59', freq='H')

print(datas)
print('Número de linhas das datas: ', datas.shape[0])

# Coloca as datas completas no arquivo
# criei uma nova variável
dados_c = dados.reindex(datas)
print(dados_c)

# Checa se existem valores NaN em todo DataFrame
dados_c.isnull().values.any()
# Conta quantos valores NaN existem em todo DataFrame
dados_c.isnull().sum().sum()

# Conta quantos valores NaN existem em todo DataFrame
print("Dados faltantes em todo o DataFrame =", dados_c.isnull().sum().sum())

# Conta quantos valores NaN existem na coluna do Hs
print("Dados faltantes considerando apenas 1 coluna =", dados_c['Hs'].isnull().sum())

print("Dados completos =",dados_c.shape[0]) ## dados completos
print("Dados originais =",dados.shape[0])   ## dados originais

print("Quantidade de linhas/datas adicionadas =", dados_c.shape[0] - dados.shape[0])
print('\n')
print("Quantidade de dados faltantes considerando as 3 colunas =", (dados_c.shape[0] - dados.shape[0]) * 3)

print(dados_c)

# E os dados -9999.00?

# Em muitos dados isso significa o mesmo que NaN, então vamos substituir.

dados_c = dados_c.replace(-9999.00, np.nan)

print(dados_c)

# Checa se existem valores NaN em todo DataFrame
dados_c.isnull().values.any()

# Conta quantos valores NaN existem em todo DataFrame
dados_c.isnull().sum().sum()

# Conta quantos valores NaN existem na coluna de Hs
dados_c['Hs'].isnull().sum()

# Conta quantos valores NaN existem na coluna de Tp
dados_c['Tp'].isnull().sum()

# Conta quantos valores NaN existem na coluna de Dm
dados_c['Dm'].isnull().sum()

# Somando todos
dados_c['Hs'].isnull().sum()+dados_c['Tp'].isnull().sum()+dados_c['Dm'].isnull().sum()

# Para apagar todos os dados nan
dados_semnan = dados_c.dropna()
print(dados_semnan)

print("Dados sem NaN =",dados_semnan.shape[0])

# criando DataFrame com duplicata 
dfdup = dados_semnan.append([dados_semnan.loc['2011-04-12 19:00:00']]*5)
print(dfdup)

# Ordena o DataFrame e coloca as duplicatas no inicio
dfdup = dfdup.sort_index()
print(dfdup)

dfdup.index.duplicated().sum()

# Para remover dados duplicados (por exemplo: duas linhas com a mesma data)
dfdup = dfdup[~dfdup.index.duplicated()]
print(dfdup)

dfdup.index.duplicated().sum()

"""#### 3. Estatísticas básicas"""
print(dados_c)

dados_c.describe()

print(dados_c['Hs'].count())

dados_c['Hs'].isnull().sum()

print(dados_c.shape[0])

print( dados_c['Hs'].count() + dados_c['Hs'].isnull().sum() )

# Count
# Quantidade de dados de Hs que não são NaN (dados válidos)
print(dados_c['Hs'].count())

# Média
media_hs = dados_c['Hs'].mean()
print("Média de Hs =", media_hs)

# Média
# Geralmente o numpy faz os cálculos mais rapidamente, sobretudo quando você tem muitos dados
media_hs = np.mean(dados_c['Hs'])
print("Média de Hs =", media_hs)

# Para mostrar o resultado no print com o valor arredondado
print("Média de Hs =", "%.3f" % media_hs)

# np.round arrendonda o resultado. Neste caso quero só apresentar 3 casas decimais
print("Média de Hs =", np.round(media_hs, 3))

# Std - Desvio padrão
std_hs1 = dados_c['Hs'].std()
std_hs2 = np.std(dados_c['Hs'])


print("Desvio padrão de Hs =", std_hs1)
print("Desvio padrão de Hs (numpy) =", std_hs2)

# Retorna o valor dos percentis 25%, 50%, 75%
p25 = np.percentile(dados_c['Hs'], 25)
print("Percentil 25 =", p25)

## Retorna NaN, por quê?

# Retorna o valor dos percentis 25%, 50%, 75%
p25 = np.nanpercentile(dados_c['Hs'], 25)
print("Percentil 25 =", p25)

p50 = np.nanpercentile(dados_c['Hs'], 50)
print("Percentil 50 =", p50)

p75 = np.nanpercentile(dados_c['Hs'], 75)
print("Percentil 75 =", p75)

# Valores extremos
# Máximo
max_hs1 = dados_c['Hs'].max()
max_hs2 = np.max(dados_c['Hs'])

print('Máximo de Hs =', max_hs1)
print('Máximo de Hs (numpy) =', max_hs2)

# Valores extremos
# Mínimo
min_hs1 = dados_c['Hs'].min()
min_hs2 = np.min(dados_c['Hs'])

print('Mínimo de Hs =', min_hs1)
print('Mínimo de Hs (numpy) =', min_hs2)

# Criação de lista com valores aleatórios
   
# cria lista com 25 números aleatorios
aleat = np.random.randn(25)
print(aleat)

# Fixa a "aleatoriedade"
np.random.seed(47)

# Fixa a "aleatoriedade"
np.random.seed(50)
aleat = np.random.randn(25)
print(aleat)

"""#### 4. Análises anuais"""

# Agora vamos fazer análises anuais

# Quero analisar o ano de 2017
dados_c.loc['2017']

#Qual foi o maior valor de Hs em 2017
print("Máximo de Hs em 2017 =", dados_c.loc['2017'].Hs.max())

#Qual foi o maior valor de Tp em 2017
print("Máximo de Tp em 2017 =", dados_c.loc['2017'].Tp.max())

#Qual foi o maior valor de Dm em 2017
print("Máximo de Dm em 2017 =", dados_c.loc['2017'].Dm.max())

# Em que data ocorreu?

#Qual foi o maior valor de Hs em 2017
print("Data do máximo de Hs em 2017 =", dados_c.loc['2017'].Hs.idxmax())

#Qual foi o maior valor de Tp em 2017
print("Data do máximo de Tp em 2017 =", dados_c.loc['2017'].Tp.idxmax())

#Qual foi o maior valor de Dm em 2017
print("Data do máximo de Dm em 2017 =", dados_c.loc['2017'].Dm.idxmax())

# Para verificar no dia do máximo de Hs, o valor das outras variáveis
dados_c.loc[dados_c.loc['2017'].Hs.idxmax()]

# Quais são os valores de Hs no ano de 2017 acima de 2.29 (percentil 75)?
dados_c.loc['2017'].Hs >= 2.29

# Quais são os valores de Hs no ano de 2017 acima de 2.29 (percentil 75)?
dados_c.loc['2017'].Hs >= p75

# Quais são os valores de Hs no ano de 2017 acima de 2.29 (percentil 75)?
dados_c.loc['2017'].Hs[dados_c.loc['2017'].Hs >= p75]

# Simplificando a escrita
hs_2017 = dados_c.loc['2017'].Hs
hs_2017[hs_2017 >= p75]

# Salvando um novo DataFrame apenas com os dados de 2017

# Cria um DataFrame vazio
df_2017 = pd.DataFrame()
df_2017 = dados_c.loc['2017']
print(df_2017)

# Colocando um nome no nosso índice
df_2017.index.name = '# Datetime'
print(df_2017)

# Salvando um arquivo txt com os dados de 2017
df_2017.to_csv(path+'boia_santos_2017.txt', index=True)

# Separando dados de um período específico

# Quero apenas os dados de 2013 a 2016
print(dados_c)
mask = (dados_c.index >= '2013-01-01 00:00:00') & (dados_c.index <= '2016-12-31 23:59:59')
print(mask)

# Separando dados de um período específico

# Quero apenas os dados de 2013 a 2016
df_periodo = pd.DataFrame()
print(df_periodo)

df_periodo = dados_c.loc[mask]
print(df_periodo)

"""#### 5. Análises mensais"""

# Quero analisar o que aconteceu nos meses de maio ao longo de todos os anos.
maio = dados_c.loc['-05-']
print(maio)

maio17 = dados_c.loc['2017-05']
print(maio17)

# Voltando ao arquivo original
dados_c.index
dados_c.index.month
dados_c.index.day
dados_c.index.year

# Seleciono os meses de maio de todos os anos
dados_c.index.month == 5

# Seleciono os meses de maio de todos os anos

# Passar o nome do DataFrame
dados_c[dados_c.index.month == 5]
maio = dados_c[dados_c.index.month == 5]
dados_c.index.hour
manha = dados_c[(dados_c.index.hour >= 9) & (dados_c.index.hour <= 12)]
manha_semnan = manha.dropna()
print(manha_semnan)

# Quais foram os valores máximos do mês de maio de todos os anos?
maio.max()

# Ocorreu em qual data?
maio.idxmax()

# O que aconteceu em 2011-05-29 06:00:00?
maio.loc[maio.Hs.idxmax()]

# O que aconteceu em 2011-05-29 06:00:00? (Outra forma)
maio.loc['2011-05-29 06:00:00']

# Qual foi o segundo máximo de Hs que ocorreu nos meses de maio?

# Excluo o dia 2011-05-29 06:00:00 no meu df
maio2 = maio.drop('2011-05-29 06:00:00')
print(maio2)

# Qual o segundo maior valor de Hs dos meses de maio e em que data ocorreu?
print("Segundo maior Hs de maio = ", maio2.Hs.max())
print("Data: ", maio2.Hs.idxmax())

# Salvando um arquivo separado com os meses de maio
maio.index.name = '# Datetime'
maio.to_csv(path+'maio_2011_2018.txt', index=True)
path

# Separando os meses do verão (janeiro, fevereiro e março)
# meses 1, 2 e 3

# A barra | representa o operador lógico "OU"
# & representa o operador lógico "E"
dados_c[(dados_c.index.month == 1) | (dados_c.index.month == 2) | (dados_c.index.month == 3)]

# Nomeando
verao = dados_c[(dados_c.index.month == 1) | (dados_c.index.month == 2) | (dados_c.index.month == 3)]

# Agora posso fazer as análises
# Mostre as alturas significativas no verão que são maiores do que 3 metros
verao[verao.Hs > 3]

# Salvando um arquivo separado para cada mês

for i in range(1, 13):
    print("Mês = ", i)

# Salvando um arquivo separado para cada mês
dados_c[(dados_c.index.month == 1)]

# Salvando um arquivo separado para cada mês

for i in range(1, 13):
    print("Mês = ", i)
    
    # Separamos os arquivos do mês
    arq_mensal = dados_c[(dados_c.index.month == i)]
    # Colocamos o nome do índice
    arq_mensal.index.name = '# Datetime'
    # Salvamos o arquivo do mês
    arq_mensal.to_csv(path+'arquivo_mensal_'+i+'.txt')

type(i)

type(str(i))

# Salvando um arquivo separado para cada mês

for i in range(1, 13):
    
    print("Mês = ", i)
    
    # Separamos os arquivos do mês
    arq_mensal = dados_c[(dados_c.index.month == i)]
    # Colocamos o nome do índice
    arq_mensal.index.name = '# Datetime'
    # Salvamos o arquivo do mês
    arq_mensal.to_csv(path+'arquivo_mensal_'+str(i)+'.txt')

# Outra forma

# Criando lista
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
print(meses)
print(meses.shape)  #shape serve apenas para matrizes (arrays)
print(len(meses))

for i in range(len(meses)):
    print(i)

meses[0]

for i in range(len(meses)):
    print(meses[i])

for i in range(len(meses)):
    print(i)

for i in range(len(meses)):
    
    print("Mês = ", meses[i])
    
    # Separamos os arquivos do mês
    arq_mensal = dados_c[(dados_c.index.month == i+1)]  # Somo 1 ao índice
    # Colocamos o nome do índice
    arq_mensal.index.name = '# Datetime'
    # Salvamos o arquivo do mês
    arq_mensal.to_csv(path+'arquivo_mensal_'+meses[i]+'.txt')

# Loop com condicional

for i in range(len(meses)):
    print("Mês = ", meses[i])
    if i > 5:   ### Só pega os meses de julho em diante
        print("Mês que vai salvar = ", meses[i])
    
        # Separamos os arquivos do mês
        arq_mensal = dados_c[(dados_c.index.month == i+1)]  # Somo 1 ao índice
        # Colocamos o nome do índice
        arq_mensal.index.name = '# Datetime'
        # Salvamos o arquivo do mês
        arq_mensal.to_csv(path+'arquivo_mensal_'+meses[i]+'.txt')

"""### Exemplo com novo arquivo

#### Abrindo o arquivo do INMET (dados meteorológicos) da estação de Arraial do Cabo
"""

inmet = pd.read_csv(path+'INMET_SE_RJ_A606_ARRAIAL DO CABO_01-01-2018_A_31-12-2018.CSV',skiprows = 8,header = 0, 
                    index_col = 0, parse_dates = {'Datetime':['DATA (YYYY-MM-DD)','HORA (UTC)']})
print(inmet.head())

inmet = pd.read_csv(path+'INMET_SE_RJ_A606_ARRAIAL DO CABO_01-01-2018_A_31-12-2018.CSV',skiprows = 8,header = 0, 
                    index_col = 0, parse_dates = {'Datetime':['DATA (YYYY-MM-DD)','HORA (UTC)']}, encoding='latin-1')
print(inmet.head())

inmet = pd.read_csv(path+'INMET_SE_RJ_A606_ARRAIAL DO CABO_01-01-2018_A_31-12-2018.CSV', sep=';',skiprows = 8,header = 0, 
                    index_col = 0, parse_dates = {'Datetime':['DATA (YYYY-MM-DD)','HORA (UTC)']}, encoding='latin-1')
print(inmet.head())

inmet.index
inmet.loc['2018-01']

# Arquivos horários para diários
inmet2 = inmet.resample('1D').mean()
print(inmet2)
inmet3 = inmet.resample('1D')
print(inmet3)

# Vamos selecionar algumas colunas 
inmet.columns

# Escolho as colunas que eu quero e informo que meu decimal é vírgula!

inmet = pd.read_csv(path+'INMET_SE_RJ_A606_ARRAIAL DO CABO_01-01-2018_A_31-12-2018.CSV', sep=';',skiprows = 8,header = 0, 
                    index_col = 0, parse_dates = {'Datetime':['DATA (YYYY-MM-DD)','HORA (UTC)']}, encoding='latin-1', decimal=',',
                   usecols=['DATA (YYYY-MM-DD)','HORA (UTC)',
                            'PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO, HORARIA (mB)',
                            'TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)',
                            'VENTO, VELOCIDADE HORARIA (m/s)'])
print(inmet.head())

"""# DESAFIO

##### 1) Salve o valor de cada coluna (exceto o Datetime) como uma variável.
"""
inmet = inmet.replace(-9999.00, np.nan)
inmet = inmet.dropna()
inmet.columns
patm = inmet['PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO, HORARIA (mB)']
tempar =  inmet['TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)']
vento = inmet['VENTO, VELOCIDADE HORARIA (m/s)']

"""##### 2) Verifique quais são os valores máximos de cada variável"""
print('Pressão Atmosférica máxima = ', patm.max())
print('Temperatura do ar máxima = ', tempar.max())
print('Velocidade do vento máxima = ', vento.max())

"""##### 3) Verifique quais são os valores mínimos de cada variável"""
print('Pressão Atmosférica minima = ', patm.min())
print('Temperatura do ar mínima = ', tempar.max())
print('Velocidade do vento mínima = ', vento.max())

"""##### 4) Verifique em que data ocorreram esses valores máximos e mínimos"""
print('Pressão Atmosférica máxima ocorreu em ', patm.idxmax())
print('Temperatura do ar máxima ocorreu em ', tempar.idxmax())
print('Velocidade do vento máxima ocorreu em ', vento.idxmax())
print('Pressão Atmosférica minima ocorreu em ', patm.idxmin())
print('Temperatura do ar mínima ocorreu em ', tempar.idxmax())
print('Velocidade do vento mínima ocorreu em ', vento.idxmax())

"""##### 5) Calcule a média de cada variável"""
print('Pressão Atmosférica média = ', patm.mean())
print('Temperatura do ar média = ', tempar.mean())
print('Velocidade do vento média = ', vento.mean())

"""##### 6) Substitua os dados -9999 por NaN e apague os dados NaN"""
inmet = inmet.replace(-9999.0, np.nan)
inmet = inmet.dropna()

"""##### 7) Faça um plote para cada variável"""

import matplotlib.pyplot as plt

plt.plot(patm)
plt.plot(tempar)
plt.plot(vento)

# Questionamento: Como fazer a média móvel?

# Primeira opção: usando np.convolve
movmean = lambda x, w: np.convolve(x, np.ones(w), 'valid') / w

# Plotando:
plt.plot(np.array(patm))
plt.plot(movmean(patm,200))
plt.show()

plt.plot(np.array(tempar))
plt.plot(movmean(tempar,200))
plt.show()

plt.plot(np.array(vento))
plt.plot(movmean(vento,200))
plt.show()

# PROBLEMA: com np.convolve o resultado tem dimensão diferente
print('patm == movmean_patm ?', patm.shape == movmean(patm,200).shape)
print('tempar == movmean_tempar ?', tempar.shape == movmean(tempar,200).shape)
print('vento == movmean_vento ?', vento.shape == movmean(vento,200).shape)


# Segunda opção: usando bottleneck function move_mean
import bottleneck as bn

mvmean_bn = lambda x: bn.move_mean(x, window = 200, min_count = None)

# Plotando:
plt.plot(np.array(patm))
plt.plot(mvmean_bn(patm))
plt.show()

plt.plot(np.array(tempar))
plt.plot(mvmean_bn(tempar))
plt.show()

plt.plot(np.array(vento))
plt.plot(mvmean_bn(vento))
plt.show()

# Verificando o tamanho:
print('patm == movmean_patm ?', patm.shape == mvmean_bn(patm).shape)
print('tempar == movmean_tempar ?', tempar.shape == mvmean_bn(tempar).shape)
print('vento == movmean_vento ?', vento.shape == mvmean_bn(vento).shape)

# RESOLVIDO!

# Segundo problema encontrado: a função bn.move_mean preenche com NaN
# as pontas do vetor até o tamanho da janela ser atingido

# Vamos testar com o Pandas
data = np.array([10,5,8,9,15,22,26,11,15,16,18,7])

d = pd.Series(data)

print(patm.rolling(200).mean())

# Plotando:
plt.plot(patm)
plt.plot(patm.rolling(200).mean())
plt.show()

plt.plot(tempar)
plt.plot(tempar.rolling(200).mean())
plt.show()

plt.plot(vento)
plt.plot(vento.rolling(200).mean())
plt.show()

# Mesmo problemas dos NaN pode ser resolvido com o método df.fillna()

print(patm.rolling(200).mean())
print(patm.rolling(200).mean().interpolate(method='linear'))




