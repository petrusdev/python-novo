'''
Escreva um programa que faça "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
from random import randint
from time import sleep

print('-=-'*19)
print('\033[35mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m]')
print('-=-'*19)

maquina = randint(0,5)
jogador = int(input('Em qual número eu pensei: '))
print('PROCESSANDO...')
sleep(1)

if jogador != maquina:
    print(f'GANHEI! Eu pensei no número {maquina} e não no {jogador}!')
else:
    print('PARABÉNS! Você conseguiu me vencer!')

print('FIM DE JOGO!')
