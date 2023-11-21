'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''
num = int(input('Digite um número: '))
mult = 0

for count in range(2, num):
    if (num % count == 0):
        mult = mult + 1

if (mult == 0):
    print('É primo')
else:
    print(f'Não é primo')
