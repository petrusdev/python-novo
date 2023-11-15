'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
Ex:
Digite um número: 1834
unidade: 4
dezena: 8
milhar: 1
'''
num = int(input('Digite um número: '))

num_str = str(num)

unidade = num_str[-1] 
dezena = num_str[-2] if len(num_str) >= 2 else '0'
centena = num_str[-3] if len(num_str) >= 3 else '0'
milhar = num_str[-4] if len(num_str) >= 4 else '0'

print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')