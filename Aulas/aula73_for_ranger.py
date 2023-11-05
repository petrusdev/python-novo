# Segundo INTERÁVEL que é o RANGE
# Iterável é qualquer objeto que pode ser percorrido sequencialmente.

'''
For + Range
range -> range(start, stop, step)
'''

numeros = range(10) # Quero número de 0 a 9. Atenção: nunca vai ao final do número no caso vai para 9
numeros = range(5, 10) # Agora tenho um rage de 5 à 9. Atenção: nunca vai ao final do número no caso vai para 9
numeros = range(5, 10, 2) # Pulando número inicia 5 à 9 e pula de 2 em 2.

numeros = range(0, 10, 2)

for numero in numeros: # Para cada numero (variavel criada dentro do for) em numeros outro iterável
    print(numero) # Exibe o número