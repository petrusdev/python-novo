'''
Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
A) Qual é o total na compra
B) Quantos produtos custam mais de R$ 1000
C) Qual o nome do produto mais barato.
'''
total = totmil = menor = cont = 0
barato = ''

print('-'*30)
print(f'{'LOJA DO BARATÃO':^30}')
print('-'*30)
while True:
    produto = input('Nome do produto: ')
    preco = float(input('Valor: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar: [s/n]: ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'{' FIM DO PROGRAMA ':-^30}')
print(f'Total da compra: R${total:.2f}')
print(f'Temos {totmil} custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')