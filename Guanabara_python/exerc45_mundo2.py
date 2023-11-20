'''
Crie um prorgama que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
'''

'''for c in range(1, 50):
    if c % 2 == 0:
        print(c)
Essa foi minha solucação e gastou mais laço de repetição.'''

for num in range(2, 50, 2):
    print(num, end= ' ')