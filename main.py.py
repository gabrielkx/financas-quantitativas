import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pytz
import math
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
'''
Escopo função
SMA_10 = pd.DataFrame()
SMA_10['SMA_10'] = dataframe['close'].rolling(window=10).mean()
SMA_110
'''
dataframe = pd.read_csv('DOL1.csv', sep=',', header=0, usecols=["close" , "time" ,"open", "close"] )#, #nrows=100 )
dataframe = dataframe.sort_values(['time'])
#print(dataframe)
#print(dataframe.head(210))  # cria tabela

  # pega os valores da colune lata

# print(dataframe.loc[0:10,["time" , "open","close"]]) # seleciona valores das clounas de 0 a 100

# dataframe.loc[0:10,"open", "close"] # localiza os 10 1 elemntos de cada coluna

#print(dataframe.sort_values("time").head()) # ordena os valores de acorde com a coluna time

#dataframe.filter(regex=".-.").head() expressoes regulares achar valores

j=0
k=0
comprado = 1
vendido = -1
posicao = 0
posven=[]
poscom=[]
somarend=0
posprint=""

def SMA(days):
    days = int(input("Digite a quantidade de dias que deseja analisar , Quantidade mínima =1\n"))
    dayBegin = len(dataframe['close'] - 1) - days
    days = days-1
    SMA_5 = pd.DataFrame()
    SMA_5['SMA_5'] = dataframe['close'].rolling(window=5).mean()
    SMA_5

    SMA_10 = pd.DataFrame()
    SMA_10['SMA_10'] = dataframe['close'].rolling(window=10).mean()
    SMA_10

    SMA_20 = pd.DataFrame()
    SMA_20['SMA_20'] = dataframe['close'].rolling(window=20).mean()
    SMA_20

    SMA_50 = pd.DataFrame()
    SMA_50['SMA_50'] = dataframe['close'].rolling(window=50).mean()
    SMA_50

    SMA_100 = pd.DataFrame()
    SMA_100['SMA_100'] = dataframe['close'].rolling(window=100).mean()
    SMA_100

    SMA_200 = pd.DataFrame()
    SMA_200['SMA_200'] = dataframe['close'].rolling(window=200).mean()
    SMA_200

    def vendido(j, list=[], s=0):
        global posicao
        global vendido
        global posven
        if i == len(dataframe['close']) - 1 and posicao > 0:
            print('vendido')
            posven.append(j)

        elif list[j] < 0:
            if s == -1:
                pass
            else:
                posicao = vendido
                print('vendido')
                posven.append(j)


    def compra(j, list=[], s=0):
        global posicao
        global comprado
        global poscom
        if i == len(dataframe['close']) - 1 and posicao < 0:
            print('comprado')
            poscom.append(j)

        elif list[j] > 0:
            if s == 1:
                pass
            else:
                posicao = comprado
                poscom.append(j)
                print('comprado')

    # define as variáveis
    j=0
    vl50 = 0
    vl5 = 0
    vl10 = 0
    vl20 = 0
    vl100 = 0
    vl200 = 0
    x = 0
    y=0
    list = []

    for i in range(dayBegin,len(dataframe['close']),1):
        global k
        k=i
        if SMA_5['SMA_5'][i] == None:
            vl5 = vl5 + 0
        elif SMA_5['SMA_5'][i] < dataframe['close'][i]:
            vl5 = vl5 + +1
        elif (SMA_5['SMA_5'][i] > dataframe['close'][i]) and (SMA_5['SMA_5'][i] !=None):
            vl5 = vl5  -1

        if SMA_10['SMA_10'][i] == None:
            vl10 = vl10 + 0
        elif SMA_10['SMA_10'][i] < dataframe['close'][i]:
            vl10 = vl10 + 1
        elif (SMA_10['SMA_10'][i] > dataframe['close'][i]) and (SMA_10['SMA_10'][i] !=None):
            vl10 = vl10  -1
        #print(vl10)


        if SMA_20['SMA_20'][i] == None:
            vl20 = vl20 + 0
        elif SMA_20['SMA_20'][i] < dataframe['close'][i]:
            vl20 = vl20 + 1
        elif (SMA_20['SMA_20'][i] > dataframe['close'][i]) and(SMA_20['SMA_20'][i] !=None):
            vl20 = vl20  -1

        if SMA_50['SMA_50'][i] == None:
            vl50 = vl50 + 0
        elif SMA_50['SMA_50'][i] < dataframe['close'][i]:
            vl50 = vl50 + 1
        elif (SMA_50['SMA_50'][i] > dataframe['close'][i]) and(SMA_50['SMA_50'][i] !=None):
            vl50 = vl50  -1

        if SMA_100['SMA_100'][i] == None:
            vl100 = vl100 + 0
        elif SMA_100['SMA_100'][i] < dataframe['close'][i]:
            vl100 = vl100 + 1
        elif (SMA_100['SMA_100'][i] > dataframe['close'][i]) and (SMA_100['SMA_100'][i] !=None):
            vl100 = vl100  -1

        if SMA_200['SMA_200'][i] == None:
            vl200 = vl200 + 0
        elif SMA_200['SMA_200'][i] < dataframe['close'][i]:
            vl200 = vl200 + 1
        elif (SMA_200['SMA_200'][i] > dataframe['close'][i]) and (SMA_200['SMA_200'][i] !=None):
            vl200 = vl200 -1


        #Cria lista das somas diarias
        soma= vl5 + vl10 + vl20 + vl50 +vl100 +vl200
        list.append(soma)
        print(" A soma dos pontos do dia {}  é {} + {} +{} + {} + {} +{} = {}  index {} ".format(dataframe['time'][i] ,vl5, vl10, vl20, vl50 , vl100, vl200, list[j],j,))



        #chamando funções de compra e venda dentro do for
        vendido(j, list,posicao)
        compra(j,list,posicao)

        # incrementando j para o criar lista de somas e zerando variaveis
        j=j+1
        vl5 = 0
        vl10 = 0
        vl20 = 0
        vl50=0
        vl100 = 0
        vl200 = 0
        soma=0

h=1
valordefaul=201
SMA(valordefaul)
if (len(poscom) > len(posven)):
    for i in range(len(posven)):
        if poscom[i]>posven[i]:
            compra=poscom[i]
            venda=posven[i]
            rendimento = ((dataframe['close'][venda]/dataframe['close'][compra])) -1
            rendimento=rendimento*100
        #print("{:.2f}".format(rendimento))
        #print(dataframe['close'][venda])
        #print(dataframe['close'][compra])
            somarend=rendimento+somarend
            print("  trade {}  rendimento total ={:.2f}%".format(h,somarend))
            h = h + 1

        elif poscom[i]<posven[i]:
            compra=poscom[i]
            venda=posven[i]
            rendimento = ((dataframe['close'][venda]/dataframe['close'][compra])) -1
            rendimento=rendimento*100
        #print("{:.2f}".format(rendimento))
        #print(dataframe['close'][venda])
        #print(dataframe['close'][compra])

            somarend=rendimento+somarend
            print("  trade {}  rendimento total ={:.2f}%".format(h,somarend))
            h = h + 1

elif (len(poscom) < len(posven)):
    for i in range(len(posven)):
        if poscom[i]>posven[i]:
            compra=poscom[i]
            venda=posven[i]
            rendimento = ((dataframe['close'][venda]/dataframe['close'][compra])) -1
            rendimento=rendimento*100
        #print("{:.2f}".format(rendimento))
        #print(dataframe['close'][venda])
        #print(dataframe['close'][compra])
            somarend=rendimento+somarend
            print("  trade {}  rendimento total ={:.2f}%".format(h,somarend))
            h = h + 1

        elif poscom[i]<posven[i]:
            compra=poscom[i]
            venda=posven[i]
            rendimento = ((dataframe['close'][venda]/dataframe['close'][compra])) -1
            rendimento=rendimento*100
        #print("{:.2f}".format(rendimento))
        #print(dataframe['close'][venda])
        #print(dataframe['close'][compra])

            somarend=rendimento+somarend
            print("  trade {}  rendimento total ={:.2f}%".format(h,somarend))
            h = h + 1




