## PyInvest

## Imports

import math
import statistics
import datetime
import locale
import random

## Função para evitar entradas incorretas

def dataInput(text):
    while True:
        data = input(text)
        try:
            data = float(data)
            if (data >= 0):
                return(data)
            else:
                print("Numero negativo inválido.")
        except ValueError:
            print("Valor inválido.")

## Conversão do CDI anual para o CDI mensal

def calcCDIAnoPraMes():
    cdiMensal = ((1 + cdiAnual)**(1/12)) - 1
    return(cdiMensal)

## Cálculo do total investido

def calcTotalInvest():
    totalInvest = capitalInicial + (aporteMensal * prazoInvest)
    return(totalInvest)

## Cálculo do CDB

def calcCDB():
    montante = capitalInicial
    counter = 0
    for i in range(0, int(prazoInvest)):
        montante = (montante + aporteMensal) * (1 + cdiMensal)
        counter += 1
    print(f"counter: {counter}")
    return(montante)

def impostoIRCDB():
    
    if prazoInvest:
        return()

## Inputs

'''capitalInicial = dataInput("Insira a capital inicial (R$): ")
aporteMensal = dataInput("Insira o aporte mensal (R$): ")
prazoInvest = dataInput("Insira o prazo do investimento (em meses): ")
cdiAnual = dataInput("Insira o CDI anual (%): ")/100
percCDIemCDB = dataInput("Insira o percentual do CDI aplicado ao CDB (%): ")/100
percCDIemLCIA = dataInput("Insira o percentual do CDI aplicado à LCI/LCA (%): ")/100
rentMensalFII = dataInput("Insira a rentabilidade mensal esperada do FII (%): ")/100
metaFinanceira = dataInput("Insira a meta financeira desejada (R$): ")'''
start = datetime.date.today()

## Testes exemplo de execução 1

capitalInicial = 8000
aporteMensal = 500
prazoInvest = 12
cdiAnual = 12/100
percCDIemCDB = 100/100
percCDIemLCIA = 90/100
rentMensalFII = 1/100
metaFinanceira = 16000
end = start + datetime.timedelta(days=prazoInvest)

## Calculos

cdiMensal = calcCDIAnoPraMes()
totalInvestido = calcTotalInvest()


## Prints dos testes

print(f"CDI Mensal: {(calcCDIAnoPraMes() * 100):.2f}%")
print(f"CDB: {calcCDB():.2f}")
print(start, end)