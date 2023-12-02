'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, 
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos
B) Quantos homens foram cadastrados
C) Quantas mulheres tem menos de 20 anos.
'''
cont_idade = 0
tot18 = 0
totH = 0

while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo [M/F]: ')).lower().upper()[0]


    if idade >= 18:
        cont_idade += 1    
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
            tot18 += 1

    continuar = ' '
    while continuar not in 'SN':   
        continuar = input('Desejar continuar [S/N]: ').strip().upper()[0]
    if continuar == 'N':
        break

print(f'A quantidade de pessoas tem mais de 18 anos: {cont_idade}')
print(f'A quantidade de homens cadastrados: {totH}')
print(f'A quantidade de mulheres que tem menos de 20 anos: {tot18}')        


