'''
Crie um programa que peça ao usuário para inserir um número inteiro. 
Em seguida, use um loop while para exibir a tabuada desse número, ou seja, 
os múltiplos desse número de 1 a 10.
Por exemplo, se o usuário inserir o número 5, o programa deve exibir a tabuada do 5, 
que inclui os produtos de 5 x 1, 5 x 2, 5 x 3, ... até 5 x 10.
'''

numero = int(input('Digite um número: '))

for i in range(1,11):
    resultado = numero * i
    print('{} x {} = {}'.format(numero, i, resultado))