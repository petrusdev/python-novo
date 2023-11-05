'''
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clar, extend, +
'''
#         01234
#         54321
string = 'ABCDE' # 5 caracteres
lista = [123, True, 'Pedro Ferreira', 1.2, []]
print(lista[2].upper(), type(lista[2]))
lista[2] = 'Maria'
print(lista[2].upper(), type(lista[2]))
