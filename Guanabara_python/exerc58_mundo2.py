'''
Faça um programa que leia um número qualquer e mostre seu fatorial.

Ex:
5! = 5x4x3x2x1 = 120
'''

num = int(input('Digite um número: '))
contador = 1
resultado = 1

while contador <= num:
    resultado *= contador
    contador += 1
print(f'O fatorial é {num}! e o resultado é {resultado}')