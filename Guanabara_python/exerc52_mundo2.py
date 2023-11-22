'''
Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantos já são menores.
Considere a maioridade com 21 anos.
'''
from datetime import date

ano_atual = date.today().year
maior = 0
menor = 0

for c in range(1,8):
    nascimento = int(input(f'Em que ano a {c}ª pessoa nasceu: '))
    resultado = ano_atual - nascimento
    if resultado >= 21:
        maior += 1
    else:
        menor += 1
print(f'A quantidade de pessoas com maioridade é: {maior}')
print(f'A quantidade de pessoas são menores é: {menor}')