'''
Escreve um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
- o primeiro valor é maior
- o segundo valor é maior
- não existe valor maior, os dois são iguais.
'''
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 > num2:
    print(f'O número {num1} é maior.')
elif num1 < num2:
    print(f'O número {num2} é o maior.')
else:
    print('Não existe valor maior, os dois são iguais.')