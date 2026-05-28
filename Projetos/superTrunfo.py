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
##  Exibir a carta do topo do jogador atual (apenas nome e atributos).
##  Solicitar que o usuário escolha o atributo através do índice (Ex: "Digite 1 para Velocidade, etc.)
##  Comparar os valores.
##  Exibir o vencedor da rodada ou informar o empate.
##  Gerenciar o movimento das cartas (incluindo o monte de espera em caso de empate).



## Código de fato:

import random