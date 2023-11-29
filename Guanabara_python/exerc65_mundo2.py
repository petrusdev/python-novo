'''
Faça uma programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
'''
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    c = 1
    for c in range(10):
        c += 1
        resultado = num * c
        print(f'{num} x {c} = {resultado}')
        

