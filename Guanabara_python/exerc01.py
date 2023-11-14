'''
Faça um programa que leia um número inteiro e mostra na tela
seu sucessor e seu antecessor
'''

n = int(input('Digite um número: '))
print('O número {} tem o antecessor {} e o sucessor {}.'.format(n, (n-1), (n+1)))