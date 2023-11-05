'''
Crie um programa que peça ao usuário para inserir um número inteiro positivo. Em seguida, 
use um loop while para contar de trás para frente a partir desse número até 1 
e exibir cada número no processo. 
Após atingir o número 1, o programa deve imprimir "Fim da contagem regressiva" e encerrar.
'''
print('Atenção: digite um número inteiro e positivo para a contagem regressiva')

numero = int(input('Digite um número: '))

if numero <= 0:
    print('Insira um número inteiro e positivo')

else:
    while numero >= 1:
        print(numero)
        numero -= 1
    print('Fim da contagem regressiva')
        