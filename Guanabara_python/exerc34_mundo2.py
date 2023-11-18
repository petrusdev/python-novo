'''
Escreva um programa que leia um número inteiro e peça para o usuário escolher qual será a base da
conversão
- 1 para binário
- 2 para octal
- 3 para hexadecimal
'''
num_int = int(input('Digite um número inteiro: ')) 
print('''Escolha uma das opções:
1 - BINÁRIO
2 - OCTAL
3 - HEXADECIMAL''')
escolha = int(input('Escolha a opção: '))

if escolha == 1:
    print(f'A representação binária de {num_int} é: {bin(num_int)[2:]}')
elif escolha == 2:
    print(f'A representação octal de {num_int} é: {oct(num_int)[2:]}')
elif escolha == 3:
    print(f'A representação hexadecimal de {num_int} é: {hex(num_int)[2:]}')
else:
    print('Opção inválida. Tente de novo.')
          

'''numero_binario = bin(num_int)[2:]
numero_octal = oct(num_int)[2:]
numero_hex = hex(num_int)[2:]

if escolha == 1:
    print(f'A representação binária de {num_int} é: {numero_binario}')
elif escolha == 2:
    print(f'A representação octal de {num_int} é: {numero_octal}')
else:
    print(f'A representação hexadecimal de {num_int} é: {numero_hex}')'''