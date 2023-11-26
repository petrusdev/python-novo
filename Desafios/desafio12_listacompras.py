print('-'*38)
print(f'{'LISTAGEM DE PREÇOS':^38}')
print('-'*38)

lista = ('Lápis', 1.75, 'Caneta', 2, 'Caderno', 10, 'Regua', 5.50, 'Borracha', 0.75, 'Mochila', 85, 'Livros', 35,
          'Estojo', 12)

for c in range(0, len(lista)):
    if c % 2 == 0:
      print(f'{lista[c]:.<30}', end='')
    else:
      print(f'R${lista[c]:>6.2f}')
print('-'*38)
   

