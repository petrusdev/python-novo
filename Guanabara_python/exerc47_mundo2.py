'''
Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora
utilizando o for
'''
num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1,10 +1):
    soma = num * c
    print(f'Soma de {num} x {c} = {soma}')