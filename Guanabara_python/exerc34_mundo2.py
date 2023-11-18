'''
Escreva um programa que leia um número inteiro e peça para o usuário escolher qual será a base da
conversão
- 1 para binário
- 2 para octal
- 3 para hexadecimal
'''
num_int = int(input('Digite um número inteiro: ')) 
print('Escolha a opção:\n1 - Binário\n2 - Octal\n3 - Hexadecimal')
escolha = int(input('Escolha a opção: '))

numero_binario = bin(num_int)[2:]
numero_octal = oct(num_int)[2:]
numero_hex = hex(num_int)[2:]

if escolha == 1:
    print(f'A representação binária de {num_int} é: {numero_binario}')
elif escolha == 2:
    print(f'A representação octal de {num_int} é: {numero_octal}')
else:
    print(f'A representação hexadecimal de {num_int} é: {numero_hex}')