'''
Desenvolva um programa que leia as duas notas de um aluno,
calcule e mostre a sua media'''

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2

print('A primeira nota foi {} e a segunda {} a sua média foi {}.'.format(n1, n2, media))