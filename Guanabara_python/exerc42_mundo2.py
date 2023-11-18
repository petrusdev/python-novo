'''
Crie um programa que faça o computador jogar jokenpô com você.
'''
from random import randint
from time import sleep

print('Escolha sua jogada:\n1 - PEDRA\n2 - PAPEL\n3 - TESOURA')
escolha = int(input('Digite sua joada: '))
print('Vamos lá...')
sleep(1)
print('Pedra...')
sleep(1)
print('Papel...')
sleep(1)
print('Tesoura...')
sleep(2)

maquina = randint(1,3)

if escolha == 1 and maquina == 2:
    print('VOCÊ PERDEU! O computador escolheu PAPEL e você escolheu PEDRA.')
elif escolha == 2 and maquina == 3:
    print('VOCÊ PERDEU! O computador escolheu TESOURA e você escolheu PAPEL.')
elif escolha == 3 and maquina == 1:
    print('VOCÊ PERDEU! O computador escolheu PEDRA e você TESOURA.')
elif escolha == 2 and maquina == 1:
    print('VOCÊ VENCEU! O computador escolheu PEDRA e você escolheu PAPEL.')
elif escolha == 3 and maquina == 2:
    print('VOCÊ VENCEU! O computador escolheu PAPEL e você escolheu TESOURA.')
elif escolha == 1 and maquina == 3:
    print('VOCÊ VENCEU! O computador escolheu TESOURA e você escolheu PEDRA.')
else:
    print('Opção inválida.')