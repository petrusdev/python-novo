'''
Crie um programa que leia quando dinheiro uma pessoa tem na carteira
e mostre quantos dolares ela pode comprar
'''

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 4.92
euro = real / 5.26
print(f'Com R${real:.2f} você pode comprar US${dolar:.2f} e {euro:.2f} euros.')