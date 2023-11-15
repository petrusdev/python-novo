'''
Faça um programa que leia o nome completo de uma pessoa, 
mostrando em seguinda o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
primeiro = Ana
último = Souza
'''
while True:
    nome = input('Digite seu nome completo: ').strip()
    nome_partes = nome.split()

    print(f'Primeiro nome: {nome_partes[0]}')
    print(f'Segundo nome: {nome_partes[-1]}')

    continuar = input('Deseja continuar? [sim/não]').strip().lower()
    if continuar != 'sim':
        break
