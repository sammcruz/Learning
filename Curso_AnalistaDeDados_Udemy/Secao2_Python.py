#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 18:48:07 2022

@author: samantha
"""

import statistics
import random
import math
import time
import datetime


# Todos os tipos de variáveis
String = str('Olá Mundo!')
Inteiro = int(10)
Flutuante = float(10.99)
Complex = complex(1j)
Lista = list( ('Maça', 'Morango', 'Pera') )
Tupla = tuple( ('Maça', 'Morango', 'Pera') )
Range = range(6)
Dicionario = dict(nome='Odemir', age=29)
Set = set( ('Maça', 'Morango', 'Pera') )
Fronzet = frozenset( ('Maça', 'Morango', 'Pera') )
Boleano = bool(5)
Bytes = bytes(5)
ByteArray = bytearray(5)
Memoryview = memoryview( bytes(5) )


 # Mostrando os Valores
print( type(String) )
print( type(Inteiro) )
print( type(Flutuante) )
print( type(Complex) )
print( type(Lista) )
print( type(Tupla) )
print( type(Range) )
print( type(Dicionario) )
print( type(Set) )
print( type(Fronzet) )
print( type(Boleano) )
print( type(Bytes) )
print( type(ByteArray) )
print( type(Memoryview) )
print( type(Data) )


# Fatiamento de strings
Minha_String = 'Aprender Python é Top!'

print(type(Minha_String))
print(len(Minha_String))

print(Minha_String[0])
print(Minha_String[-1])
print(Minha_String[-10])
print(Minha_String[9:15])

# Manipulação de Strings

String = 'Olá Mundão!'
len(String), type(String)
String.replace('Mundão', 'Mundo')
String.startswith('Olá')
String.endswith('!')

Nome = 'Ademir'
Nome.capitalize()

String_CPF = '123456789'
String_CPF.isdigit()

Minha_String.isalnum()
Minha_String.isalpha()
Nome.upper(), Nome.lower()
Frase = 'Hoje o dia está calor!!!'
Frase.find('dia')

Endereço = ' R Augusta 120, SP '
Endereço.strip()

Palavra = 'Rua Augusta 150, centro, SP'
Palavra.split(',')

# Comando input

Nome = input('Digite seu nome: ')
print('Seu nome é ', Nome)


'''
##########################  DATETIME  
'''


Dia_Hoje = datetime.datetime.today().date()
type(Dia_Hoje)
print(Dia_Hoje)
print(Dia_Hoje.year)
print(Dia_Hoje.month)
print(Dia_Hoje.day)

Data_1 = datetime.date(2022, 2, 1)
print(Data_1)

Dia_Hoje-Data_1

Data_1.strftime('%d/%m/%y')
Dia_Hoje + datetime.timedelta(days=30)
print(Dia_Hoje)


'''
##########################  DATETIME  
'''


print('Começei agora')
time.sleep(3)
print("Terminei")

Agora = time.localtime()
print(Agora)
print(type(Agora))

time.strftime('%m/%d/%y, %H:%M:%S', Agora)

Time_Texto = '21 June, 2021'

Time_Time = time.strptime(Time_Texto, '%d %B, %Y')

print(Time_Time)


'''
##########################  MATH  
'''


Tupla = (10, 5, 20, 30, 40)
min(Tupla), max(Tupla), abs(-7.25)
pow(3, 4)
math.sqrt(81), math.ceil(1.4), math.floor(1.4)
math.pi


'''
##########################  random  
'''


Lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.choice(Lista)
Palavra = 'Odemir'
random.choice(Palavra)
random.randint(0, 1000)

'''
##########################  STATISTICS  
'''


Lista = [12, 15, 28, 56, 78, 80]

statistics.mean(Lista)
statistics.median(Lista)
statistics.mode(Lista)

'''
##########################  RANGE, FOR, WHILE, BREAK E CONTINUE  
'''

listinha=[range(0,8,2)]
print(listinha)
print(type(listinha))

enumerate()

[Numero ** 2 for Numero in range(10)]

for Loop in range(0,10):
    Lista.append(Loop)

Lista = ['Brasil', 'Argentina', 'Uruguai', 'Paraguai', 'Chile', 'Bolivia', 'Colômbia']
print(Lista)

for Index, Pais in enumerate(Lista):
    print(Index, Pais)
    print(type(Pais), type(Index), type(Lista))

Parar=0
while Parar <=10:
    print(Parar)
    Parar +=1
    
while True:
    Eu= random.randint(0,8)
    Contra_Voces = random.randint(2,10)
    
    print('Eu tirei o valor:', Eu)
    print('Vcs tiraram o ', Contra_Voces)
    
    if Eu > Contra_Voces:
        print ('Ganhei!')
        break

'''
##########################  FUNÇÃO
'''

def Boas_Vindas():
    print (' Seja Bem Viada !!')
Boas_Vindas()

def Somar(a1,a2):
    Soma = a1 + a2
    print("A Soma de ",a1," com ",a2," é igual a",Soma)
Somar(1,2)

'''
##########################  FUNÇÃO LAMBDA
'''
# É uma pequena função anônima

Funcao_Soma = lambda valor: valor + 10
Funcao_Soma(1)

Func_Soma2 = lambda valor_1, valor_2: valor_1 + valor_2
Func_Soma2(1,5)

Exemplo4 = lambda Valor: 'Verdadeiro' if Valor %2 == 0 else 'Falso'
Exemplo4(3)

'''
##########################  TRY EXCEPT FINALLY
'''

try:
    0/0
    print('Deu certo o codigo')
except:
    print('Ocorreu um erro')
finally:
    print('Esse roda de qqr jeito')

'''
##########################  CLASSES/OBJETOS
'''

class Pessoas:
    
    def __init__(self, Nome, Idade):
        self.Nome = Nome
        self.Idade = Idade
    def Boas_Vindas(self):
        print("Seja Bem vindo")
        
    def Recusado(self):
        print('Seu acesso foi recusado')
        
    def Maior_Idade(self):
        if self.Idade >= 18:
            print('Usuário é maior de idade')
            self.Boas_Vindas()
        else:
            print('Usuário é menor de idade')
            self.Recusado()
            
Dados = Pessoas ('Odemir', 12)
Dados.Maior_Idade()

'''
##########################  PRINT FORMATADO 
'''

print('Soma de 2 + 2 é:', 2+2)
print( f'Soma de 2 + 2 é: { round (2+2) }')
print('soma de 2 + 2 é: {}'.format(2+2))











