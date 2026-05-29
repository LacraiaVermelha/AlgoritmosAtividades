import random
jogadores = 0
BIBLIOTECACARTAS = [
    ("Jamil",       85, 15, 68),
    ("Alcides",     95, 5,  46),
    ("Carolina",    80, 15, 34),
    ("Paula",       65, 95, 54),
    ("Elisângela",  80, 20, 52),
    ("Fernando",    65, 5,  22),
    ("Miguel",      75, 0,  18),
    ("Everton",     75, 15, 34),
    ("Kishimoto",   90, 5,  46),
    ("Fabio",       70, 35, 48),
    ("Polly",       90, 5,  34),
    ("Jefferson",   95, 10, 50),
    ("RUBEN",      100, 100,32) ## Obrigado Ruben por nos deixar usar a sala da engenharia de solos <3
]
NOME = 0; ATRIBUTO1 = 1; ATRIBUTO2 = 2; ATRIBUTO3 = 3
NOMESATRIBUTOS = ["Nome", "Lógica", "Fé", "Idade"]
ESCALASATRIBUTOS = ((0,100), (0, 100), (17,70))


def menu_opcoes(pergunta, max):
    escolha = 0
    while escolha > max or escolha < 1:
        print(pergunta)
        try:
            escolha = int(input())
        except ValueError:
            print("Valor inválido.")
    return escolha


def menu_principal():
    global jogadores
    global continuar
    escolha = menu_opcoes(f"""{"-"*35}
{f'Aviso legal:':^35}
{f'Qualquer semelhança à figuras reais':^35}
{f'é mera coincidencia!':^35}
{"-"*35}

╭{('-'*35)}╮                          
|{f'Bem-vindo ao AlciTrunfo!':^35}|
|{f' ':^35}|
|{f'Escolha um modo de jogo:':^35}|
|{f'1 - Single Player ':^35}|
|{f'2 - Multiplayer':^35}|
|{f'3 - Sair':^35}|
╰{('-'*35)}╯""", 3)
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
    impar = 1 if len(monte) %2 != 0 else 0

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
    print(f"""╭{('-'*35)}╮
|{f'Sua carta atual é: {carta_atual[NOME]}':^35}|
|{f'1. {NOMESATRIBUTOS[ATRIBUTO1]}: {carta_atual[ATRIBUTO1]}':^35}|
|{f'2. {NOMESATRIBUTOS[ATRIBUTO2]}: {carta_atual[ATRIBUTO2]}':^35}|
|{f'3. {NOMESATRIBUTOS[ATRIBUTO3]}: {carta_atual[ATRIBUTO3]}':^35}|
╰{('-'*35)}╯\n""")
    
    escolha = menu_opcoes(f"Com qual atributo você deseja competir? (De 1 a 3):", 3)

    print(f"""┏{('━'*35)}┓
┃{f'Batalha Começou!':^35}┃
┃{f' ':^35}┃
┃{f'{carta_atual[NOME]} VS {carta_oponente[NOME]}':^35}┃
┃{f' ':^35}┃
┃{f'Atributo de batalha: {NOMESATRIBUTOS[escolha]}':^35}┃
┃{f' ':^35}┃""")

    if carta_atual[escolha] > carta_oponente[escolha]:
        passar_cartas(mao_oponente, mao_jogador, monte, False)
        print(f'''┃{f'Você ganhou a batalha!':^35}┃
┃{f'Você está com {len(mao_jogador)} {plural_carta(mao_jogador)}':^35}┃
┃{f'Seu oponente está com {len(mao_oponente)} {plural_carta(mao_oponente)}.':^35}┃''')
    elif carta_atual[escolha] < carta_oponente[escolha]:
        passar_cartas(mao_jogador, mao_oponente, monte, False)
        print(f'''┃{f'Você perdeu a batalha!':^35}┃
┃{f'Você está com {len(mao_jogador)} {plural_carta(mao_jogador)}':^35}┃
┃{f'Seu oponente está com {len(mao_oponente)} {plural_carta(mao_oponente)}.':^35}┃'''))
    else:
        passar_cartas(mao_oponente, mao_jogador, monte, True)
        print(f'''┃{f'A batalha foi um empate!':^35}┃
┃{f'Você está com {len(mao_jogador)} {plural_carta(mao_jogador)}':^35}┃
┃{f'Seu oponente está com {len(mao_oponente)} {plural_carta(mao_oponente)}.':^35}┃''')
    print(f'''┃{f'O monte atualmente tem {len(monte)} {plural_carta(monte)}!':^35}┃
┗{('━'*35)}┛''')


def jogada_cpu(mao_cpu, mao_oponente, monte):
    carta_atual = mao_cpu[0]; carta_oponente = mao_oponente[0]
    maior_atributo = 1
    for i in range(1,4,1):
        if ((carta_atual[i] - ESCALASATRIBUTOS[i-1][0])/ESCALASATRIBUTOS[i-1][1] - ESCALASATRIBUTOS[i-1][0]) > ((carta_atual[maior_atributo]- ESCALASATRIBUTOS[maior_atributo-1][0])/ESCALASATRIBUTOS[maior_atributo-1][1] - ESCALASATRIBUTOS[maior_atributo-1][0]):
            maior_atributo = i

    print(f"""┏{('━'*35)}┓
┃{f'Batalha Começou!':^35}┃
┃{f' ':^35}┃
┃{f'{carta_atual[NOME]} VS {carta_oponente[NOME]}':^35}┃
┃{f' ':^35}┃
┃{f'Atributo de batalha: {NOMESATRIBUTOS[maior_atributo]}':^35}┃
┃{f' ':^35}┃""")
      
    if carta_atual[maior_atributo] > carta_oponente[maior_atributo]:
        passar_cartas(mao_oponente, mao_cpu, monte, False)
        print(f'''┃{f'Seu oponente ganhou a batalha!':^35}┃
┃{f'Você está com {len(mao_oponente)} {plural_carta(mao_oponente)}':^35}┃
┃{f'Seu oponente está com {len(mao_cpu)} {plural_carta(mao_cpu)}.':^35}┃''')
    elif carta_atual[maior_atributo] < carta_oponente[maior_atributo]:
        passar_cartas(mao_cpu, mao_oponente, monte, False)
        print(f'''┃{f'Seu oponente perdeu a batalha!':^35}┃
┃{f'Você está com {len(mao_oponente)} {plural_carta(mao_oponente)}':^35}┃
┃{f'Seu oponente está com {len(mao_cpu)} {plural_carta(mao_cpu)}.':^35}┃''')
    else:
        passar_cartas(mao_oponente, mao_cpu, monte, True)
        print(f'''┃{f'A batalha foi um empate!':^35}┃
┃{f'Você está com {len(mao_oponente)} {plural_carta(mao_oponente)}':^35}┃
┃{f'Seu oponente está com {len(mao_cpu)} {plural_carta(mao_cpu)}.':^35}┃''')
    print(f"┃{f'O monte atualmente tem {len(monte)} {plural_carta(monte)}!':^35}┃    \n┗{('━'*35)}┛\n")


def passar_cartas(perdedor, vencedor, monte, empate):
    if empate == False:
        vencedor.append(vencedor[0])
        vencedor.remove(vencedor[0])
        vencedor.append(perdedor[0])
        perdedor.remove(perdedor[0])
        for carta in monte:
            vencedor.append(carta)
        monte.clear()
    else:
        monte.append(vencedor[0])
        monte.append(perdedor[0])
        vencedor.remove(vencedor[0])
        perdedor.remove(perdedor[0])


def declarar_vencedor(mao_1, mao_2):
    if len(mao_2) == 0 and len(mao_1) == 0:
        print("O jogo foi um empate.\n")
    elif len(mao_2) == 0:
        print("O jogador número 1 foi o vencedor.\n")
    elif len(mao_1) == 0:
        print("O jogador número 2 foi o vencedor.\n")
        

def iniciar_baralhos(mao_1, mao_2, monte):
    for i in BIBLIOTECACARTAS:
        monte.append(i)
    embaralhar_maos(mao_1, mao_2, monte)
    print(f'''
{f'Embaralhando...':^35}
{f' ':^35}
{f'Iniciando jogo...':^35}
{f' ':^35}
{f'Jogador 1: {len(mao_1)} {plural_carta(mao_1)}.':^35}
{f'Jogador 2: {len(mao_2)} {plural_carta(mao_2)}.':^35}''')


def game_loop():
    mao_1 = []
    mao_2 = []
    baralho = []
    iniciar_baralhos(mao_1, mao_2, baralho)

    ordem = random.randint(1,2)
    while not (len(mao_1) == 0 or len(mao_2) == 0):
        match jogadores:
            case 2:
                if ordem == 1:
                    input(f"\n{'Jogada do jogador 1.':^35} \n{'Insira qualquer coisa para continuar.':^35}\n")
                    jogada_player(mao_1, mao_2, baralho)
                    ordem = 2
                elif ordem == 2:
                    input(f"\n{'Jogada do jogador 2.':^35} \n{'Insira qualquer coisa para continuar.':^35}\n")
                    jogada_player(mao_2, mao_1, baralho)
                    ordem = 1
            case 1:
                if ordem == 1:
                    input(f"\n{'Jogada do jogador.':^35} \n{'Insira qualquer coisa para continuar.':^35}\n")
                    jogada_player(mao_1, mao_2, baralho)
                    ordem = 2
                elif ordem == 2:
                    input(f"\n{'Jogada do computador.':^35} \n{'Insira qualquer coisa para continuar.':^35}\n")
                    jogada_cpu(mao_2, mao_1, baralho)
                    ordem = 1

    declarar_vencedor(mao_1, mao_2)


continuar = True
while continuar:
    menu_principal()
    if not continuar:
        continue
    game_loop()