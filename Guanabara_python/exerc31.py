'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salário superiores a R4 1.250,00, calcule um aumento de 10%

Para os inferiores ou iguais o aumento é de 15%.
'''
salario = float(input('Digite seu salaário: R$ '))
salario_15 = (15 * salario) / 100

if salario >= 1250:
    novo_salario = salario + (10 * salario / 100)
    print(f'Seu novo salário com aumento de 10% agora é: R${novo_salario:.2f} reais.')
else:
    novo_salario = salario + (salario * 15 / 100)
    print(f'Seu novo salário com aumento de 15% agora é: R${novo_salario:.2f} reais.')

