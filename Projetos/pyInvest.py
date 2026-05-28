## PyInvest

## Imports

import math
import statistics
import datetime
import locale
import random

## CONSTANTES
PERCPOUPANCA = 0.005
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

## Iniciando variáveis
mediaFII = 0
medianaFII = 0
desvioFII = 0
maiorValor = 0
maior = ""

## Função para evitar entradas incorretas

def dataInput(text):
    data = input(text)
    try:
        data = float(data)
        if (data >= 0):
            return(data)
        else:
            print("Numero negativo inválido.")
            exit()
    except ValueError:
        print("Valor inválido.")
        exit()

## Conversão do CDI anual para o CDI mensal

def calcCDIAnoPraMes(cdiAnual):
    cdiMensal = ((1 + cdiAnual)**(1/12)) - 1
    return(cdiMensal)

## Cálculo do total investido

def calcTotalInvest(capitalInicial, aporteMensal, prazoInvest):
    totalInvest = capitalInicial + (aporteMensal * prazoInvest)
    return(totalInvest)

## Cálculo do CDB
##Fórmula principal
def calcCDB(capitalInicial, aporteMensal, cdiMensal, cdiMensalPerc, prazoInvest, imposto):
    cdiMensal *= cdiMensalPerc
    montante = (capitalInicial * (1  + cdiMensal) ** prazoInvest) + ((aporteMensal * (((1 + cdiMensal) ** prazoInvest) - 1)) / cdiMensal)
    montante = montante - (montante - calcTotalInvest(capitalInicial, aporteMensal, prazoInvest)) * imposto
    return(montante)

## Cálculo do Imposto a ser aplicado

def calcImposto(start, dataResgate):
    diferenca = dataResgate - start
    
    if diferenca.days <= 180:
        return 0.225
    elif diferenca.days <= 360:
        return 0.2
    elif diferenca.days <= 720:
        return 0.175
    else:
        return 0.15


## Cálculo do LCI/LCA

def calcLCIA(capitalInicial, aporteMensal, cdiMensal, cdiMensalPerc, prazoInvest):
    cdiMensal *= cdiMensalPerc
    montante = (capitalInicial * (1  + cdiMensal) ** prazoInvest) + ((aporteMensal * (((1 + cdiMensal) ** prazoInvest) - 1)) / cdiMensal)
    return(montante)
    
## Cálculo da Poupança

def calcPoupanca(capitalInicial, aporteMensal, prazoInvest, PERCPOUPANCA):
    montante = (capitalInicial * (1  + PERCPOUPANCA) ** prazoInvest) + ((aporteMensal * (((1 + PERCPOUPANCA) ** prazoInvest) - 1)) / PERCPOUPANCA)
    return montante

## Cálculo do FII

def calcFII(capitalInicial, aporteMensal, prazoInvest, rentMensalFII):
    global mediaFII
    global medianaFII
    global desvioFII
    
    montante1 = simulacaoFII(capitalInicial, aporteMensal, prazoInvest, rentMensalFII)
    montante2 = simulacaoFII(capitalInicial, aporteMensal, prazoInvest, rentMensalFII)
    montante3 = simulacaoFII(capitalInicial, aporteMensal, prazoInvest, rentMensalFII)
    montante4 = simulacaoFII(capitalInicial, aporteMensal, prazoInvest, rentMensalFII)
    montante5 = simulacaoFII(capitalInicial, aporteMensal, prazoInvest, rentMensalFII)

    mediaFII = statistics.mean([montante1, montante2, montante3, montante4, montante5])
    medianaFII = statistics.median([montante1, montante2, montante3, montante4, montante5])
    desvioFII = statistics.stdev([montante1, montante2, montante3, montante4, montante5])

## Simulação do FII com variação de 3%

def simulacaoFII(capitalInicial, aporteMensal, prazoInvest, rentMensalFII):
    montante = (capitalInicial * (1  + rentMensalFII) ** prazoInvest) + ((aporteMensal * (((1 + rentMensalFII) ** prazoInvest) - 1)) / rentMensalFII)
    montante *= random.uniform(0.97, 1.03)
    return montante

## Cálculo da data de resgate
## Esse cálculo preza em manter o dia, ao invéz de adicionar dias (que podem variar de acordo com o mês). Exeções são para caso o dia não exista (como 2000-02-31)
## Nesse caso, ele volta a o último dia do mês anterior
def calcDataResgate(start, qtdMeses):
    qtdMeses += start.month
    anos = qtdMeses // 12
    meses = qtdMeses % 12
    try:
        dataResgate = datetime.date(year=(start.year + anos), month=(meses), day=start.day)
    except ValueError:
        proximoMes = datetime.date(year=(start.year + anos), month=(meses+1), day=1)
        dataResgate = proximoMes - datetime.timedelta(days=1)
    return dataResgate

## Função que formata os valores para reais

def formatarDinheiro(dinheiro):
    return locale.currency(dinheiro, symbol=True, grouping=True)

## Função que gera o relatório

def gerarRelatorio(start, dataResgate, totalInvestido, montCDB, montLCIA, montPoupanca, mediaFII, medianaFII, desvioFII, metaFinanceira, maior, maiorValor):
    print(f'''
{'=' * 62}
RELATÓRIO PYINVEST - {start.strftime("%x")}
Data estimada de resgate: {dataResgate.strftime("%x")}
Total investido: {formatarDinheiro(totalInvestido)}
{'-' * 62}
{'CDB':<10}: {formatarDinheiro(montCDB)}
{'Gráfico':<10}: {'█'*math.floor((montCDB/maiorValor)*50)}
{'LCI/LCA':<10}: {formatarDinheiro(montLCIA)}
{'Gráfico':<10}: {'█'*math.floor((montLCIA/maiorValor)*50)}
{'Poupança'}: {formatarDinheiro(montPoupanca)}
{'Gráfico':<10}: {'█'*math.floor((montPoupanca/maiorValor)*50)}
{'FII (Média)'}: {formatarDinheiro(mediaFII)}
{'Gráfico':<10}: {'█'*math.floor((mediaFII/maiorValor)*50)}
{'-' * 62}
Estatísticas FII (Mediana): {formatarDinheiro(medianaFII)}
Desvio padrão FII: {formatarDinheiro(desvioFII)}
Meta atingida? {'Sim' if maiorValor >= metaFinanceira else 'Não'}

Melhor opção: {maior} com {formatarDinheiro(maiorValor)}
''')

## Função achando qual o maior investimento, tanto em título quanto em valor

def acharMaiorInvestimento(montCDB, montLCIA, montPoupanca, mediaFII):
    global maior
    global maiorValor

    if montCDB > montLCIA:
        if montCDB > montPoupanca:
            if montCDB > mediaFII:
                maior = "CDB"
            else:
                maior = "FII"
        else:
            if montPoupanca > mediaFII:
                maior = "Poupanca"
            else:
                maior = "FII"
    else:
        if montLCIA > montPoupanca:
            if montLCIA > mediaFII:
                maior = "LCI/LCA"
            else:
                maior = "FII"
        else:
            if montPoupanca > mediaFII:
                maior = "Poupanca"
            else:
                maior = "FII"

    match maior:
        case "CDB":
            maiorValor = montCDB
        case "LCI/LCA":
            maiorValor = montLCIA
        case "Poupanca":
            maiorValor = montPoupanca
        case "FII":
            maiorValor = mediaFII

def printTitulo():
    print(f"{' PYINVEST ':=^62}")

## Testes exemplo de execução 1
"""capitalInicial = 8000
aporteMensal = 500
prazoInvest = 12
cdiAnual = 12/100
percCDIemCDB = 100/100
percCDIemLCIA = 90/100
rentMensalFII = 1/100
metaFinanceira = 16000"""

## Testes exemplo de execução 2
"""capitalInicial = 500000
aporteMensal = 1000
prazoInvest = 120
cdiAnual = 14.9/100
percCDIemCDB = 110/100
percCDIemLCIA = 90/100
rentMensalFII = 1.2/100
metaFinanceira = 1000000"""

## Main
## Título

printTitulo()

## Inputs

capitalInicial = dataInput("Insira o capital inicial (R$): ")
aporteMensal = dataInput("Insira o aporte mensal (R$): ")
prazoInvest = int(dataInput("Insira o prazo do investimento (em meses): "))
cdiAnual = dataInput("Insira o CDI anual (%): ")/100
percCDIemCDB = dataInput("Insira o percentual do CDI aplicado ao CDB (%): ")/100
percCDIemLCIA = dataInput("Insira o percentual do CDI aplicado à LCI/LCA (%): ")/100
rentMensalFII = dataInput("Insira a rentabilidade mensal esperada do FII (%): ")/100
metaFinanceira = dataInput("Insira a meta financeira desejada (R$): ")

## Resgatando data atual e achando a data onde a simulação acaba

start = datetime.date.today()
dataResgate = calcDataResgate(start, prazoInvest)

## Cálculos do CDI mensal e o total investido

cdiMensal = calcCDIAnoPraMes(cdiAnual)
totalInvestido = calcTotalInvest(capitalInicial, aporteMensal, prazoInvest)

## Cálculo do montante em cada tipo de investimento

montCDB = calcCDB(capitalInicial, aporteMensal, cdiMensal, percCDIemCDB, prazoInvest, calcImposto(start, dataResgate))
montLCIA = calcLCIA(capitalInicial, aporteMensal, cdiMensal, percCDIemLCIA, prazoInvest)
montPoupanca = calcPoupanca(capitalInicial, aporteMensal, prazoInvest, PERCPOUPANCA)
calcFII(capitalInicial, aporteMensal, prazoInvest, rentMensalFII)

## Rodando a função para achar qual o maior investimento

acharMaiorInvestimento(montCDB, montLCIA, montPoupanca, mediaFII)

gerarRelatorio(start, dataResgate, totalInvestido, montCDB, montLCIA, montPoupanca, mediaFII, medianaFII, desvioFII, metaFinanceira, maior, maiorValor) 