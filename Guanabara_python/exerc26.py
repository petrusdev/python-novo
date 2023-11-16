'''
Escreve um programa que leia a velocidade de um carro.

Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.

A multa vai custar R$ 7,00 por cada km acima do limite.
'''

velocidade_car = int(input('Qual a velocidade atual do carro?: '))
multa = (velocidade_car - 80) * 7

if velocidade_car > 80:
    print(f'\033[31mMULTADO! Você excedeu o limite permitido que é de 80km/h\033[m. \nVocê deve pagar uma multa de R${multa:.2f}!')
else: 
    print('Tenha um bom dia! Dirija com segurança!')
