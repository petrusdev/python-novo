'''
Faça um programa que leia o comprimento do cateto oposto e do adjacente de um triângulo
retângulo, calcule e mostre o compimento da hipotenusa
'''
from math import hypot

co = float(input('Qual o comprimento cateto oposto: '))
ca = float(input('Qual o comprimento cateto adjacente: '))
hipotenusa = hypot(co, ca)
print(f'{hipotenusa:.2f}')