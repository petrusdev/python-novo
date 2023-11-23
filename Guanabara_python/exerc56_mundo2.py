'''
Melhore o jogo do DESAFIO 028 onde o computador vai 'pensar' 
em um número entre 0 e 10. Só que agora o jogador vai tentar adivinar 
até acerta, mostrando no final quantos palpites foram necessários para vencer.
'''
from random import randint
from time import sleep

print('-=-'*19)
print('\033[35mVou pensar em um número entre 1 e 10. Tente adivinhar...\033[m')
print('-=-'*19)

maquina = randint(1,10)
jogador = int(input('Em qual número eu pensei: '))
print('PROCESSANDO...')
sleep(1)

palpites = 0

while jogador != maquina:
        print(f'Você perdeu! O computador escolheu ({maquina}) e você escolheu ({jogador})')
        maquina = randint(1,10)
        jogador = int(input('Tente novamente. Em qual número eu pensei: '))

        print('PROCESSANDO...')
        sleep(1)
        
        palpites += 1
    
print(f'PARABÉNS! Você conseguiu me vencer!\nO computador escolheu ({maquina}) e você escolheu ({jogador}).')
print(f'Foi necessário {palpites} palpites para você vencer.')