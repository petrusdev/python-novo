from random import randint

tentativas = 0

while True:
    jogador = ' '

    while jogador not in 'pi':
        jogador = input('Você deseja impa/par? ').lower().strip()[0]
        print('Não entendi.')
    
    jogada = int(input('Digite sua jogada de 0 a 10: '))
    maquina = randint(0,10)
    total = jogada + maquina
    

    if jogador == 'i':
        if total % 2 == 1:
            tentativas += 1
            print('Você digitou {} e a maquina {} e o total {} é IMPA. Você venceu!'.format(jogada, maquina, total))
        else:
            print('Você digitou {} e a maquina {} e o total {} é PAR. Maquina venceu!'.format(jogada, maquina, total))
            break

    elif jogador == 'p':
        if total % 2 == 0:
            tentativas += 1
            print('Você digitou {} e a maquina {} e o total {} é PAR. Você venceu!'.format(jogada, maquina, total))
        else:
            print('Você digitou {} e a maquina {} e o total {} é IMPA. Maquina venceu!'.format(jogada, maquina, total))
            break

print('GAME OVER!!! Você ganhou {} vezes.'.format(tentativas))

