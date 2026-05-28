## Single-player E multi-player

## O baralho é composto por diversas cartas, cada uma com um nome e um conjunto de atributos
## numéricos (ex: Velocidade, Peso, Potência).

## As cartas são distribuídas aleatoriamente entre os dois jogadores

## A cada rodada, o jogador da vez escolhe um atributo de sua carta do topo. Esse valor é comparado
## com o mesmo atributo da carta do topo do adversário.

## Quem tiver o maior valor vence a rodada e leva ambas as cartas para o final do seu monte.

## Se houver empate no atributo escolhido, as cartas de ambos os jogadores vão para uma lista de monte
## de espera (ou descarte). O vencedor da rodada seguinte ganha as cartas daquela rodada mais todas as
## cartas acumuladas no monte de espera.

## O jogo termina quando um jogador possuir todas as cartas do baralho.


## Fluxo obrigatório:
## 1. Menu Inicial: Apresentar as opções: (1) Single Player, (2) Multiplayer, (3) Sair.
## 2. Configuração: Criar o baralho, embaralhar e dividir as listas mao_jogador1 e mao_jogador2.
## 3. Loop Principal: Enquanto ambos os jogadores tiverem cartas:
##      Exibir a carta do topo do jogador atual (apenas nome e atributos).
##      Solicitar que o usuário escolha o atributo através do índice (Ex: "Digite 1 para Velocidade, etc.)
##      Comparar os valores.
##      Exibir o vencedor da rodada ou informar o empate.
##      Gerenciar o movimento das cartas (incluindo o monte de espera em caso de empate).
## 4. Finalização: Declarar o vencedor absoluto e retornar ao menu.

## Bônus:
## ● Ler os detalhes e tipos de cartas de um arquivo texto
## ● Seu jogo pode ter vários tipos de super Trunfo, e os jogadores devem escolher com qual jogar
## ● Ranking de jogadores armazenado em arquivos


## Código de fato:

import random
jogadores = 0
BIBLIOTECACARTAS = [
    ("Jamil",       90, 34, 68),
    ("Alcides",    100,  2, 46),
    ("Carolina",    85, 15, 37),
    ("Paula",       65, 93, 55),
    ("Elizangela",  83, 45, 52),
    ("Fernando",     2,  1, 22),
    ("Miguel",      77, 10, 18)  
]
NOME = 0; ATRIBUTO1 = 1; ATRIBUTO2 = 2; ATRIBUTO3 = 3
NOMESATRIBUTOS = ["Nome", "Lógica", "Fé", "Idade"]
ESCALASATRIBUTOS = ((0,100), (0, 100), (17,70))

def menu_opcoes(pergunta, max):
    escolha = 0
    while escolha > max or escolha < 1:
        print(pergunta)
        escolha = int(input())
    return escolha


def menu_principal():
    global jogadores
    global continuar
    escolha = menu_opcoes("""
Aviso legal: Qualquer semelhança com figuras reais é mera coincidencia.
                          
Bem-vindo ao superTrunfo! Escolha um modo de jogo:
1 - Single Player 
2 - Multiplayer
3 - Sair""", 3)
    match escolha:
        case 1:
            jogadores = 1
        case 2:
            jogadores = 2
        case 3:
            continuar = False

def plural_carta(mao):
    string = "carta" if len(mao) == 1 else "cartas"
    return string

def embaralhar_maos(mao_1, mao_2, monte):
    ## Definindo variável impar
    impar = 1 if len(monte)%2 != 0 else 0

    ## Embaralhando cartas da mão do Jogador 1
    for _ in range((len(monte)//2)):
        carta = random.choice(monte)
        mao_1.append(carta)
        monte.remove(carta)

    ## Embaralhando cartas da mão do Jogador 2
    for _ in range(len(monte) - impar):
        carta = random.choice(monte)
        mao_2.append(carta)
        monte.remove(carta)


def jogada_player(mao_jogador, mao_oponente, monte):
    ## Exibir a carta do topo do jogador atual (apenas nome e atributos).
    carta_atual = mao_jogador[0]; carta_oponente = mao_oponente[0]
    print(f"""Sua carta atual é: {carta_atual[NOME]}
1. {NOMESATRIBUTOS[ATRIBUTO1]}: {carta_atual[ATRIBUTO1]}
2. {NOMESATRIBUTOS[ATRIBUTO2]}: {carta_atual[ATRIBUTO2]}
3. {NOMESATRIBUTOS[ATRIBUTO3]}: {carta_atual[ATRIBUTO3]}""")
    
    escolha = menu_opcoes(f"Com qual atributo você deseja competir? (De 1 a 3):", 3)

    print(f"""
    Batalha Começou!
    
    {carta_atual[NOME]} VS {carta_oponente[NOME]}

    Atributo de batalha: {NOMESATRIBUTOS[escolha]}""")

    if carta_atual[escolha] > carta_oponente[escolha]:
        passar_cartas(mao_oponente, mao_jogador, monte, False)
        print(f"\nVocê ganhou a batalha! Você está com {len(mao_jogador)} {plural_carta(mao_jogador)} e seu oponente com {len(mao_oponente)} {plural_carta(mao_oponente)}.\n")
    elif carta_atual[escolha] < carta_oponente[escolha]:
        passar_cartas(mao_jogador, mao_oponente, monte, False)
        print(f"\nVocê perdeu a batalha! Você está com {len(mao_jogador)} {plural_carta(mao_jogador)} e seu oponente com {len(mao_oponente)} {plural_carta(mao_oponente)}.\n")
    else:
        passar_cartas(mao_oponente, mao_jogador, monte, True)
        print(f"\nA batalha foi um empate! Você está com {len(mao_jogador)} {plural_carta(mao_jogador)} e seu oponente com {len(mao_oponente)} {plural_carta(mao_oponente)}.\n")
    print(f"O monte atualmente tem {len(monte)} {plural_carta(monte)}!")


def jogada_cpu(mao_cpu, mao_oponente, monte):
    carta_atual = mao_cpu[0]; carta_oponente = mao_oponente[0]
    maior_atributo = 1
    for i in range(1,4,1):
        if ((carta_atual[i] - ESCALASATRIBUTOS[i-1][0])/ESCALASATRIBUTOS[i-1][1] - ESCALASATRIBUTOS[i-1][0]) > ((carta_atual[maior_atributo]- ESCALASATRIBUTOS[maior_atributo-1][0])/ESCALASATRIBUTOS[maior_atributo-1][1] - ESCALASATRIBUTOS[maior_atributo-1][0]):
            maior_atributo = i

    print(f"""
    Batalha Começou!
    
    {carta_atual[NOME]} VS {carta_oponente[NOME]}

    Atributo de batalha: {NOMESATRIBUTOS[maior_atributo]}""")
      
    if carta_atual[maior_atributo] > carta_oponente[maior_atributo]:
        passar_cartas(mao_oponente, mao_cpu, monte, False)
        print(f"Seu inimigo ganhou a batalha! Você está com {len(mao_oponente)} {plural_carta(mao_oponente)} e seu oponente com {len(mao_cpu)} {plural_carta(mao_cpu)}.")
    elif carta_atual[maior_atributo] < carta_oponente[maior_atributo]:
        passar_cartas(mao_cpu, mao_oponente, monte, False)
        print(f"Seu oponente perdeu a batalha! Você está com {len(mao_oponente)} {plural_carta(mao_oponente)} e seu oponente com {len(mao_cpu)} {plural_carta(mao_cpu)}.")
    else:
        passar_cartas(mao_oponente, mao_cpu, monte, True)
        print(f"A batalha foi um empate! Você está com {len(mao_oponente)} {plural_carta(mao_oponente)} e seu oponente com {len(mao_cpu)} {plural_carta(mao_cpu)}.")
    print(f"O monte atualmente tem {len(monte)} {plural_carta(monte)}!")


def passar_cartas(perdedor, vencedor, monte, empate):
    if empate == False:
        vencedor.append(perdedor[0])
        perdedor.remove(perdedor[0])
        for carta in monte:
            vencedor.append(monte[0])
            monte.remove(monte[0])
        vencedor.append(vencedor[0])
        vencedor.remove(vencedor[0])
    else:
        monte.append(perdedor[0])
        monte.append(vencedor[0])
        perdedor.remove(perdedor[0])
        vencedor.remove(vencedor[0])


def declarar_vencedor(mao_1, mao_2):
    if len(mao_2) == 0:
        print("O jogador número 1 foi o vencedor.\n")
    elif len(mao_1) == 0:
        print("O jogador número 2 foi o vencedor.\n")
        

def iniciar_baralhos(mao_1, mao_2, monte):
    for i in BIBLIOTECACARTAS:
        monte.append(i)
    embaralhar_maos(mao_1, mao_2, monte)
    print(f"\n\nEmbaralhando...\n\nIniciando jogo...\n\nJogador 1: {len(mao_1)} {plural_carta(mao_1)}. \nJogador 2: {len(mao_2)} {plural_carta(mao_2)}.")


def game_loop():
    mao_1 = []
    mao_2 = []
    baralho = []
    iniciar_baralhos(mao_1, mao_2, baralho)

    ##print(f"\n baralho: {baralho} \n mão 1: {mao_1} \n mão 2: {mao_2} \n")

    ordem = random.randint(1,2)
    while not (len(mao_1) == 0 or len(mao_2) == 0):
        match jogadores:
            case 2:
                if ordem == 1:
                    input("\n\nJogada do jogador 1. Insira qualquer coisa para continuar.\n\n")
                    jogada_player(mao_1, mao_2, baralho)
                    ##print(f"\n baralho: {baralho} \n mão 1: {mao_1} \n mão 2: {mao_2} \n")
                    ordem = 2
                elif ordem == 2:
                    input("\n\nJogada do jogador 2. Insira qualquer coisa para continuar.\n\n")
                    jogada_player(mao_2, mao_1, baralho)
                    ##print(f"\n baralho: {baralho} \n mão 1: {mao_1} \n mão 2: {mao_2} \n")
                    ordem = 1
            case 1:
                if ordem == 1:
                    input("\n\nJogada do jogador. Insira qualquer coisa para continuar.\n\n")
                    jogada_player(mao_1, mao_2, baralho)
                    ##print(f"\n baralho: {baralho} \n mão 1: {mao_1} \n mão 2: {mao_2} \n")
                    ordem = 2
                elif ordem == 2:
                    input("\n\nJogada do computador. Insira qualquer coisa para continuar.\n\n")
                    jogada_cpu(mao_2, mao_1, baralho)
                    ##print(f"\n baralho: {baralho} \n mão 1: {mao_1} \n mão 2: {mao_2} \n")
                    ordem = 1
                    
    ##print(f"\n baralho: {baralho} \n mão 1: {mao_1} \n mão 2: {mao_2} \n")

    declarar_vencedor(mao_1, mao_2)


continuar = True
while continuar:
    menu_principal()
    if not continuar:
        continue
    game_loop()