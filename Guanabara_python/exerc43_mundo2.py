''' Fazer programa que mostra meu alistamento militar'''
from datetime import date
ano_atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = ano_atual - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano_atual}')

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE.')

if idade < 18:
    resultado = 18 - idade
    ano = ano_atual + resultado
    print(f'Você ainda não tem 18 anos. Ainda faltam {resultado} anos para o alistamento.')
    print(f'Seu alistamento será em {ano}.')

elif idade > 18:
    resultado = idade - 18
    if resultado == 1:
        print(f'Você já deveria ter se alistado há {resultado} ano.')
    else:
        print(f'Você já deveria ter se alistado há {resultado} anos.')
    ano = ano_atual - resultado
    print(f'Seu alistamento foi em {ano}.')
    