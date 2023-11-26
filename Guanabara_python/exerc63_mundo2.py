'''
Crie um número que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores
lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''
quantidade_numeros_digitados = 0
maior = float('-inf')
menor = float('inf')

while True:
    entrada = (input('Digite um número: '))
   
    try:
        numero = float(entrada)
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    except ValueError:
        print('Valor inválido.')

    if quantidade_numeros_digitados >= 0:
        quantidade_numeros_digitados = quantidade_numeros_digitados + 1

    continuar = input('Deseja continuar? (s/n): ')
    if continuar.lower().strip() == 's':
        continue
    elif continuar.lower().strip() == 'n':
        break
    else:
        print('Comando inválido. Digite [s] para continuar ou [n] para encerrar o programa.')
        
media = numero / quantidade_numeros_digitados
print(f'Você digitou {quantidade_numeros_digitados} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior:.2f} e o menor foi {menor:.2f}')
print('FIM!')