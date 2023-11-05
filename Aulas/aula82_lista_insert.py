'''
Listas em Python
Tipo list - Mutável
Suporta vários valores de quaquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concagtena listas
Create Read Update - Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
'''
#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Pedro')
nome = lista.pop()
lista.append(1234)
del lista[-1]
print(lista)
lista.insert(100, 5)
print(lista)