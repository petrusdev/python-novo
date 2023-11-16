'''
Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
pesquisa principio matemático ver se as retas formam um triângulo.
'''
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMA um \033[33mtriângulo\033[m.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')