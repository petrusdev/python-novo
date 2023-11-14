'''
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
com 15% de aumento.
'''

produto = float(input('Digite seu salário: R$ '))
desconto_10 = produto - (produto * 10 /100)
desconto_20 = produto - (produto * 20 / 100)

print(f'No cartão fica: R$ {desconto_10:.2f} reais \nÀ vista fica por: R$ {desconto_20:.2f} reais')
