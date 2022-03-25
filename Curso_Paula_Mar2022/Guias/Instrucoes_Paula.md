# Instruções para instalação

### Neste documento estão os principais passos para instalação dos programas que vamos utilizar no curso.

## 1. Criar uma pasta chamada curso-python

### Dentro dessa pasta, criar a pasta instaladores que vai conter os arquivos executáveis (.exe)

## 2. Instalar o Miniconda

### Link:https://docs.conda.io/en/latest/miniconda.html

### Na página do link acima, em Windows installers, escolher a versão do Python 3.7.

## Se o seu Windows for 64 bits:

#### ● Clique em Miniconda3 Windows 64-bitpara fazer o download.

## Se o seu Windows for 32 bits:

#### ● Clique em Miniconda3 Windows 32-bitpara fazer o download.

Depois siga as seguintes instruções:

● Mova o arquivo .exe para a pasta /curso-python/instaladores
● Dê um duplo clique no arquivo .exe e inicie a instalação. (Executar, Next, I Agree, Just
Me, Next, Install, Next).
● Selecionar **“Add Anaconda to my Path environment variable”**.
● Selecionar **“Register Anaconda as my default Python3.7”**
● Por fim, “Finish”
A instalação vai durar aproximadamente 5 minutos.
Para verificar se a instalação ocorreu corretamente, abrir o **Anaconda Prompt** e digitar o
comando **conda list.**

## 3. Criar o Ambiente Virtual Python

Nosso ambiente virtual vai se chamar “ **t1** ”. Nele vamosinstalar as bibliotecas do Python que
nós vamos usar.
● Abra o **Anaconda Prompt** e digite o seguinte comando:
**conda create -n t**
Durante a instalação, quando for solicitado na tela, pressione “y” + Enter para continuar.

## 4. Instalar o Jupyter Notebook e as bibliotecas

```
● Ative o ambiente virtual. Para isto, digite no Anaconda Prompt:
```

**conda activate t**
● Para instalar o jupyter notebook digite no Anaconda Prompt:
**conda install jupyter notebook**
● Depois digite:
**pip install jupyter**
● Para instalar as bibliotecas:
**pip install pandas numpy matplotlib scipy statistics**
*Obs: Se precisar instalar mais alguma biblioteca depois dessa instalação (como a biblioteca do
seaborn, por exemplo), digite no Anaconda Prompt: **conda install -n t1 seaborn**
● Para abrir o jupyter notebook, digite no Anaconda Prompt:
**jupyter notebook**
Esse comando vai abrir uma tela no seu navegador da internet (provavelmente no google
chrome) e neste ambiente vamos criar as nossas rotinas.

*** Comandos úteis para o ambiente virtual ***
● Para desativar o ambiente virtual criado digite:
**conda deactivate**
● Para visualizar a lista de ambientes virtuais já criados:
**conda env list**
● Ver a lista de bibliotecas instaladas no ambiente virtual:
**conda list**

*** Links úteis ***
● Fala algumas diferenças entre o Anaconda e o Miniconda. Também dá alguns
comandos básicos de instalação:
https://ichi.pro/pt/13-comandos-conda-para-cientistas-de-dados-
● Link utilizado na parte da instalação das bibliotecas
**https://www.geeksforgeeks.org/how-to-setup-conda-environment-with-jupyter-notebook/**



