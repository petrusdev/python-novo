'''
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado.
'''
dia = 60
km = 0.15

dia_alugado = float(input('Quantos dias alugados? '))
km_rodado = float(input('Quantos KM rodados? '))

total_pagar = (dia * dia_alugado) + (km * km_rodado)

print(f'O total a pagar é de R$ {total_pagar:.2f}')