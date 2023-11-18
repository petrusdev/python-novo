'''
A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de 
um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER
'''
data_nascimento = int(input('Digite o ano do seu nascimento: '))
idade = 2023 - data_nascimento 

if idade <= 9:
    print('Categoria: MIRIM')
elif 9 < idade <= 14:
    print('Categoria: INFANTIL')
elif 14 < idade <= 19: 
    print('Categoria: JUNIOR')
elif 19 < idade <= 20:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')