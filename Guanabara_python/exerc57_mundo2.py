'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novo números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''
from time import sleep

valor1 = float(input('Digite um valor: '))
valor2 = float(input('Digite outro valor: '))
opcao = 0

while opcao != 5:
    print('Escolha uma das opção:\n[1] somar\n[2] multiplicar\n[3] maior\n[4] novo números\n[5] sair do programa')
    opcao = int(input('Escolha sua opção = '))
    
    if opcao == 1:
        soma = valor1 + valor2
        print(f'{soma:.2f}')

    elif opcao == 2:
        multiplicar = valor1 * valor2
        print(f'{multiplicar:.2f}')

    elif opcao == 3:
        if valor1 > valor2:
            print(f'O primeiro valor {valor1} é maior que o segundo valor {valor2}')
        elif valor1 < valor2:
            print(f'O segundo valor {valor2} é maior que o segundo valor {valor2}')
        else:
            print('Os números são iguais.')
    elif opcao == 4:
        print('Informe os números novamente: ')
        valor1 = int(input('Digite um valor: '))
        valor2 = int(input('Digite outro valor: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Opção inválida. Tente novamente.')

print('Fim do programa! Volte sempre!')