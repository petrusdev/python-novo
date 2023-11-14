'''
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
com 5% de desconto.
'''

produto = float(input('Qual o preço do produto? R$ '))
novo_preco = produto - (produto * 5 / 100)

print(f'O preço do produto é {produto:.2f} e com desconto 5% fica por apenas {novo_preco:.2f} reais.')