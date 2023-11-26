'''
DESAFIO 11
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''
n1 = int(input('Digite primeiro número: '))
n2 = int(input('Digite segundo número: '))
n3 = int(input('Digite terceiro número: '))
n4 = int(input('Digite quarto número: '))

valores = (n1, n2, n3, n4)

quantidade_nove = valores.count(9)
print(f'O número 9 apareceu {quantidade_nove} vezes.')

posicao_tres = valores.index(3)
if 3 in valores:
    print(f'O primeiro valor 3 foi digitado na posição: {posicao_tres + 1}')
else:  
    None

numeros_par = []

for valor in valores:
    if valor % 2 == 0:
        numeros_par.append(valor)
        print(f'Os números pares digitados foram {numeros_par}')
    else:
        None





