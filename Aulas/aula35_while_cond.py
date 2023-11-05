# Faça um programa que conte 1 a 10 pelo while.

contador = 0

while contador < 10: # Estabeleço algo, exe menor que 10 termina, para que não fique no loop.
    contador = contador + 1 # ele soma com +1 e na próxima vez ele voltar já vem com a soma +1 de novo.
    print(contador) # o contador que ele volta é o do WHILE e não o lá de cima por isso fica somando.

print('FIM!')

# Poderia ser assim também como eu vi na aula posterior e voltei para fazer esse comentário
# exemplo abaixo de código otimizado

contato = 0

while contador <=10:
    contador += 1
    print(contador)

print('FIM')