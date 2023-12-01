'''
Faça um  programa que jogue par ou impar com o computador. O jogo será interrompido quando o jogador perder PERDER,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo
'''
from random import randint

cont = 0

while True:
    jogador = int(input('Escolha um número: '))
    escolha_jogador = str(input('Escolha sua jogada [IMPAR/PAR]: ')).strip().lower()
    computador = randint(0,10)
    resultado = jogador + computador

    if escolha_jogador == 'par':
        if resultado % 2 == 0:
            print('Você venceu!')
            cont += 1
        else:
            print(f'Você perdeu! Você venceu {cont} partidas consecutivas!')
            break
    else:
        if resultado % 2 != 0:
            print('Você venceu!')
            cont += 1
        else:
            print(f'Você perdeu! Você venceu {cont} partidas consecutivas!')
            break

    

