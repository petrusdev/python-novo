'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas 
daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.
'''
soma = 0
for c in range(1,6 + 1):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma = soma + num
print(f'A soma dos números pares é igual: {soma}')
    