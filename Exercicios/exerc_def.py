'''
Crie uma função que multiplica todos os argumentos não nomeados recebidos
Retorne o total para uma variável e mostre o valor da variável

Crie uma função fala se um número é par ou ímpar.
Retorne se o número é par ou impar
'''

'''def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplicar(2, 3, 5)
print(multiplicacao)'''

def par_impar(numero):
    par = numero % 2 == 0

    if par:
        return f'{numero} é par'
    return f'{numero} é impar'
    
print(par_impar(5))
print(par_impar(2))
print(par_impar(6))
print(par_impar(7))
