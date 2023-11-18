'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa. 
Calcule o IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
'''
peso = int(input('Digite seu peso(kg): '))
altura = float(input('Digite sua altura(m): '))

imc = peso / (altura ** 2)

if imc <= 18.5:
    print(f'Seu IMC é: {imc:.2f}. Abaixo do peso.')
elif 18.6 <= imc <= 24.90:
    print(f'Seu IMC é: {imc:.2f}. Normal: Que bom que você está com o peso normal!')
elif 25 <= imc <= 29.9:
    print(f'Seu IMC é: {imc:.2f}. Sobrepeso.')
elif 30 <= imc <= 34.9:
    print(f'Seu IMC é: {imc:.2f}. Obesidade grau 1: Sinal de alerta!')
elif 35 <= imc <= 39.9:
    print(f'Seu IMC é: {imc:.2f}. Obesidade grau 2.')
else:
    print(f'Seu IMC é: {imc:.2f}. Obesabidade grau 3: Aqui o sinal é \033[31mvermelho\033[m.')    