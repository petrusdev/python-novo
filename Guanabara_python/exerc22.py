'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome.
'''
nome = input('Digite seu nome: ').strip().upper()
if 'SILVA' in nome:
    print(f'O nome tem "SILVA".')
else:
    print('O nome não tem "SILVA"')