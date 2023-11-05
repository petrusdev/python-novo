'''
Listas em Python 
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Médotos úteis:
    append, insert, opo, del, celar, extend, +
    Creat Read Update Delete
    Criar, ler, alterar, apagar = list[i] (CRUD)
'''
listas = [10, 20, 30, 40]
listas[2] = 300 # altera o indice dois da lista 
listas.append(50) # append adiciona um item a lista no final dela
listas.pop() # remove o último da lista, se quero excluir o 50 o pop tem que ser abaixo dele
listas.append(60)
listas.append(70)
ultimo_valor = listas.pop()
print(listas, 'Removido,', ultimo_valor)